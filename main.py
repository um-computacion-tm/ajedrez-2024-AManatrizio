from game.chess import Chess


def main():
    game = Chess()
    while not game.is_over():
        game.display_board()
        move = input("Enter your move: ")
        if not game.play_move(move):
            print("Invalid move! Try again.")
            


if __name__ == "__main__":
    main()
    
    