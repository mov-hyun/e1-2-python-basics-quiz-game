import json
import random
from datetime import datetime
from pathlib import Path

from src.quiz import Quiz


DEFAULT_QUIZ_DATA = [
    {
        "question": "Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?",
        "choices": ["func", "define", "def", "function"],
        "answer": 3,
        "hint": "함수를 만들 때 가장 자주 보는 세 글자 키워드입니다.",
    },
    {
        "question": "함수 안에서 값을 호출한 곳으로 돌려줄 때 사용하는 키워드는 무엇인가요?",
        "choices": ["print", "break", "return", "yield"],
        "answer": 3,
        "hint": "함수의 실행 결과를 바깥으로 보내는 역할을 합니다.",
    },
    {
        "question": "다음 중 Python 함수 호출 예시로 올바른 것은 무엇인가요?",
        "choices": ["my_func[]", "my_func()", "call my_func()", "function my_func()"],
        "answer": 2,
        "hint": "함수를 사용할 때는 이름 뒤에 소괄호를 붙입니다.",
    },
    {
        "question": "함수 정의에서 괄호 안에 적는 값들의 이름은 무엇인가요?",
        "choices": ["매개변수", "반환값", "반복문", "조건문"],
        "answer": 1,
        "hint": "함수에 전달되는 입력값의 이름을 가리키는 말입니다.",
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
        "hint": "같은 작업을 여러 번 써야 할 때 도움이 되는 특징입니다.",
    },
]


class QuizGame:
    def __init__(self, state_file="state.json"):
        self.state_file = Path(state_file)
        self.quizzes = []
        self.best_score = 0
        self.rankings = []
        self.history = []

    # 저장/복구 로직은 별도 메서드로 분리해 state.json 관리 책임을 모은다.
    def load_state(self):
        if not self.state_file.exists():
            self.quizzes = self._build_default_quizzes()
            self.best_score = 0
            self.rankings = []
            self.history = []
            return

        try:
            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError):
            print("⚠️ state.json 파일을 읽을 수 없어 기본 데이터로 시작합니다.")
            self.quizzes = self._build_default_quizzes()
            self.best_score = 0
            self.rankings = []
            self.history = []
            return

        if not isinstance(data, dict):
            print("⚠️ state.json 구조가 올바르지 않아 기본 데이터로 시작합니다.")
            self.quizzes = self._build_default_quizzes()
            self.best_score = 0
            self.rankings = []
            self.history = []
            return

        self.quizzes = self._load_quizzes(data.get("quizzes", []))
        if not self.quizzes:
            print("⚠️ 유효한 퀴즈 데이터가 없어 기본 퀴즈로 복구합니다.")
            self.quizzes = self._build_default_quizzes()

        self.rankings = self._load_rankings(data.get("rankings", []))
        self.history = self._load_history(data.get("history", []))
        if self.rankings:
            self.best_score = self.rankings[0]["score"]
        else:
            self.best_score = self._load_best_score(data.get("best_score", 0))

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "rankings": self.rankings,
            "history": self.history,
        }
        try:
            with self.state_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️ state.json 파일 저장에 실패했습니다.")

    def show_menu(self):
        print("=" * 40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")
        print("=" * 40)

    # 메뉴 입력, 정답 입력, 퀴즈 추가 입력에서 같은 검증 로직을 재사용한다.
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
            6,
            "⚠️ 잘못된 입력입니다. 1-6 사이의 숫자를 입력하세요.",
            return_on_interrupt=6,
        )

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.play_quiz()
        elif choice == 2:
            self.add_quiz()
        elif choice == 3:
            self.show_quiz_list()
        elif choice == 4:
            self.show_score()
        elif choice == 5:
            self.delete_quiz()
        elif choice == 6:
            self.save_state()
            print("프로그램을 종료합니다.")
            return False

        return True

    # 퀴즈 진행, 힌트 사용, 점수 계산은 play_quiz에서 한 흐름으로 관리한다.
    def play_quiz(self):
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        selected_question_count = self._read_int(
            f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ",
            1,
            len(self.quizzes),
            f"⚠️ 잘못된 입력입니다. 1-{len(self.quizzes)} 사이의 숫자를 입력하세요.",
        )

        quiz_order = self.quizzes[:]
        random.shuffle(quiz_order)
        quiz_order = quiz_order[:selected_question_count]

        total_questions = len(quiz_order)
        correct_count = 0
        total_score = 0.0
        remaining_hints = 3

        print(f"📝 퀴즈를 시작합니다! (총 {total_questions}문제)")
        print(f"💡 이번 게임에서 사용할 수 있는 힌트는 총 {remaining_hints}회입니다.")
        print()

        for index, quiz in enumerate(quiz_order, start=1):
            print("-" * 40)
            print(f"[문제 {index}]")
            quiz.display()
            print()
            hint_used_for_question = False

            while True:
                print(f"남은 힌트: {remaining_hints}회")
                user_answer = self._read_int(
                    "정답 입력 (0: 힌트 보기, 1-4: 답안): ",
                    0,
                    4,
                    "⚠️ 잘못된 입력입니다. 0-4 사이의 숫자를 입력하세요.",
                )

                if user_answer is None:
                    print("퀴즈 진행을 중단하고 메뉴로 돌아갑니다.")
                    return

                if user_answer != 0:
                    break

                if hint_used_for_question:
                    print("⚠️ 이 문제의 힌트는 이미 확인했습니다.")
                    print()
                    continue

                if remaining_hints <= 0:
                    print("⚠️ 사용할 수 있는 힌트가 없습니다.")
                    print()
                    continue

                if not quiz.hint:
                    print("⚠️ 이 문제에는 힌트가 없습니다.")
                    print()
                    continue

                remaining_hints -= 1
                hint_used_for_question = True
                print(f"💡 힌트: {quiz.hint}")
                print()


            if quiz.is_correct(user_answer):
                correct_count += 1
                if hint_used_for_question:
                    total_score += 0.5
                else:
                    total_score += 1.0
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

            print()

        nickname = self._read_text(
            "닉네임을 입력하세요: ",
            "⚠️ 닉네임은 비워둘 수 없습니다. 다시 입력하세요.",
            return_on_interrupt="익명",
        )
        if nickname == "익명":
            print("닉네임 입력이 중단되어 '익명'으로 저장합니다.")

        ranking_added, is_new_best = self._update_rankings(nickname, total_score)
        self._append_history(
            nickname=nickname,
            total_questions=total_questions,
            correct_count=correct_count,
            score=total_score,
        )
        self.save_state()

        print("=" * 40)
        print(
            f"🏆 결과: {total_questions}문제 중 {correct_count}문제 정답! "
            f"(총점 {total_score:.1f}점)"
        )
        if is_new_best:
            print("🎉 새로운 최고 점수입니다!")
        elif ranking_added:
            print("랭킹이 갱신되었습니다.")
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

        hint = self._read_text(
            "힌트를 입력하세요: ",
            "⚠️ 힌트는 비워둘 수 없습니다. 다시 입력하세요.",
        )

        new_quiz = Quiz(question, choices, answer, hint)
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

    def show_score(self):
        if not self.rankings and not self.history:
            print("📊 아직 점수 기록이 없습니다.")
            return

        print(f"🏆 현재 최고 점수: {self.best_score:.1f}점")

        if self.history:
            sorted_history = sorted(
                self.history,
                key=lambda record: (record["score"], record["played_at"]),
                reverse=True,
            )

            print("🏆 퀴즈 랭킹")
            print("-" * 40)
            for index, record in enumerate(sorted_history, start=1):
                print(
                    f"{index}. {record['nickname']} | {record['score']:.1f}점 | "
                    f"{record['correct_count']}/{record['total_questions']} | "
                    f"{record['played_at']}"
                )
            print("-" * 40)
        else:
            print("📊 플레이 히스토리 기록은 아직 없습니다.")

    def delete_quiz(self):
        if not self.quizzes:
            print("📭 삭제할 퀴즈가 없습니다.")
            return

        print("🗑️ 삭제할 퀴즈를 선택하세요.")
        print("-" * 40)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("-" * 40)

        quiz_number = self._read_int(
            "삭제할 퀴즈 번호를 입력하세요: ",
            1,
            len(self.quizzes),
            f"⚠️ 잘못된 입력입니다. 1-{len(self.quizzes)} 사이의 숫자를 입력하세요.",
        )

        selected_quiz = self.quizzes[quiz_number - 1]
        if self._is_default_quiz(selected_quiz):
            print("⚠️ 기본 퀴즈는 삭제할 수 없습니다.")
            return

        print()
        print(f"선택한 퀴즈: {selected_quiz.question}")
        print("1. 삭제")
        print("2. 취소")

        confirm = self._read_int(
            "선택: ",
            1,
            2,
            "⚠️ 잘못된 입력입니다. 1-2 사이의 숫자를 입력하세요.",
            return_on_interrupt=2,
        )

        if confirm == 2:
            print("퀴즈 삭제를 취소했습니다.")
            return

        deleted_quiz = self.quizzes.pop(quiz_number - 1)
        self.save_state()
        print(f"✅ '{deleted_quiz.question}' 퀴즈가 삭제되었습니다.")

    def run(self):
        should_continue = True

        while should_continue:
            self.show_menu()
            choice = self.get_menu_choice()
            should_continue = self.handle_menu_choice(choice)
            print()

    def _build_default_quizzes(self):
        return [Quiz.from_dict(item) for item in DEFAULT_QUIZ_DATA]

    def _is_default_quiz(self, quiz):
        for default_quiz in DEFAULT_QUIZ_DATA:
            if quiz.to_dict() == default_quiz:
                return True
        return False

    def _load_quizzes(self, quiz_data):
        quizzes = []

        if not isinstance(quiz_data, list):
            return quizzes

        for item in quiz_data:
            try:
                quizzes.append(Quiz.from_dict(item))
            except (KeyError, TypeError, ValueError):
                continue

        return quizzes

    def _load_best_score(self, best_score_data):
        if not isinstance(best_score_data, (int, float)) or best_score_data < 0:
            return 0
        return float(best_score_data)

    def _load_rankings(self, ranking_data):
        rankings = []

        if not isinstance(ranking_data, list):
            return rankings

        for item in ranking_data:
            if not isinstance(item, dict):
                continue

            nickname = item.get("nickname")
            score = item.get("score")

            if not isinstance(nickname, str) or not nickname.strip():
                continue
            if not isinstance(score, (int, float)) or score < 0:
                continue

            rankings.append(
                {
                    "nickname": nickname.strip(),
                    "score": float(score),
                }
            )

        rankings.sort(key=lambda item: item["score"], reverse=True)
        return rankings

    def _load_history(self, history_data):
        history = []

        if not isinstance(history_data, list):
            return history

        for item in history_data:
            if not isinstance(item, dict):
                continue

            nickname = item.get("nickname")
            played_at = item.get("played_at")
            total_questions = item.get("total_questions")
            correct_count = item.get("correct_count")
            score = item.get("score")

            if not isinstance(nickname, str) or not nickname.strip():
                continue
            if not isinstance(played_at, str) or not played_at.strip():
                continue
            if not isinstance(total_questions, int) or total_questions < 0:
                continue
            if not isinstance(correct_count, int) or correct_count < 0:
                continue
            if correct_count > total_questions:
                continue
            if not isinstance(score, (int, float)) or score < 0:
                continue

            history.append(
                {
                    "nickname": nickname.strip(),
                    "played_at": played_at.strip(),
                    "total_questions": total_questions,
                    "correct_count": correct_count,
                    "score": float(score),
                }
            )

        return history

    def _update_rankings(self, nickname, score):
        new_entry = {
            "nickname": nickname,
            "score": score,
        }
        previous_top_score = self.best_score

        self.rankings.append(new_entry)
        self.rankings.sort(key=lambda item: item["score"], reverse=True)
        ranking_added = any(item is new_entry for item in self.rankings)

        if self.rankings:
            self.best_score = self.rankings[0]["score"]
        else:
            self.best_score = 0

        is_new_best = ranking_added and score > previous_top_score
        return ranking_added, is_new_best

    def _append_history(self, nickname, total_questions, correct_count, score):
        self.history.append(
            {
                "nickname": nickname,
                "played_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_questions": total_questions,
                "correct_count": correct_count,
                "score": score,
            }
        )
