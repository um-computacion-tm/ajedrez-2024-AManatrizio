from game.chess import Chess

def display_menu():
    print("\nMenu:")
    print("1. Make a move")
    print("2. View score (captures)")
    print("3. End game by mutual agreement")
    print("4. Quit")

def display_game_status(chess):
    chess.display_board()
    chess.get_captures()
    print(f"\nTurn of: {chess.__current_player__}")

def handle_move(chess):
    print("To move a piece, type the row number followed by \nthe column number without any spaces. For example: 62")
    piece = input("Enter your piece to move: ")
    move = input("Enter where to move: ")
    result = chess.play_move(piece, move)
    
    if isinstance(result, tuple):
        result, info = result
    else:
        info = None

    if result == "INVALID_TURN":
        print("It's not your turn!")
    elif result == "INVALID_CAPTURE":
        print("You can't capture your own piece!")
    elif result == "INVALID":
        print("Invalid move! Try again.")
    elif result == "KING_CAPTURED":
        winning_color = "White" if info == "BLACK" else "Black"
        print(f"The {winning_color} player has captured the king! Game over.")
    elif result == "PROMOTION_NEEDED":
        fila, columna = info
        print("Pawn promotion! Choose a piece to promote to:")
        print("1. Queen")
        print("2. Rook")
        print("3. Bishop")
        print("4. Knight")
        choice = input("Enter your choice (1-4): ")
        promoted_piece = chess.promote_pawn(fila, columna, choice)
        print(f"Pawn promoted to {promoted_piece}")
    elif result == "VALID":
        print("Move successful!")

def handle_view_score(chess):
    captures = chess.get_captures()
    print(f"\nWhite captures: {captures['__white_captures__']}")
    print(f"\nBlack captures: {captures['__black_captures__']}")


def handle_end_game_agreement(chess):
    confirm = input("Are you sure you want to end the game by mutual agreement? (y/n): ").lower()
    if confirm == 'y':
        chess.end_game_by_agreement()
        print("The game has ended by mutual agreement.")
        return True
    return False

def display_game_result(chess):
    print("The game has ended!")
    if chess.__mutual_agreement_to_end__:
        print("The game ended by mutual agreement.")
    elif chess.__board__.__king_captured__:
        print("The king has been captured.")
    else:
        captures = chess.get_captures()
        winner = "WHITE" if captures['__white_captures__'] == 15 else "BLACK"
        print(f"{winner} has won by capturing all opponent's pieces.")

def main():
    chess = Chess()
    while not chess.is_over():
        display_game_status(chess)
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            handle_move(chess)
        elif choice == '2':
            handle_view_score(chess)
        elif choice == '3':
            if handle_end_game_agreement(chess):
                break
        elif choice == '4':
            print("Quitting the game.")
            return
        else:
            print("Invalid choice. Please try again.")

    if chess.is_over():
        display_game_result(chess)

if __name__ == "__main__":
    main()