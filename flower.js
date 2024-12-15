// let e = [];

// for (i=0; i<hearPoints; i++){
//     let x = rand() * width;
//     let y rand() * innerHeight=;
    
//     e[i] ={
//         vx: 0,
//         vy: 0,
//         R: 2,
//         speed: rand() + 5,
//         q:(rand()*heartPointsCount),
//         D: 2 * (i % 2) - 1,
//         force : 0.2 rand () + 0.7,
//         f:"hsla(0," + (40 * rand() + 60) + '%, ' + (60*rand()+20)+ "%.3",
//         trace: []
//     };
//     for (let k=0; k< traceCount; k++){
//         e[i].trace[k] = {x: x, y: y};
//     }
//     }
// }

let e = [];

for (let i = 0; i < hearPoints; i++) {
    let x = Math.random() * width;
    let y = Math.random() * innerHeight;

    e[i] = {
        vx: 0,
        vy: 0,
        R: 2,
        speed: Math.random() + 5,
        q: Math.floor(Math.random() * heartPointsCount),
        D: 2 * (i % 2) - 1,
        force: 0.2 * Math.random() + 0.7,
        f: "hsla(0," + (40 * Math.random() + 60) + "%, " + (60 * Math.random() + 20) + "%, 0.3)",
        trace: []
    };

    for (let k = 0; k < traceCount; k++) {
        e[i].trace[k] = { x: x, y: y };
    }
document.body.innerHTML = `<pre>${JSON.stringify(e, null, 2)}</pre>`;

}
