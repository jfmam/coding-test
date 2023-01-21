// 2차원 배열과 정수형으로 받기
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const input = [];
let n,m;
let isData = true;
rl.on("line", line => {
    if(isData) {
        [n,m] = line.split(' ').map(v => parseInt(v));
        isData = false;
    } else {
        input.push(line.split(' ').map(v => parseInt(v)));
    }
}).on("close", () => {
    console.log(n,m)
    console.log(input);
    process.exit()
})