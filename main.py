from game.chess import Chess


def main():
    chess = Chess()
    while not chess.is_over():
        chess.display_board()
        chess.get_captures
        print(f"Turno de: {chess.current_player}")
        piece = input("Enter your piece to move: ")
        move = input("Enter where to move: ")
        if not chess.play_move(piece,move):
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()
    
    