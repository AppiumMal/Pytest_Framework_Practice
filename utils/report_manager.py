import json
import logging
import re
from datetime import datetime, timezone
from html import escape
from importlib import import_module
from pathlib import Path
from typing import Any

from pytest import Item
from _pytest.reports import TestReport


class ReportManager:
    def __init__(self, artifact_dir: str | Path = "test-artifacts") -> None:
        self.artifact_dir = Path(artifact_dir)
        self.logger = logging.getLogger(__name__)

    def _artifact_stem(self, test_name: str) -> str:
        stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", test_name).strip("_.")
        return stem or "test"

    def capture_screenshot(self, driver: Any, test_name: str) -> Path:
        self.artifact_dir.mkdir(parents=True, exist_ok=True)
        path = self.artifact_dir / f"{self._artifact_stem(test_name)}.png"
        if not driver.save_screenshot(str(path)):
            raise OSError(f"WebDriver did not save screenshot to {path}")
        self.logger.info("Captured screenshot: %s", path)
        return path

    def attach_test_metadata(
        self,
        report: TestReport,
        metadata: dict[str, Any],
        screenshot_path: Path | None = None,
        artifact_path: Path | None = None,
        html_report_enabled: bool = False,
    ) -> None:
        if not html_report_enabled:
            return

        extras = import_module("pytest_html.extras")
        report_extras = getattr(report, "extras", [])
        setattr(report, "extras", report_extras)
        details = "<pre>{}</pre>".format(escape(json.dumps(metadata, indent=2)))
        report_extras.append(extras.html(details))
        if artifact_path is not None:
            report_extras.append(
                extras.url(artifact_path.as_posix(), name="Test metadata JSON")
            )
        if screenshot_path is not None:
            report_extras.append(extras.image(screenshot_path.as_posix()))

    def create_test_artifact(
        self,
        item: Item,
        report: TestReport,
        screenshot_path: Path | None = None,
        screenshot_error: str | None = None,
        html_report_enabled: bool = False,
    ) -> Path:
        self.artifact_dir.mkdir(parents=True, exist_ok=True)
        artifact_path = self.artifact_dir / (
            f"{self._artifact_stem(item.nodeid)}.json"
        )
        metadata = {
            "test": item.nodeid,
            "outcome": report.outcome,
            "phase": report.when,
            "duration_seconds": report.duration,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "markers": [marker.name for marker in item.iter_markers()],
            "failure": str(report.longrepr) if report.failed else None,
            "screenshot": str(screenshot_path) if screenshot_path else None,
            "screenshot_error": screenshot_error,
        }
        artifact_path.write_text(
            json.dumps(metadata, indent=2), encoding="utf-8"
        )
        self.attach_test_metadata(
            report, metadata, screenshot_path, artifact_path,
            html_report_enabled,
        )
        self.logger.info("Created test artifact: %s", artifact_path)
        return artifact_path
