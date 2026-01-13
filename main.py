import random
from collections import Counter

MOVES = ["rock", "paper", "scissors"]
WIN_MAP = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

class AdaptiveRPS:
    def __init__(self):
        self.player_history = []
        self.move_counter = Counter()

    def predict_player_move(self):
        if not self.player_history:
            return random.choice(MOVES)

        most_common_move = self.move_counter.most_common(1)[0][0]
        return most_common_move

    def counter_move(self, predicted_move):
        for move, beats in WIN_MAP.items():
            if beats == predicted_move:
                return move

    def get_computer_move(self):
        predicted = self.predict_player_move()
        return self.counter_move(predicted)

    def update_history(self, player_move):
        self.player_history.append(player_move)
        self.move_counter[player_move] += 1

    def determine_winner(self, player, computer):
        if player == computer:
            return "draw"
        elif WIN_MAP[player] == computer:
            return "player"
        else:
            return "computer"


def main():
    game = AdaptiveRPS()
    score = {"player": 0, "computer": 0, "draw": 0}

    print("🎮 Adaptive Rock Paper Scissors")
    print("Type 'exit' to quit\n")

    while True:
        player_move = input("Choose rock / paper / scissors: ").lower()

        if player_move == "exit":
            break

        if player_move not in MOVES:
            print("❌ Invalid move. Try again.\n")
            continue

        computer_move = game.get_computer_move()
        game.update_history(player_move)

        result = game.determine_winner(player_move, computer_move)
        score[result] += 1

        print(f"🧠 Computer chose: {computer_move}")
        if result == "draw":
            print("⚖️ It's a draw!")
        elif result == "player":
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

        print(f"📊 Score → You: {score['player']} | Computer: {score['computer']} | Draws: {score['draw']}\n")

    print("\nFinal Score:")
    print(score)
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()
