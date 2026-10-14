const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const html = fs.readFileSync(process.argv[2] || path.resolve(__dirname, "../index.html"), "utf8");
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const ctx = vm.createContext({});
for (const name of ["boxes", "singleContactOrder", "angles"]) {
  vm.runInContext(script.match(new RegExp("const " + name + "=[^;]+;"))[0], ctx);
}
vm.runInContext(script.slice(script.indexOf("const rigs="), script.indexOf("function polygon")), ctx);
vm.runInContext(script.slice(script.indexOf("function gait("), script.indexOf("function drawRigLeg(")), ctx);
const run = code => vm.runInContext(code, ctx);
assert.equal(run("singleContactOrder.join(',')"), "2,12,15,3,4,5,6,7,8,9,10,11,13,14,0,1");
assert.equal(run("angles.join(',')"), "0,0,0,0,0,0,0,0,1,5,8,9,8,6,4,2");
assert.equal(run("rigs.map(r=>r.name).join(',')"), "right,left");
let dualSupport = 0;
const swingCounts = { left: 0, right: 0 };
for (let frame = 0; frame < 16; frame++) {
  const poses = run("rigs.map(r=>gait(" + frame + ",r,[500,340]))");
  assert(poses.some(p => p.stance), "At least one hind paw must support");
  if (poses.every(p => p.stance)) dualSupport++;
  poses.forEach((p, i) => { if (!p.stance) swingCounts[i ? "left" : "right"]++; });
}
assert.equal(dualSupport, 4);
assert.deepEqual(swingCounts, { left: 6, right: 6 });
let samples = 0;
for (const strength of [0, 100, 150]) for (let frame = 0; frame < 16; frame++) for (const fraction of [0, .25, .5, .75]) {
  const results = run(`(() => {
    const frame=${frame},fraction=${fraction},strength=${strength},phase=frame+fraction;
    const [left,top,right,bottom]=boxes[singleContactOrder[frame]],scale=410/(right-left),pivot=left+(right-left)*.7;
    const angle=(angles[frame]+(angles[(frame+1)%16]-angles[frame])*fraction)*strength/100*Math.PI/180;
    const lift=Math.max(0,Math.sin(angle)*410*.3);
    return rigs.map(r=>{
      const dx=(r.hip[0]-pivot)*scale,dy=(r.hip[1]-bottom)*scale;
      const hip=[500+dx*Math.cos(angle)-dy*Math.sin(angle),450-lift+dx*Math.sin(angle)+dy*Math.cos(angle)];
      const state=gait(phase,r,hip),joints=solveLeg(r,hip,state);
      const lengths=joints.slice(0,3).map((p,i)=>Math.hypot(joints[i+1][0]-p[0],joints[i+1][1]-p[1]));
      const expected=r.source.slice(0,3).map((p,i)=>Math.hypot(r.source[i+1][0]-p[0],r.source[i+1][1]-p[1])*410/311);
      const rx=r.name==="left"?20:18,theta=state.toeAngle;
      const sole=state.foot[1]+(410/311)*(r.name==="right" ? Math.max(-22*Math.sin(theta),14*Math.sin(theta))+9*Math.cos(theta) : -4*Math.sin(theta)+Math.cos(theta)+Math.hypot(rx*Math.sin(theta),8*Math.cos(theta)));
      return {state,joints,lengths,expected,sole};
    });
  })()`);
  assert(results.some(p=>p.state.stance));
  for (const p of results) {
    assert(p.joints.flat().every(Number.isFinite));
    p.lengths.forEach((len,i)=>assert(Math.abs(len-p.expected[i])<1e-6, "Bone length must stay fixed"));
    if (p.state.stance) assert(Math.abs(p.sole-450)<1e-6, "Painted paw sole must meet ground");
    else assert(p.sole<450.01, "Swing paw must clear ground");
  }
  samples++;
}
for (const name of ["left", "right"]) {
  const result = run(`(() => {
    const r=rigs.find(r=>r.name==="${name}");
    const a=gait(0,r,[500,340]),b=gait(16,r,[500,340]);
    return [a.foot,b.foot,a.stance,b.stance];
  })()`);
  assert.deepEqual(Array.from(result[0]), Array.from(result[1]));
  assert.equal(result[2], result[3]);
}
console.log("PASS: " + samples + " poses; fixed limb identity and bone lengths; grounded stance; airborne swing; four double-support frames; cycle wrap; unchanged forehand parameters.");

