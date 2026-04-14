# E1-2. Git과 함께하는 Python 첫 발자국
---
## 1.프로젝트 개요

- Python 기반 CLI 퀴즈 게임 구현     
- 객체지향 설계       
- JSON 기반 데이터 파일 사용       
- Git을 활용한 프로젝트 관리       

[1. 프로젝트 개요](#1-프로젝트-개요)   
[2. Git 명령어 정리](#2-git-명령어-정리)   
[3. Python 기본 정리](#3-python-기본-정리)   
[4. 퀴즈 주제와 선정 이유](#4-퀴즈-주제와-선정-이유)   
[5. 실행 방법](#5-실행-방법)   
[6. 기능 목록](#6-기능-목록)   
[7. 파일 구조](#7-파일-구조)   
[8. 데이터 파일 설명](#8-데이터-파일-설명)   
[9. 퀴즈 보너스 기능](#9-퀴즈-보너스-기능)   
[10. 브랜치 병합](#10-브랜치-병합)   
[11. 트러블 슈팅](#11-트러블-슈팅)   

### 프로젝트 구조

```text
e1-2-python-basics-quiz-game/
├── .gitignore
├── README.md
├── main.py
├── state.json
└── src/
    ├── quiz.py
    └── quiz_game.py
```

### 수행항목 체크리스트

- [x] 프로젝트 개요
- [x] Git 명령어 정리
- [x] 퀴즈 주제와 선정 이유
- [x] 실행 방법
- [x] 기능 목록
- [x] 파일 구조
- [x] 데이터 파일 설명
- [x] 퀴즈 보너스 기능
- [x] Python 기본 정리
- [x] 브랜치 병합
- [x] 트러블 슈팅

## 2. Git 명령어 정리

이 프로젝트에서는 Git을 사용해 작업 내용을 기록하고, 기능 단위로 개발 과정을 관리했습니다.  
아래는 이번 과제에서 사용한 핵심 Git 명령어 정리입니다.

| 명령어 | 설명 | 예시 |
| --- | --- | --- |
| `git init` | 로컬 디렉터리를 Git 저장소로 초기화 | `git init` |
| `git add` | 커밋할 파일을 스테이징 영역에 추가 | `git add .` |
| `git commit` | 변경 이력을 저장 | `git commit -m "Feat: 메인 메뉴 기능 구현"` |
| `git push` | 로컬 커밋을 원격 저장소에 업로드 | `git push origin main` |
| `git pull` | 원격 저장소의 최신 변경사항을 가져와 반영 | `git pull origin main` |
| `git branch` | 현재 브랜치 목록 확인 | `git branch` |
| `git branch 브랜치명` | 새 브랜치 생성 | `git branch feature/hint` |
| `git checkout -b` | 새 브랜치를 만들고 바로 이동 | `git checkout -b play-quiz` |
| `git checkout` | 브랜치 이동 | `git checkout play-quiz` |
| `git merge` | 다른 브랜치의 작업 내용을 현재 브랜치에 병합 | `git merge feature/hint` |
| `git merge --no-ff` | merge commit을 남기면서 병합 | `git merge --no-ff feature/hint` |
| `git push origin 브랜치명` | 현재 브랜치를 원격 저장소에 업로드 | `git push origin feature/hint` |
| `git log --oneline --graph --decorate --all` | 브랜치 생성과 병합 흐름을 그래프로 확인 | `git log --oneline --graph --decorate --all` |
| `git clone` | 원격 저장소를 로컬로 복제 | `git clone <저장소_URL>` |

이번 과제에서는 위 명령어들을 사용해 초기 설정, 기능별 커밋, 브랜치 작업, 병합, 원격 저장소 업로드, clone/pull 실습을 진행했습니다.

### 2.1 Git clone / pull 실습

과제 요구사항에 맞게 저장소를 별도 폴더로 복제한 뒤, 복제본에서 README를 수정하고 push한 다음 원래 작업 폴더에서 pull로 변경 사항을 가져오는 과정을 실습했습니다.

```bash
# 저장소를 새로운 로컬 디렉터리로 복제
east1111@1234 e1-2-python-basics-quiz-game % cd ..
east1111@1234 ~ % git clone https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git e1-2-python-basics-quiz-game-copy
Cloning into 'e1-2-python-basics-quiz-game-copy'...
remote: Enumerating objects: 129, done.
remote: Counting objects: 100% (129/129), done.
remote: Compressing objects: 100% (87/87), done.
remote: Total 129 (delta 63), reused 104 (delta 41), pack-reused 0 (from 0)
Receiving objects: 100% (129/129), 44.04 KiB | 2.45 MiB/s, done.
Resolving deltas: 100% (63/63), done.

# 복제본 폴더로 이동 후 현재 브랜치 확인
east1111@1234 ~ % cd e1-2-python-basics-quiz-game-copy
east1111@1234 e1-2-python-basics-quiz-game-copy % git branch
* main

# 복제본에서 README 수정 내용을 커밋하고 원격 저장소에 push
east1111@1234 e1-2-python-basics-quiz-game-copy % git add README.md
east1111@1234 e1-2-python-basics-quiz-game-copy % git commit -m "Docs: clone pull 실습용 README 문구 추가"
east1111@1234 e1-2-python-basics-quiz-game-copy % git push origin main

[main *****] Docs: clone pull 실습용 README 문구 추가
 1 file changed, 2 insertions(+)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 369 bytes | 369.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
   *****..*****  main -> main

# 원래 작업 폴더에서 최신 변경 사항 pull
east1111@1234 e1-2-python-basics-quiz-game % git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 349 bytes | 116.00 KiB/s, done.
From https://github.com/mov-hyun/e1-2-python-basics-quiz-game
 * branch            main       -> FETCH_HEAD
   *****..*****  main       -> origin/main
Updating *****..*****
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```
## 3. Python 기본 정리

이 프로젝트를 만들면서 사용한 Python 기본 개념은 아래와 같습니다.

### 3.1 변수

변수는 값을 저장하고 다시 사용하기 위한 이름표입니다.  
프로그램에서는 메뉴 선택, 정답 수, 점수, 남은 힌트 횟수 같은 값을 변수에 저장해 사용했습니다.

### 3.2 자료형

이 프로젝트에서 사용한 대표적인 자료형은 다음과 같습니다.

- `int`: 메뉴 번호, 정답 번호, 문제 개수
- `float`: 힌트 사용 시 반영되는 `0.5점` 같은 점수
- `str`: 문제, 선택지, 닉네임, 힌트 문구
- `bool`: 정답 여부, 힌트 사용 여부 같은 참/거짓 값
- `list`: 퀴즈 목록, 선택지 목록, 랭킹 목록
- `dict`: JSON 데이터 구조 표현

### 3.3 조건문

`if`, `elif`, `else`를 사용해 상황에 따라 다른 동작을 처리했습니다.  
예를 들어 메뉴 선택에 따라 다른 기능을 실행하고, 정답/오답 여부와 입력값의 유효성을 구분했습니다.

### 3.4 반복문

프로젝트에서는 `while`과 `for`를 모두 사용했습니다.

- `while`
  - 올바른 입력이 들어올 때까지 다시 입력받기
  - 게임 메뉴를 반복해서 보여주기
- `for`
  - 퀴즈와 선택지를 순서대로 처리하기
  - 랭킹 목록을 출력하기

### 3.5 함수와 메서드

함수와 메서드는 기능을 역할별로 나누기 위해 사용했습니다.  
이 프로젝트에서는 입력 처리, 게임 진행, 저장/복구 로직을 각각 다른 메서드로 분리해 한 메서드가 한 가지 책임에 집중하도록 구성했습니다.

예를 들어 `_read_text()`와 `_read_int()`는 메뉴 입력, 정답 입력, 퀴즈 추가 입력에서 공통으로 재사용되고,  
`play_quiz()`는 문제 출제와 점수 계산, `add_quiz()`는 새 퀴즈 등록, `load_state()`와 `save_state()`는 파일 저장/불러오기를 담당합니다.

이처럼 기능별로 메서드를 나누면 코드 흐름을 이해하기 쉬워지고,  
입력 검증 같은 공통 로직을 한 곳에서 관리할 수 있어 수정이나 확장도 더 쉬워집니다.

### 3.6 클래스와 객체

클래스는 관련 있는 데이터와 기능을 하나로 묶는 도구입니다.  
`__init__` 메서드는 객체가 생성될 때 초기값을 넣는 역할을 하고, `self`는 현재 객체 자신을 가리킵니다.  
이 프로젝트에서는 퀴즈 한 개를 표현하는 `Quiz` 클래스와 게임 전체를 관리하는 `QuizGame` 클래스를 나누어 사용했습니다.

`Quiz` 클래스는 문제, 선택지, 정답, 힌트처럼 하나의 퀴즈에 필요한 데이터와  
문제 출력, 정답 확인 같은 동작을 함께 묶어 관리합니다.  
`QuizGame` 클래스는 퀴즈 목록, 점수, 랭킹, 히스토리, 파일 저장 경로 같은 상태를 가지고  
메뉴 출력, 퀴즈 진행, 점수 확인, 저장/복구 같은 전체 흐름을 담당합니다.

만약 이 프로젝트를 함수만으로 구현했다면 문제 데이터와 게임 상태를 여러 함수에 따로 전달해야 해서  
코드가 더 복잡해지고 관련된 데이터가 흩어지기 쉬웠을 것입니다.  
반면 클래스를 사용하면 관련 데이터와 동작을 한 객체 안에 묶을 수 있어  
코드의 의미가 더 분명해지고 기능을 추가하거나 수정할 때도 관리하기 쉬워집니다.

### 3.7 파일 입출력과 JSON

프로그램을 종료해도 데이터가 유지되도록 JSON 파일을 사용했습니다.  
JSON은 Python의 `dict`, `list`, `str`, `int`, `float` 같은 자료형과 자연스럽게 연결되기 때문에 저장 형식으로 사용하기 좋습니다.

### 3.8 예외 처리

`try/except`를 사용해 프로그램이 갑자기 종료되지 않도록 처리했습니다.  
숫자 변환 실패, 입력 중단, 파일 읽기/쓰기 실패, JSON 손상 같은 상황을 예외 처리로 대응했습니다.

## 4. 퀴즈 주제와 선정 이유

퀴즈 주제는 "Python 기초 문법"입니다.

선정 이유는 다음과 같습니다.
- 개발 입문 과정에서 가장 기본이 되는 내용
- 이참에 공부해두면 좋음


## 5. 실행 방법

프로젝트 루트 디렉터리에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

Python 3.10 이상 환경에서 실행하는 것을 권장합니다.

### 실행 화면
```bash
eastsae7567@c4r1s6 e1-2-python-basics-quiz-game % python3 main.py
========================================
        🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 퀴즈 삭제
6. 종료
========================================
선택: 
```

## 6. 기능 목록

### 6.1 `퀴즈 풀기`
저장된 퀴즈를 랜덤 순서로 출제합니다.
정답 입력, 오답 안내, 결과 요약을 제공합니다.
```bash
몇 문제를 풀까요? (1-5): 5
📝 퀴즈를 시작합니다! (총 5문제)
💡 이번 게임에서 사용할 수 있는 힌트는 총 3회입니다.

----------------------------------------
[문제 1]
다음 중 함수의 장점으로 가장 알맞은 것은 무엇인가요?
1. 코드를 반복해서 새로 작성해야 한다
2. 코드 재사용이 쉬워진다
3. 오류가 절대 발생하지 않는다
4. 변수를 사용할 수 없게 된다

남은 힌트: 3회
정답 입력 (0: 힌트 보기, 1-4: 답안): 
```

### 6.2 `퀴즈 추가`
문제, 선택지 4개, 정답 번호, 힌트를 입력해 새 퀴즈를 저장합니다.
잘못된 입력은 다시 안내하고, 완료되면 `state.json`에 바로 반영됩니다.
```bash
📌 새로운 퀴즈를 추가합니다.
문제를 입력하세요: Python에서 반복문을 시작할 때 자주 사용하는 키워드는?
선택지 1: if
선택지 2: for
선택지 3: def
선택지 4: class
정답 번호 (1-4): 2
힌트를 입력하세요: 리스트나 문자열을 순회할 때 자주 사용합니다.

✅ 퀴즈가 추가되었습니다!
```

### 6.3 `퀴즈 목록`
등록된 퀴즈를 번호와 함께 확인할 수 있습니다.
원하면 정답 번호와 정답 항목도 함께 볼 수 있습니다.
```bash
📋 등록된 퀴즈 목록 (총 5개)
----------------------------------------
[1] Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?
[2] 함수 안에서 값을 호출한 곳으로 돌려줄 때 사용하는 키워드는 무엇인가요?
[3] 다음 중 Python 함수 호출 예시로 올바른 것은 무엇인가요?
[4] 함수 정의에서 괄호 안에 적는 값들의 이름은 무엇인가요?
[5] 다음 중 함수의 장점으로 가장 알맞은 것은 무엇인가요?
----------------------------------------
1. 정답도 함께 보기
2. 나가기
선택: 1

[1] Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?
정답: 3번 - def
```

### 6.4 `점수 확인`
현재 최고 점수와 점수순 퀴즈 랭킹을 확인할 수 있습니다.
닉네임, 점수, 정답 수/문제 수, 시간이 함께 표시됩니다.
```bash
🏆 현재 최고 점수: 5.0점
🏆 퀴즈 랭킹
----------------------------------------
1. 민수 | 5.0점 | 5/5 | 2026-04-12 14:57:23
2. 지수 | 3.0점 | 3/5 | 2026-04-12 14:57:28
3. 현우 | 2.5점 | 3/5 | 2026-04-12 14:58:44
4. 서연 | 1.0점 | 1/3 | 2026-04-12 15:01:32
5. 도윤 | 0.0점 | 0/2 | 2026-04-12 15:04:22
----------------------------------------
```

### 6.5 `퀴즈 삭제`
사용자가 추가한 퀴즈를 삭제할 수 있습니다.
기본 퀴즈는 삭제되지 않도록 보호했습니다.
```bash
🗑️ 삭제할 퀴즈를 선택하세요.
----------------------------------------
[1] Python에서 반복문을 시작할 때 자주 사용하는 키워드는?
[2] Python에서 문자열 길이를 구할 때 사용하는 함수는?
----------------------------------------
삭제할 퀴즈 번호: 2
1. 삭제
2. 취소
선택: 1

✅ 퀴즈가 삭제되었습니다.
```

### 6.6 `힌트 기능`
한 게임에서 최대 3번까지 힌트를 볼 수 있습니다.
힌트를 사용하고 정답을 맞히면 0.5점, 힌트 없이 맞히면 1점입니다.
```bash
남은 힌트: 3회
정답 입력 (0: 힌트 보기, 1-4: 답안): 0
💡 힌트: 함수를 만들 때 가장 자주 보는 세 글자 키워드입니다.

남은 힌트: 2회
정답 입력 (0: 힌트 보기, 1-4: 답안): 3
✅ 정답입니다!
```

### 6.7 `데이터 저장 및 복구`
퀴즈, 점수, 랭킹/기록이 `state.json`에 저장됩니다.
파일이 없거나 손상되면 기본 퀴즈 데이터로 복구합니다.
```bash
⚠️ state.json 파일을 읽을 수 없어 기본 데이터로 시작합니다.
⚠️ 유효한 퀴즈 데이터가 없어 기본 퀴즈로 복구합니다.
```

### 6.8 `안전 종료 처리`
입력 중 `Ctrl+C(KeyboardInterrupt)` 또는 `EOFError`가 발생해도 프로그램이 비정상 종료되지 않도록 처리했습니다.
안내 메시지를 출력한 뒤 가능한 범위에서 현재 상태를 저장하고 안전하게 종료합니다.
```bash
선택: ^C
입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.
프로그램을 종료합니다.
```

## 7. 파일 구조

```text
e1-2-python-basics-quiz-game/
├── .gitignore
├── README.md
├── main.py
├── state.json
└── src/
    ├── quiz.py
    └── quiz_game.py
```

- `main.py`
  - 프로그램 실행 시작점입니다.
- `src/quiz.py`
  - 퀴즈 한 문제를 표현하는 `Quiz` 클래스를 정의합니다.
  - 문제 내용, 선택지, 정답, 힌트처럼 개별 퀴즈에 필요한 데이터를 보관합니다.
  - 문제 출력, 정답 확인, JSON 저장을 위한 데이터 변환을 담당합니다.
- `src/quiz_game.py`
  - 메뉴, 퀴즈 진행, 점수 계산, 파일 저장/불러오기 등 전체 게임 흐름을 관리하는 `QuizGame` 클래스를 정의합니다.
  - 퀴즈 추가/삭제, 힌트 사용, 점수 확인, 랭킹/히스토리 관리도 이 클래스에서 처리합니다.
- `state.json`
  - 퀴즈 데이터와 점수, 랭킹을 저장하는 파일입니다.
- `README.md`
  - 프로젝트 설명과 실행 방법, Git 기록을 정리한 문서입니다.

이처럼 `Quiz`는 개별 문제의 정보와 동작을 담당하고, `QuizGame`은 게임 전체 흐름과 저장 로직을 담당하도록 책임을 분리했습니다.
이 구조 덕분에 코드의 역할이 명확해지고, 기능을 추가하거나 수정할 때도 더 쉽게 관리할 수 있습니다.
또한 입력 처리, 게임 진행, 저장/복구 로직을 메서드 단위로 나누어 공통 기능은 재사용하고 각 메서드의 책임은 최대한 한 가지로 유지하려고 했습니다.

## 8. 데이터 파일 설명

이 프로젝트는 루트 디렉터리의 `state.json` 파일을 사용해 데이터를 저장합니다.

### 8.1 경로

- `./state.json`

### 8.2 역할

- 기본 퀴즈 및 사용자가 추가한 퀴즈 저장
- 최고 점수 저장
- 점수순 랭킹 기록 저장
- 모든 플레이 히스토리 저장
- 프로그램 재실행 시 상태 복원

### 8.3 주요 필드 구조

```json
{
  "quizzes": [
    {
      "question": "Python의 창시자는?",
      "choices": ["Guido", "Linus", "Bjarne", "James"],
      "answer": 1,
      "hint": "이름이 Guido로 시작합니다."
    }
  ],
  "best_score": 3.5,
  "rankings": [
    {
      "nickname": "east",
      "score": 3.5
    }
  ],
  "history": [
    {
      "nickname": "east",
      "played_at": "2026-04-12 21:35:10",
      "total_questions": 5,
      "correct_count": 4,
      "score": 3.5
    }
  ]
}
```

### 8.4 필드 설명

- `quizzes`
  - 퀴즈 목록
- `question`
  - 문제 내용
- `choices`
  - 선택지 4개
- `answer`
  - 정답 번호 `1~4`
- `hint`
  - 문제 풀이에 도움을 주는 힌트 문구
- `best_score`
  - 현재 최고 점수
- `rankings`
  - 닉네임과 점수 중심의 기록 목록
- `history`
  - 모든 플레이 기록 목록
  - 점수 확인 화면에서는 `history`를 점수순으로 정렬해 랭킹처럼 보여줍니다.
- `played_at`
  - 플레이한 날짜와 시간
- `total_questions`
  - 해당 게임에서 푼 문제 수
- `correct_count`
  - 해당 게임에서 맞힌 문제 수

### 8.5 읽기/쓰기 흐름

- 프로그램 시작 시 `main.py`에서 `QuizGame` 객체를 만든 뒤 `load_state()`를 호출해 `state.json`을 먼저 읽습니다.
- 파일이 없거나 JSON이 손상된 경우에는 안내 메시지를 출력하고 기본 퀴즈 데이터로 복구한 뒤 게임을 시작합니다.
- 실행 중에는 퀴즈 추가, 퀴즈 삭제, 점수/기록 갱신 시점에 `save_state()`를 호출해 현재 상태를 저장합니다.
- 종료 메뉴를 선택하거나 입력 중단이 발생했을 때도 가능한 범위에서 저장한 뒤 안전하게 종료합니다.
- 이 흐름 덕분에 프로그램을 다시 실행해도 퀴즈, 점수, 기록이 유지됩니다.

### 8.6 대용량 데이터 처리 한계

- 현재 구조는 `state.json` 파일 전체를 한 번에 읽고(`json.load`) 전체를 다시 저장하는(`json.dump`) 방식입니다.
- 그래서 퀴즈, 랭킹, 히스토리 데이터가 1000개 이상으로 크게 늘어나면 메모리 사용량과 로딩/저장 시간이 함께 증가할 수 있습니다.
- 특히 `history`와 `rankings`를 리스트로 관리하기 때문에 데이터가 많아질수록 정렬과 탐색 비용도 커집니다.
- 이번 과제 규모에서는 JSON 방식이 단순하고 이해하기 쉬워 적절하지만, 더 큰 규모에서는 오래된 기록 정리, 파일 분리, SQLite 같은 데이터베이스 사용을 고려할 수 있습니다.

## 9. 퀴즈 보너스 기능

현재 구현한 보너스 기능은 아래와 같습니다.

- `랜덤 출제`
  - 퀴즈 풀기 시 문제 순서를 랜덤하게 섞어 출제합니다.
- `문제 수 선택`
  - 퀴즈를 시작할 때 몇 문제를 풀지 직접 입력할 수 있습니다.
- `힌트 기능`
  - `Quiz` 클래스에 `hint` 속성을 추가했습니다.
  - 풀이 중 `0`을 입력하면 힌트를 볼 수 있습니다.
  - 한 게임에서 최대 3번까지 힌트를 사용할 수 있습니다.
  - 힌트를 사용하고 정답을 맞히면 0.5점, 사용하지 않고 맞히면 1.0점을 받습니다.
- `퀴즈 삭제 기능`
  - 사용자가 추가한 퀴즈를 삭제할 수 있습니다.
  - 삭제한 내용은 `state.json` 파일에 바로 반영됩니다.
  - 기본 퀴즈는 삭제되지 않도록 보호했습니다.
- `점수 기록 히스토리`
  - 최고 점수뿐 아니라 모든 게임 기록을 저장합니다.
  - 날짜/시간, 푼 문제 수, 맞힌 문제 수, 점수를 함께 기록합니다.
  - 점수 확인 메뉴에서 기록을 점수순으로 확인할 수 있습니다.

## 10. 브랜치 병합

이번 과제에서는 브랜치를 생성하고 기능 단위로 작업한 뒤 `main` 브랜치에 병합하는 과정을 직접 실습했습니다.

### 10.1 퀴즈 삭제 기능 브랜치 작업

먼저 `feature/delete-quiz` 브랜치를 생성한 뒤 퀴즈 삭제 기능을 구현하고 커밋한 후, 원격 저장소에 push했습니다.

```bash
# 삭제 기능 작업 내용을 스테이징
east1111@1234 e1-2-python-basics-quiz-game % git add .
# 삭제 기능 커밋 생성
east1111@1234 e1-2-python-basics-quiz-game % git commit -m "Feat: 퀴즈 삭제 기능 구현"
# feature/delete-quiz 브랜치로 원격 push
east1111@1234 e1-2-python-basics-quiz-game % git push origin feature/delete-quiz
[feature/delete-quiz 8d9e888] Feat: 퀴즈 삭제 기능 구현
 2 files changed, 57 insertions(+), 14 deletions(-)
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 6 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.00 KiB | 1.00 MiB/s, done.
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'feature/delete-quiz' on GitHub by visiting:
remote:      https://github.com/mov-hyun/e1-2-python-basics-quiz-game/pull/new/feature/delete-quiz
remote:
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
 * [new branch]      feature/delete-quiz -> feature/delete-quiz
```

이후 `main` 브랜치로 돌아와 병합한 뒤 다시 원격 저장소에 push했습니다.

```bash
# main 브랜치로 이동
east1111@1234 e1-2-python-basics-quiz-game % git checkout main
# feature/delete-quiz 브랜치를 main에 병합
git merge feature/delete-quiz
# 병합 결과를 원격 저장소에 push
git push origin main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Updating 2a97f46..8d9e888
Fast-forward
 src/quiz_game.py | 61 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++----
 state.json       | 10 ----------
 2 files changed, 57 insertions(+), 14 deletions(-)
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
   *****..*****  main -> main
```

이 병합은 `fast-forward` 방식으로 진행되었기 때문에, 기능은 정상적으로 반영되었지만 별도의 merge commit은 생성되지 않았습니다.

### 10.2 힌트 기능 브랜치 작업

그다음 `feature/hint` 브랜치를 생성하고, 게임당 3회 힌트 기능을 구현한 뒤 커밋하고 push했습니다.

```bash
# README 수정 내용을 먼저 main 브랜치에 반영
east1111@1234 e1-2-python-basics-quiz-game % git add .
# README 수정 커밋 생성
git commit -m "Docs: README git 명령어 정리 수정"
# main 브랜치 최신 상태를 원격 저장소에 push
git push origin main

[main 0bfec6e] Docs: README git 명령어 정리 수정
 1 file changed, 3 insertions(+), 1 deletion(-)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 441 bytes | 441.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
   8d9e888..0bfec6e  main -> main

# 힌트 기능 개발용 브랜치 생성 및 이동
east1111@1234 e1-2-python-basics-quiz-game % git checkout -b feature/hint
Switched to a new branch 'feature/hint'

# 현재 브랜치 목록 확인
east1111@1234 e1-2-python-basics-quiz-game % git branch
  feature/delete-quiz
* feature/hint
  main

# 힌트 기능 작업 내용을 스테이징
east1111@1234 e1-2-python-basics-quiz-game % git add .
# 힌트 기능 커밋 생성
git commit -m "Feat: 게임당 3회 힌트 기능 구현"
# feature/hint 브랜치를 원격 저장소에 push
git push origin feature/hint

[feature/hint f486202] Feat: 게임당 3회 힌트 기능 구현
 3 files changed, 69 insertions(+), 18 deletions(-)
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 6 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.60 KiB | 1.60 MiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
remote:
remote: Create a pull request for 'feature/hint' on GitHub by visiting:
remote:      https://github.com/mov-hyun/e1-2-python-basics-quiz-game/pull/new/feature/hint
remote:
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
 * [new branch]      feature/hint -> feature/hint
```

이번에는 병합 기록을 명확히 남기기 위해 `--no-ff` 옵션을 사용해 `main` 브랜치에 병합했습니다.

```bash
# main 브랜치로 이동
east1111@1234 e1-2-python-basics-quiz-game % git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

# --no-ff 옵션으로 merge commit을 명시적으로 생성
east1111@1234 e1-2-python-basics-quiz-game % git merge --no-ff feature/hint -m "Merge branch 'feature/hint'"
Merge made by the 'ort' strategy.
 src/quiz.py      |  5 ++++-
 src/quiz_game.py | 61 ++++++++++++++++++++++++++++++++++++++++++++++++++-----------
 state.json       | 21 +++++++++++++++------
 3 files changed, 69 insertions(+), 18 deletions(-)

# 병합된 main 브랜치를 원격 저장소에 push
east1111@1234 e1-2-python-basics-quiz-game % git push origin main
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 225 bytes | 225.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
   0bfec6e..592e202  main -> main
```

### 10.3 최종 병합 결과 확인

마지막으로 아래 명령어로 전체 브랜치와 병합 기록을 확인했습니다.

```bash
# 현재 존재하는 브랜치와 현재 위치 확인
east1111@1234 e1-2-python-basics-quiz-game % git branch
  feature/delete-quiz
* main

# 전체 브랜치와 병합 흐름을 그래프로 확인
east1111@1234 e1-2-python-basics-quiz-game % git log --oneline --graph --decorate --all
*   592e202 (HEAD -> main, origin/main, origin/HEAD) Merge branch 'feature/hint'
|\  
| * f486202 (origin/feature/hint, feature/hint) Feat: 게임당 3회 힌트 기능 구현
|/  
* 0bfec6e Docs: README git 명령어 정리 수정
* 8d9e888 (origin/feature/delete-quiz, feature/delete-quiz) Feat: 퀴즈 삭제 기능 구현
* 2a97f46 Feat: state.json 예외 처리 및 복구 로직 강화
* d693c11 Feat: 닉네임 기반 랭킹 저장 및 점수 확인 기능 구현
* 47c19e9 Feat: 퀴즈 목록 및 정답 보기 기능 구현
* ab7be86 Feat: 퀴즈 추가 기능 구현
* cdb48c1 Feat: 퀴즈 풀기 기능 구현
* 11622d0 docs: README 트러블슈팅 항목 추가
* 72a7845 Feat: quiz_game 메뉴와 공통 입력 처리 구현
* 1e85bb1 Feat: 퀴즈 실행시 초기화면 구현
* 5de6674 Feat: Quiz 프로그램 뼈대 제작
* c2b9fc4 Data: 퀴즈 데이터 파일 생성
* cbedcde git 명령어 정리
* b304e07 프로젝트 md 디자인 다시 수정
* 3270636 프로젝트 md 문법 수정
* 215e8c1 프로젝트 뼈대 수정
* d804c20 프로젝트 뼈대 작성
* 8bbf27d Initial commit
```

이 기록을 통해 `feature/hint` 브랜치에서 작업한 커밋 `f486202`가 `main` 브랜치의 merge commit `592e202`를 통해 병합된 것을 확인할 수 있었습니다. 이 과정을 통해 브랜치를 분리해서 기능을 개발하고, 작업이 끝난 뒤 `main` 브랜치에 안전하게 병합하는 Git 흐름을 직접 경험할 수 있었습니다.

## 11. 트러블 슈팅

### 11.1 GitHub 인증 오류 (PAT 기반 재인증)

| 구분 | 내용 |
|------|------|
| 문제 | git push 실행 시 "Password authentication is not supported" 오류가 발생하며 원격 저장소에 push되지 않음 |
| 원인 | GitHub는 HTTPS Git 작업에서 계정 비밀번호 인증을 지원하지 않는다. 또한 macOS에서는 Git 자격증명이 osxkeychain에 저장되어 재사용될 수 있어, 기존에 저장된 잘못되었거나 만료된 인증 정보가 인증 실패를 유발했을 가능성이 있었다. |
| 해결 | 1. git config --get credential.helper로 osxkeychain 사용 여부를 확인하였다. <br> 2. git credential-osxkeychain erase로 기존 인증 정보 삭제를 시도하였다. <br> 3. 삭제 명령은 오류로 완료되지 않았지만, 이후 git push 과정에서 유효한 인증 정보로 다시 인증이 이루어졌다. <br> 4. 그 결과 정상적으로 원격 저장소에 push할 수 있었다. |
| 결과 | 비밀번호 인증 오류를 해결하고 GitHub 원격 저장소에 정상적으로 push 성공 |

#### 📌 실제 트러블 슈팅 로그

```bash
east1111@1234 e1-2-python-basics-quiz-game % git push
# GitHub에 push를 시도했지만, 비밀번호 인증이 지원되지 않아 실패함
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git/'

east1111@1234 e1-2-python-basics-quiz-game % git config --get credential.helper
# 현재 Git 자격 증명 저장 방식 확인
osxkeychain

east1111@1234 e1-2-python-basics-quiz-game % git credential-osxkeychain erase
# macOS Keychain에 저장된 기존 GitHub 인증 정보 삭제를 시도함
host=github.com
protocol=https

fatal: failed to erase: -1
# Keychain 자격증명 삭제 시도는 실패했음
# 다만 이후 git push에서 유효한 인증 정보가 다시 적용되어 정상적으로 push가 완료됨
# 따라서 직접 해결 요인은 삭제 성공 자체보다 재인증 과정에 있었음

east1111@1234 e1-2-python-basics-quiz-game % git push
# GitHub 비밀번호 대신 PAT를 입력하여 다시 push 실행
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 6 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.11 KiB | 1.11 MiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/mov-hyun/e1-2-python-basics-quiz-game.git
   *****..*****  main -> main

east1111@1234 e1-2-python-basics-quiz-game % git push
# 추가 변경 사항이 없어 최신 상태임
Everything up-to-date
```
