function solution(board) {
    n = board.length
    let rows = new Array(n).fill(0);
    let cols = new Array(n).fill(0);
    let diag = 0;
    let antiDiag = 0;
    move = 0

    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++) {
            if(board[i][j] == 'X') {
                rows[i] += 1
                cols[j] += 1
                move += 1
            } 
            else if (board[i][j] == 'O') {
                rows[i] -= 1
                cols[j] -= 1
                move += 1
            }

            if (rows[i] == n || cols[j] == n || diag == n || antiDiag == n) {
                return 'X WIN'
            } 
            else if (rows[i] == -n || cols[j] == -n || diag == -n || antiDiag == -n) {
                return 'O WIN'
            } 
        }
    }
    if (move == n * n) {
        return 'Draw'
    } else {
        return 'Pending'
    }
}

board1 = ['XO', 'X.'] // 'X WIN'
board2 = ['XOX', 'OXO', '.X.'] // 'ONGOING'
console.log(solution(board1))
console.log(solution(board2))