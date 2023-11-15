function solution(user_id, banned_id) {
    var answer = new Set();

    function dfs(level, selected) {
        if (level === banned_id.length) {
            answer.add([...selected].sort().join(','));
            return;
        }

        for (let i = 0; i < user_id.length; i++) {
            let user = user_id[i];
            let banned = banned_id[level];

            if (!selected.has(i) && isMatched(user, banned)) {
                selected.add(i);
                dfs(level + 1, selected);
                selected.delete(i);
            }
        }
    }

    function isMatched(user, banned) {
        if (user.length !== banned.length) return false;
        for (let i = 0; i < user.length; i++) {
            if (banned[i] !== '*' && user[i] !== banned[i]) {
                return false;
            }
        }
        return true;
    }

    dfs(0, new Set());

    return answer.size;
}
