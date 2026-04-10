from quiz_game import QuizGame


def main():
    game = QuizGame()
    game.load_state()
    game.run()
    return game


if __name__ == "__main__":
    main()
