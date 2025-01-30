
import math
import copy

# Constants
X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def player(board):
    cx = 0
    co = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                cx += 1
            if board[row][col] == O:
                co += 1
    if cx > co:
        return O
    else:
        return X


def actions(board):
    possible_actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    return possible_actions


def result(board, action):
    if action not in actions(board):
        raise Exception("not valid action")
    row, col = action
    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def check_row(board, player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_col(board, player):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def dig1(board, player):
    count = 0
    for row in range(3):
        for col in range(3):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


def dig2(board, player):
    count = 0
    for row in range(3):
        for col in range(3):
            if (3 - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


def winner(board):
    if check_col(board, X) or check_row(board, X) or dig1(board, X) or dig2(board, X):
        return X
    if check_col(board, O) or check_row(board, O) or dig1(board, O) or dig2(board, O):
        return O
    else:
        return None


def terminal(board):
    return winner(board) is not None or all(all(cell != EMPTY for cell in row) for row in board)


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
************************************************************************************************************************************main*********************************************************************************************************
import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 500, 400

# Colors
black = (255, 228, 196)
white = (255, 239, 219)
screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, (233, 150, 122))
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, (0, 197, 205))  # Color for X
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, (255, 62, 150))  # Color for O
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, (205, 183, 158), rect, 3)

                if board[i][j] != ttt.EMPTY:
                    if board[i][j] == ttt.X:
                        move = moveFont.render(board[i][j], True, (0, 197, 205))  # Color for X
                    else:
                        move = moveFont.render(board[i][j], True, (255, 62, 150))  # Color for O
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, (233, 150, 122))
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, (233, 150, 122))
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()

