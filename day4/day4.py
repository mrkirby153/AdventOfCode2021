
class Board():

    def __init__(self, data):
        # Generate a 5x5 board with all spaces unmarked
        self.board = list(map(lambda x: list(map(lambda y: (y, False), x)), data))
        self.has_won = False
    
    def mark_numbers(self, numbers):
        for number in numbers:
            self.mark_number(number)

    def mark_number(self, number):
        for x in range(0, 5):
            for y in range(0, 5):
                if self.board[x][y][0] == number:
                    self.board[x][y] = (number, True)
    
    def print_board(self):
        for x in range(0, 5):
            for y in range(0, 5):
                num = self.board[x][y][0]
                num = str(num) if num > 9 else ' ' + str(num)
                color = '\033[92m' if self.board[x][y][1] else '\033[91m'
                print(color + num, end=" ")
            print()
        print('\033[0m') # Reset color
    
    def is_board_winner(self):
        # Check if any row, or column is a winner
        for x in range(0, 5):
            if self.board[x][0][1] and self.board[x][1][1] and self.board[x][2][1] and self.board[x][3][1] and self.board[x][4][1]:
                return True
            if self.board[0][x][1] and self.board[1][x][1] and self.board[2][x][1] and self.board[3][x][1] and self.board[4][x][1]:
                return True
        return False

    def reset_board(self):
        for x in range(0, 5):
            for y in range(0, 5):
                self.board[x][y] = (self.board[x][y][0], False)



with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

calls = input_data[0].split(',')

raw_boards = []

boards = input_data[2:]

curr_board_nums = []
for i in range(len(boards)):
    board_row = boards[i]
    if board_row == "":
        raw_boards.append(curr_board_nums)
        curr_board_nums = []
        continue
    curr_row_nums = []
    while len(board_row) > 0:
        # Consume 2 characters for the number
        num = int(board_row[:2])
        curr_row_nums.append(num)
        # Consume 1 more character for the space
        board_row = board_row[3:]
    curr_board_nums.append(curr_row_nums)

raw_boards.append(curr_board_nums)

raw_boards = list(map(lambda x: Board(x), raw_boards))

def mark_all_boards(call):
    for board in raw_boards:
        if board.has_won:
            continue # If the board has won, stop calling it
        board.mark_number(call)

def part_1():
    for call in calls:
        mark_all_boards(int(call))
        if any(map(lambda x: x.is_board_winner(), raw_boards)):
            # There's a winner
            print("Some board is a winner!")
            winner = list(filter(lambda x: x.is_board_winner(), raw_boards))[0]
            winner.print_board()

            # Sum unmarked spaces
            sum = 0
            for x in range(0, 5):
                for y in range(0, 5):
                    if winner.board[x][y][1] == False:
                        sum += winner.board[x][y][0]
            return sum * int(call)


def part_2():
    last_winner = None
    last_call = None
    for call in calls:
        last_call = call
        mark_all_boards(int(call))
        winning_boards = list(filter(lambda x: x.is_board_winner() and not x.has_won, raw_boards))
        if len(winning_boards) > 0:
            for b in winning_boards:
                b.has_won = True
                last_winner = b
            if all(map(lambda x: x.has_won, raw_boards)):
                print("All boards have won!")
                break
    print("The last board to win: ")
    last_winner.print_board()


    # Sum unmarked spaces
    sum = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if last_winner.board[x][y][1] == False:
                sum += last_winner.board[x][y][0]
    return sum * int(call)


print(f"Part 1: {part_1()}")
map(lambda x: x.reset_board(), raw_boards) # Reset the boards
print(f"Part 2: {part_2()}")
