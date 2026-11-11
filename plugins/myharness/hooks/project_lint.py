"""프로젝트의 아키텍처 린터를 부르는 PostToolUse Hook.

규칙 자체는 프로젝트마다 다르므로 플러그인에 넣지 않는다.
프로젝트에 scripts/arch_lint.py 가 있으면 실행하고, 없으면 그냥 통과한다.
  - pyproject.toml 이 있고 uv 가 있으면 `uv run --project` 로 실행
  - 아니면 지금 Python 으로 실행
린터가 exit 2 로 끝나면 그 stderr 를 그대로 에이전트에게 돌려준다.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    project = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
    lint = project / "scripts" / "arch_lint.py"
    if not lint.is_file():
        return 0

    if (project / "pyproject.toml").is_file() and shutil.which("uv"):
        cmd = ["uv", "run", "--project", str(project), "python", str(lint)]
    else:
        cmd = [sys.executable, str(lint)]
    result = subprocess.run(cmd, cwd=project, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        sys.stderr.write(result.stderr or result.stdout)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
