const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = [];

rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    console.log('1',n,m)
    console.log('2',input)
   process.exit();
})