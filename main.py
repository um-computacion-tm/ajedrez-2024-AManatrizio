from game.chess import Chess

def display_menu():
    print("\nMenu:")
    print("1. Make a move")
    print("2. End game by mutual agreement")
    print("3. Quit")

def main():
    chess = Chess()
    while not chess.is_over():
        chess.display_board()
        chess.get_captures()
        print(f"\nTurn of: {chess.current_player}")
        
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("To move a piece, type the row number followed by \nthe column number without any spaces. For example: 62")
            piece = input("Enter your piece to move: ")
            move = input("Enter where to move: ")
            if not chess.play_move(piece, move):
                print("Invalid move! Try again.")
        elif choice == '2':
            confirm = input("Are you sure you want to end the game by mutual agreement? (y/n): ").lower()
            if confirm == 'y':
                chess.end_game_by_agreement()
                print("The game has ended by mutual agreement.")
                break
        elif choice == '3':
            print("Quitting the game.")
            return
        else:
            print("Invalid choice. Please try again.")

    if chess.is_over():
        print("The game has ended!")
        if chess.mutual_agreement_to_end:
            print("The game ended by mutual agreement.")
        elif chess.board.king_captured:
            print("The king has been captured.")
        else:
            winner = "WHITE" if chess.board.black_captures == 15 else "BLACK"
            print(f"{winner} has won by capturing all opponent's pieces.")



if __name__ == "__main__":
    main()