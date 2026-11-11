---
name: round-close
description: 개발 라운드를 끝내기 전에 사용한다. 문서 · 정리 · 테스트 종료 조건을 점검한다.
---

# 라운드 종료 절차

아래를 모두 지킨다. 하나라도 안 되면 끝났다고 보고하지 않는다.

1. `docs/roundNN/spec.md` · `plan.md` · `review.md`가 지금 코드와 맞는다.
2. `docs/SSOT.md`를 지금 코드 기준으로 고쳤다. (현재 라운드, API 목록, 데이터 모델)
3. cleaner 에이전트로 죽은 코드를 정리했고, 결과를 `review.md`에 적었다.
4. verifier 에이전트로 검증했고, CLAUDE.md에 적힌 테스트 · 린트 명령이 통과한다.
5. `docs/ROADMAP.md`에서 이번 라운드를 완료로 표시했다.

Hook에 막힌 작업은 다른 명령으로 우회하지 말고 멈춰서 사람에게 보고한다.
