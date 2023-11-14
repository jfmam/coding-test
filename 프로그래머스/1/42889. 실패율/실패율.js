function solution(N, stages) {
    var answer = [];
    let people = stages.length
    let failList = {}
    
    for(let i = 1; i <= N; i++) {
        let failPeople = stages.filter((v) => v === i).length
        if(failPeople === 0) failList[i] = 0
        else failList[i] = failPeople / people
        people -= failPeople
    }
    answer = Object.entries(failList).sort((a,b) => b[1] - a[1])
    return answer.map(v => +v[0]);
}