import webbrowser

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Static

from codelimit.common.report.Report import Report
from codelimit.tui.QualityProfile import QualityProfile
from codelimit.version import version


class Header(Widget):
    def __init__(self, report: Report):
        super().__init__()
        self.report = report
        self.styles.dock = 'top'
        self.styles.width = '100%'
        self.styles.height = 3

    def compose(self) -> ComposeResult:
        # yield Vertical(Static(Text.from_ansi(self.report.risk_category_plot())))
        yield Vertical(Static(self.report.codebase.root), QualityProfile(self.report.quality_profile()))


class HeaderLeft(Static):
    def __init__(self, *children: Widget):
        super().__init__(*children)
        self.styles.dock = 'left'

    def render(self) -> str:
        return f'CodeLimit v.{version}'

    def on_click(self) -> None:
        webbrowser.open('https://github.com/getcodelimit/codelimit')