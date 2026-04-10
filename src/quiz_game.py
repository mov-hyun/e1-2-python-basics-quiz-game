import json
from pathlib import Path

from quiz import Quiz


DEFAULT_QUIZ_DATA = [
    {
        "question": "Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?",
        "choices": ["func", "define", "def", "function"],
        "answer": 3,
    },
    {
        "question": "함수 안에서 값을 호출한 곳으로 돌려줄 때 사용하는 키워드는 무엇인가요?",
        "choices": ["print", "break", "return", "yield"],
        "answer": 3,
    },
    {
        "question": "다음 중 Python 함수 호출 예시로 올바른 것은 무엇인가요?",
        "choices": ["my_func[]", "my_func()", "call my_func()", "function my_func()"],
        "answer": 2,
    },
    {
        "question": "함수 정의에서 괄호 안에 적는 값들의 이름은 무엇인가요?",
        "choices": ["매개변수", "반환값", "반복문", "조건문"],
        "answer": 1,
    },
    {
        "question": "다음 중 함수의 장점으로 가장 알맞은 것은 무엇인가요?",
        "choices": [
            "코드를 반복해서 새로 작성해야 한다",
            "코드 재사용이 쉬워진다",
            "오류가 절대 발생하지 않는다",
            "변수를 사용할 수 없게 된다",
        ],
        "answer": 2,
    },
]


class QuizGame:
    def __init__(self, state_file="state.json"):
        self.state_file = Path(state_file)
        self.quizzes = []
        self.best_score = 0

    def load_state(self):
        if not self.state_file.exists():
            self.quizzes = self._build_default_quizzes()
            self.best_score = 0
            return

        try:
            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError):
            self.quizzes = self._build_default_quizzes()
            self.best_score = 0
            return

        quiz_data = data.get("quizzes", [])
        self.quizzes = [Quiz.from_dict(item) for item in quiz_data]
        self.best_score = data.get("best_score", 0)

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        with self.state_file.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def show_menu(self):
        print("=" * 40)
        print("        나만의 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_menu_choice(self):
        while True:
            try:
                raw_value = input("선택: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n프로그램을 안전하게 종료합니다.")
                self.save_state()
                return 5

            if not raw_value:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue

            try:
                choice = int(raw_value)
            except ValueError:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue

            if choice not in range(1, 6):
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue

            return choice

    def handle_menu_choice(self, choice):
        if choice == 1:
            print("퀴즈 풀기 기능은 다음 단계에서 구현합니다.")
        elif choice == 2:
            print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")
        elif choice == 3:
            print("퀴즈 목록 기능은 다음 단계에서 구현합니다.")
        elif choice == 4:
            print("점수 확인 기능은 다음 단계에서 구현합니다.")
        elif choice == 5:
            self.save_state()
            print("프로그램을 종료합니다.")
            return False

        return True

    def run(self):
        should_continue = True

        while should_continue:
            self.show_menu()
            choice = self.get_menu_choice()
            should_continue = self.handle_menu_choice(choice)
            print()

    def _build_default_quizzes(self):
        return [Quiz.from_dict(item) for item in DEFAULT_QUIZ_DATA]
