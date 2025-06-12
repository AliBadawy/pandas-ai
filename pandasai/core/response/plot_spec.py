from typing import Any, Dict

from .base import BaseResponse


class PlotSpecResponse(BaseResponse):
    """Response class for plot specifications."""

    def __init__(self, value: Dict[str, Any], last_code_executed: str | None = None):
        if not isinstance(value, dict):
            raise ValueError("PlotSpecResponse expects a dictionary value")
        super().__init__(value, "plot_spec", last_code_executed)

    def to_dict(self) -> Dict[str, Any]:
        """Return the plot specification dictionary."""
        return self.value
