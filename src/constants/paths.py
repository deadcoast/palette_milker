from pathlib import Path


class Paths:
    """Paths to the data files."""

    DATA_DIR = Path(__file__).parent / "data"
    PALETTES_FILE = DATA_DIR / "palettes.json"
    CSS_PATH = "app.tcss"

    @classmethod
    def get_data_dir(cls) -> Path:
        """Get the data directory."""
        return Path(cls.DATA_DIR)

    @classmethod
    def get_palettes_file(cls) -> Path:
        """Get the palettes file."""
        return Path(cls.PALETTES_FILE)

    @classmethod
    def get_css_path(cls) -> Path:
        """Get the CSS path."""
        return Path(cls.CSS_PATH)
