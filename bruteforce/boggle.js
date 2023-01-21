// 보글게임
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
const board = ["Y","E","S", "I", "N","Y","E","S", "I", "N","Y","E","S", "I", "N","Y","E","S", "I", "N","Y","E","S", "I", "N"];
const n = 5;


// 이동하기
const dx = [-1,-1,0,1,1,1,0,-1];
const dy = [0,1,1,1,0,-1,-1,-1];

function hasWord(str, x, y) {
    if(x < 0 || y < 0) return;
    if(x >= n || y >=n) return;

}





rl.on("line", (line) => {
    board.push(line)
}).on("close", () => {
    console.log();
    process.exit();
})