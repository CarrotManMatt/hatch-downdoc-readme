"""Python wrapper for converting/reducing AsciiDoc files back to Markdown."""

from typing import TYPE_CHECKING

from console import run

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__: "Sequence[str]" = ("run",)
