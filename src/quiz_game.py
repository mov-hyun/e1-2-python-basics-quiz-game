import json
from pathlib import Path

from src.quiz import Quiz


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
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def _read_text(self, prompt, empty_message, return_on_interrupt=None):
        while True:
            try:
                raw_value = input(prompt)
            except (EOFError, KeyboardInterrupt):
                print("\n입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
                self.save_state()
                return return_on_interrupt

            raw_value = raw_value.strip()
            if not raw_value:
                print(empty_message)
                continue

            return raw_value

    def _read_int(self, prompt, min_value, max_value, error_message, return_on_interrupt=None):
        while True:
            raw_value = self._read_text(prompt, error_message, return_on_interrupt)
            if raw_value == return_on_interrupt:
                return return_on_interrupt

            try:
                value = int(raw_value)
            except ValueError:
                print(error_message)
                continue

            if value < min_value or value > max_value:
                print(error_message)
                continue

            return value

    def get_menu_choice(self):
        return self._read_int(
            "선택: ",
            1,
            5,
            "⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.",
            return_on_interrupt=5,
        )

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.play_quiz()
        elif choice == 2:
            self.add_quiz()
        elif choice == 3:
            self.show_quiz_list()
        elif choice == 4:
            print("점수 확인 기능은 다음 단계에서 구현합니다.")
        elif choice == 5:
            self.save_state()
            print("프로그램을 종료합니다.")
            return False

        return True

    def play_quiz(self):
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        total_questions = len(self.quizzes)
        correct_count = 0

        print(f"📝 퀴즈를 시작합니다! (총 {total_questions}문제)")
        print()

        for index, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            print(f"[문제 {index}]")
            quiz.display()
            print()

            user_answer = self._read_int(
                "정답 입력 (1-4): ",
                1,
                4,
                "⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.",
            )

            if user_answer is None:
                print("퀴즈 진행을 중단하고 메뉴로 돌아갑니다.")
                return

            if quiz.is_correct(user_answer):
                correct_count += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

            print()

        print("=" * 40)
        print(f"🏆 결과: {total_questions}문제 중 {correct_count}문제 정답!")
        print("=" * 40)

    def add_quiz(self):
        print("📌 새로운 퀴즈를 추가합니다.")
        print()

        question = self._read_text(
            "문제를 입력하세요: ",
            "⚠️ 문제는 비워둘 수 없습니다. 다시 입력하세요.",
        )

        choices = []
        for index in range(1, 5):
            choice = self._read_text(
                f"선택지 {index}: ",
                f"⚠️ 선택지 {index}은(는) 비워둘 수 없습니다. 다시 입력하세요.",
            )
            choices.append(choice)

        answer = self._read_int(
            "정답 번호 (1-4): ",
            1,
            4,
            "⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.",
        )

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print()
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        self._print_quiz_list(show_answers=False)
        print("1. 정답도 함께 보기")
        print("2. 나가기")

        choice = self._read_int(
            "선택: ",
            1,
            2,
            "⚠️ 잘못된 입력입니다. 1-2 사이의 숫자를 입력하세요.",
            return_on_interrupt=2,
        )

        if choice == 1:
            print()
            self._print_quiz_list(show_answers=True)

    def _print_quiz_list(self, show_answers):
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
            if show_answers:
                answer_text = quiz.choices[quiz.answer - 1]
                print(f"정답: {quiz.answer}번 - {answer_text}")
                print()

        print("-" * 40)

    def run(self):
        should_continue = True

        while should_continue:
            self.show_menu()
            choice = self.get_menu_choice()
            should_continue = self.handle_menu_choice(choice)
            print()

    def _build_default_quizzes(self):
        return [Quiz.from_dict(item) for item in DEFAULT_QUIZ_DATA]
