const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = []

rl.on("line", (line) => {
    input.push(line.trim());
})

rl.on("close", () => {
    const C = Number(input[0]);
    for(let i = 0; i<C; i++) {
       let N,M;
       let Pair = [];
       [N,M] = input[i*2 +1].split(" ").map(v1 => Number(v1));
       Pair = input[i*2 + 2].split(" ").map(v2 => Number(v2))
       solution(N,M,Pair);
    }
    process.exit();
})

// 2차원 배열 초기화, 짝궁이 될 수 있는 경우를 true로 표시
const makeMatrix = (row) => {
    let mat = [];
    for (let i = 0; i < row; i++) {
        let a = [];
        for (let j = 0; j < row; j++) {
            a.push(false);
        }
        mat.push(a);
    }
    return mat;
}

const solution = (n,m,pair) => {
    const areFriends = makeMatrix(n);
  
    let temp = 0;
    pair.forEach((v, idx) => {
        if(!(idx % 2)){
            temp = v;
        }
        else {
            areFriends[temp][v] = true;
            areFriends[v][temp] = true;
        }
    });
    
    const countParings = (taken) => {
        let firstFree = -1;
        for(let i = 0; i<n;i++) {
            if(!taken[i]) {
                // 짝을 만들지 않은 학생들 중 가장 번호가 빠른 것찾기
                firstFree = i;
                break;
            }
        }
  
        // 기저사례: 모든학생이 짝을 찾았을 경우 1을반환한다.
        if(firstFree == -1) {
            return 1;
        }

        let ret = 0;
        // firstFree로 찍힌 학생과 짝이 되기 위한 학생을 고른다.
        for(let pairWith = firstFree +1; pairWith <n; pairWith++) {
            // 조건으로는 짝이없고 짝궁인 경우
           if(!taken[pairWith] && areFriends[firstFree][pairWith]) {
            // 해당 조건이 만족할 때 두가지로 나뉜다. 짝궁이 되는 경우와 되지 않는 경우
            // 짝이 되었으면 taken 함수에 표시해준다. 짝궁이 되었을 경우 ret에 +를 해준다
            taken[firstFree] = taken[pairWith] = true;
            ret += countParings(taken);
            // 짝궁이 될 수 있지만 짝이 되지 않는경우가 있을수도 있음으로 false로 표시하는 경우
            taken[firstFree] = taken[pairWith] = false;
            // ret += 0;
           } 
        }
        return ret;
    }
     
    console.log(countParings(Array(n).fill(false)));
}