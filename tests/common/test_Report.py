from codelimit.common.Codebase import Codebase
from codelimit.common.Report import Report


def test_empty_measurements_collection():
    report = Report(Codebase())

    assert report.get_average() == 0
    assert report.ninetieth_percentile() == 0
    assert report.risk_categories() == [0, 0, 0, 0]