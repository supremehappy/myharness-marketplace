# myharness-marketplace

practice-m3 하네스에서 agents · hooks · skills만 뽑아 만든 로컬 플러그인 마켓플레이스입니다.

## 설치

```
/plugin marketplace add supremehappy/myharness-marketplace
/plugin install myharness@myharness-marketplace
```

## 들어 있는 것

| 종류 | 이름 | 하는 일 |
|---|---|---|
| agent | verifier | spec 기준 검증, 보고만 함 |
| agent | cleaner | 죽은 코드 · 어긋난 문서 정리 |
| skill | round-close | 라운드 종료 조건 점검 |
| hook | guard.py (PreToolUse) | rm -rf, 강제 삭제, force push, .env 읽기 차단 |
| hook | project_lint.py (PostToolUse) | 프로젝트에 `scripts/arch_lint.py`가 있으면 실행 |

## 프로젝트마다 따로 둘 것

- `CLAUDE.md`: 코드 규칙, 테스트 · 린트 명령, 패키지 규칙
- `scripts/arch_lint.py`: 그 프로젝트의 아키텍처 규칙
- `docs/ROADMAP.md`, `docs/SSOT.md`, `docs/roundNN/`

Hook은 `python`을 PATH에서 찾습니다.
