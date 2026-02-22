from __future__ import annotations

import os
import subprocess
import sys


def test_cli_help() -> None:
    proc = subprocess.run(
        [sys.executable, "moderate_image.py", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    help_text = f"{proc.stdout}\n{proc.stderr}"
    assert "--no-apis" in help_text


def test_main_import_smoke() -> None:
    __import__("modimg.cli")
    __import__("modimg.pipeline")


def test_cli_help_with_invalid_sample_frames_env_does_not_crash() -> None:
    env = os.environ.copy()
    env["SAMPLE_FRAMES"] = "not_an_int"

    proc = subprocess.run(
        [sys.executable, "moderate_image.py", "--help"],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )

    assert proc.returncode == 0
