function solution(cacheSize, cities) {
    var answer = 0
    let cache = [];
   
    for(let i of cities) {
        i = i.toLowerCase();
        if(cache.find(v => v === i)){
            answer += 1
            cache = cache.filter(v => v !== i).concat(i)
        }
        else {
            answer += 5;
            
            if(cacheSize === 0) {
                continue
            }
            
            if (cache.length >= cacheSize) {
                cache.shift()
            }
            cache.push(i)
        }
    }
    return answer;
}