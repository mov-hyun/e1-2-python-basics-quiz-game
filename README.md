# E1-2. Git과 함께하는 Python 첫 발자국
---
## 1.프로젝트 개요

- Python 기반 CLI 퀴즈 게임 구현     
- 객체지향 설계       
- JSON 기반 데이터 파일 사용       
- Git을 활용한 프로젝트 관리       

[1. 프로젝트 개요](#1-프로젝트-개요)   
[2. Git 명령어 정리](#2-git-명령어-정리)   
[3. 퀴즈 주제와 선정 이유](#3-퀴즈-주제와-선정-이유)   
[4. 실행 방법](#4-실행-방법)   
[5. 기능 목록](#5-기능-목록)   
[6. 파일 구조](#6-파일-구조)   
[7. 데이터 파일 설명](#7-데이터-파일-설명)   
[8. 퀴즈 보너스 기능](#8-퀴즈-보너스-기능)   
[9. 브랜치 병합](#9-브랜치-병합)   
[10. 트러블 슈팅](#10-트러블-슈팅)   

### 프로젝트 구조

```
e1-2-python-basics-quiz-game/  
├── .gitignore     
├── README.md      
├── main.py
├──    
└── src/      
     ├── quiz_game.py
     └── quiz.py
```

### 수행항목 체크리스트

- [ ] 프로젝트 개요
- [ ] Git 명령어 정리
- [ ] 퀴즈 주제와 선정 이유
- [ ] 실행 방법
- [ ] 기능 목록
- [ ] 파일 구조
- [ ] 데이터 파일 설명
- [ ] 퀴즈 보너스 기능
- [ ] Python 기본 정리
- [ ] 트러블 슈팅

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

## 3. 퀴즈 주제와 선정 이유

퀴즈 주제는 "Python 기초 문법"입니다.

선정 이유는 다음과 같습니다.
- 개발 입문 과정에서 가장 기본이 되는 내용
- 어차피 필요해서 이참에 공부해두면 좋음


## 4. 실행 방법

프로젝트 루트 디렉터리에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

Python 3.10 이상 환경에서 실행하는 것을 권장합니다.

## 5. 기능 목록

## 6. 파일 구조

## 7. 데이터 파일 설명

## 8. 퀴즈 보너스 기능

## 9. 브랜치 병합

이번 과제에서는 브랜치를 생성하고 기능 단위로 작업한 뒤 `main` 브랜치에 병합하는 과정을 직접 실습했습니다.

### 9.1 퀴즈 삭제 기능 브랜치 작업

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

### 9.2 힌트 기능 브랜치 작업

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

### 9.3 최종 병합 결과 확인

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

## 10. 트러블 슈팅

### 10.1 GitHub 인증 오류 (PAT 기반 재인증)

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
