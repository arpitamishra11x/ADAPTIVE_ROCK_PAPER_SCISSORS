import random
from collections import Counter
from typing import Dict

# ----------------- Constants -----------------
MOVES = ["rock", "paper", "scissors"]
WIN_MAP = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


class AdaptiveRPS:
    """
    Adaptive Rock Paper Scissors AI.
    Predicts player moves based on history
    and counters the most frequent choice.
    """

    def __init__(self):
        self.player_history = []
        self.move_counter = Counter()

    def predict_player_move(self) -> str:
        """Predict the player's next move."""
        if len(self.player_history) < 3:
            return random.choice(MOVES)

        return self.move_counter.most_common(1)[0][0]

    def counter_move(self, predicted_move: str) -> str:
        """Return the move that beats the predicted move."""
        for move, beats in WIN_MAP.items():
            if beats == predicted_move:
                return move

    def get_computer_move(self) -> str:
        predicted = self.predict_player_move()
        return self.counter_move(predicted)

    def update_history(self, player_move: str) -> None:
        self.player_history.append(player_move)
        self.move_counter[player_move] += 1

    def determine_winner(self, player: str, computer: str) -> str:
        if player == computer:
            return "draw"
        elif WIN_MAP[player] == computer:
            return "player"
        return "computer"


def main():
    game = AdaptiveRPS()
    score: Dict[str, int] = {"player": 0, "computer": 0, "draw": 0}
    round_number = 1

    print("🎮 Adaptive Rock Paper Scissors")
    print("Type 'exit' to quit\n")

    while True:
        print(f"--- Round {round_number} ---")
        player_move = input("Choose rock / paper / scissors: ").strip().lower()

        if player_move == "exit":
            break

        if player_move not in MOVES:
            print("❌ Invalid move. Please try again.\n")
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

        print(
            f"📊 Score → You: {score['player']} | "
            f"Computer: {score['computer']} | "
            f"Draws: {score['draw']}\n"
        )

        round_number += 1

    print("\n🏁 Final Score:")
    print(score)
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()
