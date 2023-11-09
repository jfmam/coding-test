

// 현재 진행된 거리가 목표지점보다 멀어지면 종료
function distance(x,y,r,c) {
    return Math.abs(r-x) + Math.abs(c-y)
}

function solution(n, m, x, y, r, c, k) {
    function dfs(i,j,s,cnt) {
        if(k < cnt + distance(i,j,r,c)) {
            return;
        }
        
        if(i===r && j === c && cnt === k) {
          answer = s
          return
        }
        
        for(let v = 0; v < move.length; v++) {
            let ii = move[v][0] + i
            let jj = move[v][1] + j
            
            if((1 <= ii && ii <= n) && (1 <= jj && jj <= m) && s < answer) {
                dfs(ii,jj, s + str[v], cnt+1)
            }
        }
    }
    
    var answer = 'z';
    const move = [[1,0],[0,-1],[0,1],[-1,0]]
    const str = ['d','l','r','u']
    const dist = Math.abs(r-x) + Math.abs(c-y)
    if(dist > k || (k-dist) % 2 === 1) return 'impossible'
    
    dfs(x,y,'',0)

    return answer
}