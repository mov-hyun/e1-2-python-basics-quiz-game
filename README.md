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
[9. Python 기본 정리](#9-python-기본-정리)   
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
| `git checkout` | 브랜치 이동 또는 새 브랜치 생성 | `git checkout -b play-quiz` |
| `git clone` | 원격 저장소를 로컬로 복제 | `git clone <저장소_URL>` |

이번 과제에서는 위 명령어들을 사용해 초기 설정, 기능별 커밋, 브랜치 작업, 병합, 원격 저장소 업로드, clone/pull 실습을 진행했습니다.

## 3. 퀴즈 주제와 선정 이유

퀴즈 주제는 "Python 기초 문법"입니다.

선정 이유는 다음과 같습니다.
- 개발 입문 과정에서 가장 기본이 되는 내용
- 어차피 필요해서 이참에 공부해두면 좋음


## 4. 실행 방법

## 5. 기능 목록

## 6. 파일 구조

## 7. 데이터 파일 설명

## 8. 퀴즈 보너스 기능

## 9. Python 기본 정리

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