import random


class Game:
    def __init__(self):
        self.board = [['-' for x in range(3)] for y in range(3)]

    def get_cell(self, x: int, y: int) -> str:
        return self.board[x][y]

    def set_cell(self, x: int, y: int, value) -> None:
        self.board[x][y] = value

    def random_choice(self) -> None:
        return random.choice(['X', '0'])

    def check_winner(self) -> str:
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != '-':
                return f'winner = {row[0]}'

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '-':
                return f'winner = {self.board[0][col]}'

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            return  f'winner = {self.board[0][0]}'
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
            return f'winner = {self.board[0][2]}'

    def __str__(self) -> str:
        return '\n'.join([' '.join(row) for row in self.board])

if __name__ == "__main__":
    board = Game()
    player = board.random_choice()
    print(f'You play {player}')
    print(board)
    print(f'insert x, y coordinates betwen 0-2')
    while board.check_winner() == None:
        result_input = input('Insert coordinates betwen 0-2 \n')
        input_list = result_input.split()
        x = (int(input_list[0]))
        y = (int(input_list[1]))
        board.set_cell(x,y, player)
        print(board)
        print(board.check_winner())

