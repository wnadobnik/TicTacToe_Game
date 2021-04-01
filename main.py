import random


class TicTacToe:

    # param1 defines x and y dimension of the board
    # param2 if True, player plays wirh circles
    # param3 if True, player starts the game

    def __init__(self, board_size, player_circles=True, player_first=True):

        # assign marks to player and computer
        if player_circles:
            self.mark_player = '[o]'
            self.mark_computer = '[x]'
        else:
            self.mark_player = '[x]'
            self.mark_computer = '[o]'

        # assign first move
        if player_first:
            self.next_move = self.mark_player
        else:
            self.next_move = self.mark_computer

        # state of the game variables
        self.last_move_loc = {'x': '', 'y': ''}
        self.move_count = 0

        # board preparation
        self.board_size = board_size
        self.board = [['[ ]' for line in range(self.board_size)] for field in range(self.board_size)]

    # prints board

    def display(self):
        print('____________________')
        for line in self.board:
            line_display = ''
            for field in line:
                line_display += field
            print(line_display)

    # checks if move is possible, registers co-ordinates and changes move count

    def log_move(self, coord_x, coord_y):
        if self.board[coord_y][coord_x] == '[ ]':
            self.board[coord_y][coord_x] = self.next_move
            self.last_move_loc['x'], self.last_move_loc['y'] = coord_x, coord_y
            if self.next_move == self.mark_computer:
                self.next_move = self.mark_player
            else:
                self.next_move = self.mark_computer
            self.move_count += 1
            return True
        else:
            return False

    # Computer player "AI". Checks for opportunities to win. Acts on the first opportunity

    def computer_move(self):

        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.is_computer(x, y):
                    # horizontal check - a marks current field
                    # [a][x][ ]
                    if self.is_computer(x + 1, y) and self.is_available(x + 2, y):
                        self.log_move(x + 2, y)
                        return
                    # [a][ ][ ]
                    elif self.is_available(x + 1, y) and self.is_available(x + 2, y):
                        self.log_move(x + 1, y)
                        return
                    # [ ][a][ ]
                    elif self.is_available(x - 1, y) and self.is_available(x + 1, y):
                        self.log_move(x + 1, y)
                        return
                    # [ ][ ][a]
                    elif self.is_available(x - 1, y) and self.is_available(x - 2, y):
                        self.log_move(x - 1, y)
                        return
                    # [ ][x][a]
                    elif self.is_computer(x - 1, y) and self.is_available(x - 2, y):
                        self.log_move(x - 2, y)
                        return
                    # vertical check - a marks current field
                    # [a][x][ ]
                    elif self.is_computer(x, y + 1) and self.is_available(x, y + 2):
                        self.log_move(x, y + 2)
                        return
                    # [a][ ][ ]
                    elif self.is_available(x, y + 1) and self.is_available(x, y + 2):
                        self.log_move(x, y + 1)
                        return
                    # [ ][a][ ]
                    elif self.is_available(x, y - 1) and self.is_available(x, y + 1):
                        self.log_move(x, y + 1)
                        return
                    # [ ][ ][a]
                    elif self.is_available(x, y - 1) and self.is_available(x, y - 2):
                        self.log_move(x, y - 1)
                        return
                    # [ ][x][a]
                    elif self.is_computer(x, y - 1) and self.is_available(x, y - 2):
                        self.log_move(x, y - 2)
                        return
                    # angle check 1 - - a marks current field
                    # [a][x][ ]
                    elif self.is_computer(x + 1, y + 1) and self.is_available(x + 2, y + 2):
                        self.log_move(x + 2, y + 2)
                        return
                    # [a][ ][ ]
                    elif self.is_available(x + 1, y + 1) and self.is_available(x + 2, y + 2):
                        self.log_move(x + 1, y + 1)
                        return
                        # [ ][a][ ]
                    elif self.is_available(x - 1, y - 1) and self.is_available(x + 1, y + 1):
                        self.log_move(x + 1, y + 1)
                        return
                    # [ ][ ][a]
                    elif self.is_available(x - 1, y - 1) and self.is_available(x - 2, y - 2):
                        self.log_move(x - 1, y - 1)
                        return
                    # [ ][x][a]
                    elif self.is_computer(x - 1, y - 1) and self.is_available(x - 2, y - 2):
                        self.log_move(x - 2, y - 2)
                        return
                    # angle check 2 - a marks current field
                    # [a][x][ ]
                    elif self.is_computer(x - 1, y + 1) and self.is_available(x - 2, y + 2):
                        self.log_move(x - 2, y + 2)
                        return
                    # [a][ ][ ]
                    elif self.is_available(x - 1, y + 1) and self.is_available(x - 2, y + 2):
                        self.log_move(x - 1, y + 1)
                        return
                    # [ ][a][ ]
                    elif self.is_available(x + 1, y - 1) and self.is_available(x - 1, y + 1):
                        self.log_move(x - 1, y + 1)
                        return
                    # [ ][ ][a]
                    elif self.is_available(x + 1, y - 1) and self.is_available(x + 2, y - 2):
                        self.log_move(x + 1, y - 1)
                        return
                    # [ ][x][a]
                    elif self.is_computer(x + 1, y - 1) and self.is_available(x + 2, y - 2):
                        self.log_move(x + 2, y - 2)
                        return
                if self.is_available(x, y) and self.is_available(x + 1, y) and self.is_available(x + 2, y):
                    self.log_move(x, y)
                elif self.is_available(x, y) and self.is_available(x, y + 1) and self.is_available(x, y + 2):
                    self.log_move(x, y)
                elif self.is_available(x, y) and self.is_available(x + 1, y + 1) and self.is_available(x + 2, y + 2):
                    self.log_move(x, y)
                elif self.is_available(x, y) and self.is_available(x - 1, y + 1) and self.is_available(x - 2, y + 2):
                    self.log_move(x, y)

    # check if field exists and is empty

    def is_available(self, coord_x, coord_y):
        if coord_x <= self.board_size - 1 and coord_y <= self.board_size - 1:
            if self.board[coord_y][coord_x] == '[ ]':
                return True
        else:
            return False

    def is_computer(self, coord_x, coord_y):
        if coord_x <= self.board_size - 1 and coord_y <= self.board_size - 1:
            if self.board[coord_y][coord_x] == self.mark_computer:
                return True
        else:
            return False

    def check_victory(self):
        pass


a = TicTacToe(3, True)
while True:
    x = int(input())
    y = int(input())
    a.log_move(x, y)
    a.display()
    a.computer_move()
    a.display()
