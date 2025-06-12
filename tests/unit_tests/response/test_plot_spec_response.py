import pytest

from pandasai.core.response.plot_spec import PlotSpecResponse


def test_plot_spec_response_initialization():
    spec = {"x": "age", "y": "salary"}
    response = PlotSpecResponse(spec, "code")
    assert response.type == "plot_spec"
    assert response.value == spec
    assert response.last_code_executed == "code"


def test_plot_spec_to_dict():
    spec = {"x": "age"}
    response = PlotSpecResponse(spec, None)
    assert response.to_dict() == spec
