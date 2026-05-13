import turtle
import time
BOARD_SIZE = 800
CELL_SIZE = BOARD_SIZE // 3
WIN_CONDITIONS = [
    # Rows
    [(0, 0), (0, 1), (0, 2)], 
    [(1, 0), (1, 1), (1, 2)], 
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)], 
    [(0, 1), (1, 1), (2, 1)], 
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)], 
    [(0, 2), (1, 1), (2, 0)]
]
screen = turtle.Screen()
pen = turtle.Turtle()
clicked_row = None
clicked_col = None 

def setup_turtle():
    screen.setup(width = BOARD_SIZE, height = BOARD_SIZE)
    screen.title("Turtle Tic Tac Toe")
    screen.setworldcoordinates(0, 0, BOARD_SIZE, BOARD_SIZE)
    pen.speed(10)
    pen.hideturtle()
    pen.pensize(5)

def draw_grid():
    pen.penup()
    for i in range(1, 3):
        # Draw vertical lines
        pen.goto(i * CELL_SIZE, 0)
        pen.pendown()
        pen.goto(i * CELL_SIZE, BOARD_SIZE)
        pen.penup()
        # Draw horizontal lines
        pen.goto(0, i * CELL_SIZE)
        pen.pendown()
        pen.goto(BOARD_SIZE, i * CELL_SIZE)
        pen.penup()

def draw_x(x, y):
    padding = CELL_SIZE * 0.1
    pen.pencolor("red")

    pen.penup()
    # Line 1: From bottom-left
    pen.goto(x + padding, y + padding)
    pen.pendown()
    # To top-right
    pen.goto(x + CELL_SIZE - padding, y + CELL_SIZE - padding)

    pen.penup()
    # Line 2: From bottom-right
    pen.goto(x + CELL_SIZE - padding, y + padding)
    pen.pendown()
    # To top-left
    pen.goto(x + padding, y + CELL_SIZE - padding)
    pen.penup()

def draw_o(x, y):
    radius = CELL_SIZE * 0.4
    pen.pencolor("blue")

    pen.penup()
    # Circle is positioned in the middle of the square
    # (CELL_SIZE / 2, CELL_SIZE / 2)
    # Move the y position down by radius because
    # the circle function starts drawing from the bottom
    pen.goto(x + CELL_SIZE / 2, y + CELL_SIZE / 2 - radius)

    pen.pendown()
    pen.circle(radius)
    pen.penup()

def draw_symbol(row, col, symbol):
    # Convert row and column input into window coordinates
    start_x = col * CELL_SIZE
    # (2 – row) is used to flip the y-axis so that
    # row 0 is the top and row 2 is the bottom
    start_y = (2 - row) * CELL_SIZE

    if symbol == "X":
        # Call the draw_x function if symbol is "X"
        draw_x(start_x, start_y)
    elif symbol == "O":
        # Call the draw_O function if symbol is "O"
        draw_o(start_x, start_y)

def initialize_board():
    # Create a 3x3 nested list using nested for loops
    board = []

    # Outer loop iterates 3 times (rows)
    for i in range(3):
        row = []
        # Inner loop iterates 3 times (columns)
        for i in range(3):
            row.append(' ')
        board.append(row)

    return board

def get_player_move(board, current_symbol):
    # Cast the input to integer
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    # Access the board and set value
    board[row][col] = current_symbol

def check_full(board):
    # Access the lists in board
    for row in board:
        # Access the elements in the list
        for col in row:
            # Check if it is empty
            if col == ' ':
                # Return false if space is found
                return False
    # Return true after looping through the board
    return True

def switch_symbol(current_symbol):
    if current_symbol == "X":
        return "O"
    else:
        return "X"
    
def check_win(board):
    for condition in WIN_CONDITIONS:
        # If all cells of that winning condition are holding the
        # same symbol and is not empty then there is a winner
        if board[condition[0][0]][condition[0][1]] == \
           board[condition[1][0]][condition[1][1]] == \
           board[condition[2][0]][condition[2][1]] != ' ':
            return True
    # Return false if no winner is found     
    return False

def record_click_position(x,y):
    global clicked_row, clicked_col

    col = int(x // CELL_SIZE)
    # BOARD_SIZE -y flips the y coordinate
    row = int((BOARD_SIZE - y) // CELL_SIZE)

    if row >=0 and row < 3 and col >=0 and col <3:
        clicked_row = row
        clicked_col = col

def wait_for_click():
    global clicked_row,clicked_col

    # Resets the previous click
    clicked_col = None
    clicked_row = None
    # Returns the x and y coordinates of the mouse when
    # the player clicks and calls record_click_position
    screen.onclick(record_click_position)
    # Wait until the player clicks
    while clicked_row is None:
        turtle.update()
        time.sleep(0.01)

    screen.onclick(None)
    return clicked_row, clicked_col


def get_player_move_turtle(board, current_symbol):
    while True:
        # Receive the row and col of the click
        row, col = wait_for_click()
        
        # Check if the square is empty
        if board[row][col] == ' ':
            # Draw symbol at the clicks position
            board[row][col] = current_symbol
            draw_symbol(row, col, current_symbol)
            break
        else:
            print("Spot already taken! Choose again.")

def display_message(message):
    pen.penup()
    pen.goto(BOARD_SIZE/2,BOARD_SIZE/2-50)
    pen.pencolor("black")
    pen.write(message, align="center", font=("Arial",32,"bold"))

# Initialize the board to a variable
board = initialize_board()
# Initialize the starting symbol
current_symbol = "X"



# for i in range(9):

#     get_player_move(board, current_symbol)

#     # Print inner lists in rows
#     for row in board:
#         print(row)
    
#     # Break out of the loop when the board is full
#     if check_full(board) == True:
#         print("Board is full.")
#         break

#     # Break out of the loop when there is a winner
#     if check_win(board) == True:
#         print(f"{current_symbol} wins!")
#         break

#     current_symbol = switch_symbol(current_symbol)


setup_turtle()
draw_grid()

while True:
    get_player_move_turtle(board, current_symbol)
    current_symbol = switch_symbol(current_symbol)
    if check_win(board):
        display_message(f"Player {current_symbol} wins!")
        break
    elif check_full(board) == True:
        display_message("It's a draw!")
        break

screen.mainloop()