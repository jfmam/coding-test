function solution(commands) {
  let answer = [];
  const cell = Array(51)
    .fill()
    .map((_) => Array(51).fill(''));
  const parent = Array(51)
    .fill()
    .map((_, i) =>
      Array(51)
        .fill()
        .map((_, j) => [i, j])
    );

  for (const commandStr of commands) {
    const [command, ...rest] = commandStr.split(' ');

    switch (command) {
      case 'UPDATE':
        if (rest.length === 3) update(rest);
        else replace(rest);
        break;
      case 'MERGE':
        merge(rest);
        break;
      case 'UNMERGE':
        unmerge(rest);
        break;
      case 'PRINT':
        answer = [...answer, print(rest)];
        break;
    }
  }

  return answer;

  function update(param) {
    const [r, c, value] = param;
    const target = find([r, c]);

    iterateAll((i, j) => {
      if (isSameCoords(parent[i][j], target)) cell[i][j] = value;
    });
  }

  function replace(param) {
    const [value1, value2] = param;

    iterateAll((i, j) => {
      if (cell[i][j] === value1) cell[i][j] = value2;
    });
  }

  function merge(param) {
    const [r1, c1, r2, c2] = param;
    if (r1 === r2 && c1 === c2) return;

    const value = cell[r1][c1] !== '' ? cell[r1][c1] : cell[r2][c2];
    const parent1 = find([r1, c1]);
    const parent2 = find([r2, c2]);

    if (!isSameCoords(parent1, parent2)) {
      parent[r2][c2] = parent1;
    }

    iterateAll((i, j) => {
      if (isSameCoords(parent[i][j], parent2)) {
        parent[i][j] = parent1;
      }
      if (isSameCoords(parent[i][j], parent1)) {
        cell[i][j] = value;
      }
    });
  }

  function unmerge(param) {
    const [r, c] = param;
    const value = cell[r][c];
    const target = find([r, c]);

    iterateAll((i, j) => {
      if (isSameCoords(parent[i][j], target)) {
        cell[i][j] = '';
        parent[i][j] = [i, j];
      }
    });

    cell[r][c] = value;
  }

  function print(param) {
    const [r, c] = param;

    return cell[r][c] === '' ? 'EMPTY' : cell[r][c];
  }

  function find(coord) {
    const [r, c] = coord;

    if (isSameCoords([r, c], parent[r][c])) {
      return [Number(r), Number(c)];
    }

    parent[r][c] = find(parent[r][c]);

    return parent[r][c];
  }

  function isSameCoords(coord1, coord2) {
    return coord1.toString() === coord2.toString();
  }

  function iterateAll(callbackFn) {
    for (let i = 0; i < 51; i++) {
      for (let j = 0; j < 51; j++) {
        callbackFn(i, j);
      }
    }
  }
}