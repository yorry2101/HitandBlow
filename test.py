# game managerの検証
from game_manager import GameManager
def test_make_guess(player_guess):
    answer = GameManager.generate_answer()
    game_manager = GameManager(answer)

    print(f"Testing with answer: {answer} and player guess: {player_guess}")

    hit, blow = game_manager.make_guess(player_guess)
    print(f"Hit = {hit}, Blow = {blow}")

    print("end of test_make_guess\n")

def main():
    player_guess = GameManager.generate_answer()
    test_make_guess(player_guess)

if __name__ == "__main__":
    main()