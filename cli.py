from game.chess import Chess

class Cli:
    def __init__(self):
        self.chess = Chess()

    def run(self):
        while not self.chess.is_over():
            self.display_game_status()
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.handle_move()
            elif choice == '2':
                self.handle_view_score()
            elif choice == '3':
                if self.handle_end_game_agreement():
                    break
            elif choice == '4':
                print("Quitting the game.")
                return
            else:
                print("Invalid choice. Please try again.")

        if self.chess.is_over():
            self.display_game_result()

    def display_menu(self):
        print("\nMenu:")
        print("1. Make a move")
        print("2. View score (captures)")
        print("3. End game by mutual agreement")
        print("4. Quit")

    def display_game_status(self):
        self.chess.display_board()
        self.chess.get_captures()
        print(f"\nTurn of: {self.chess.__current_player__}")

    def handle_move(self):
        while True:
            try:
                print("To move a piece, type the row number followed by \nthe column number without any spaces. For example: 62")
                piece = input("Enter your piece to move: ")
                move = input("Enter where to move: ")
                result = self.chess.play_move(piece, move)
                
                if isinstance(result, tuple):
                    result, info = result
                else:
                    info = None

                if self.process_move_result(result, info):
                    return
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")

    def process_move_result(self, result, info):
        if result == "INVALID_TURN":
            print("It's not your turn!")
        elif result == "INVALID_CAPTURE":
            print("You can't capture your own piece!")
        elif result == "INVALID":
            print("Invalid move! Try again.")
        elif result == "KING_CAPTURED":
            self.handle_king_capture(info)
            return True
        elif result == "PROMOTION_NEEDED":
            self.handle_pawn_promotion(info)
            self.display_game_status()
            return True
        elif result == "VALID":
            print("Move successful!")
            return True
        else:
            print("Unexpected result. Please try again.")
        return False

    def handle_king_capture(self, captured_color):
        winning_color = "White" if captured_color == "BLACK" else "Black"
        print(f"The {winning_color} player has captured the king!")
        print(f"{winning_color} wins!")

    def handle_pawn_promotion(self, info):
        fila, columna = info
        print("Pawn promotion! Choose a piece to promote to:")
        print("1. Queen")
        print("2. Rook")
        print("3. Bishop")
        print("4. Knight")
        choice = input("Enter your choice (1-4): ")
        promoted_piece = self.chess.promote_pawn(fila, columna, choice)
        print(f"Pawn promoted to {promoted_piece}")

    def handle_view_score(self):
        captures = self.chess.get_captures()
        print(f"\nWhite captures: {captures['__white_captures__']}")
        print(f"\nBlack captures: {captures['__black_captures__']}")

    def handle_end_game_agreement(self):
        confirm = input("Are you sure you want to end the game by mutual agreement? (y/n): ").lower()
        if confirm == 'y':
            self.chess.end_game_by_agreement()
            print("The game has ended by mutual agreement.")
            return True
        return False

    def display_game_result(self):
        print("The game has ended!")
        if self.chess.__mutual_agreement_to_end__:
            print("The game ended by mutual agreement.")
        elif self.chess.__board__.__king_captured__:
            print("The king has been captured.")
        else:
            captures = self.chess.get_captures()
            winner = "WHITE" if captures['__white_captures__'] == 15 else "BLACK"
            print(f"{winner} has won by capturing all opponent's pieces.")
