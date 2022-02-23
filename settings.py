from pathlib import Path

html_path = Path(__file__).parent.joinpath("html_files")
jpg_path = Path(__file__).parent.joinpath("jpg_files")

if not html_path.exists():
    html_path.mkdir()

if not jpg_path.exists():
    jpg_path.mkdir()
