from codelimit.common.Language import Language
from codelimit.common.Token import Token
from codelimit.common.gsm.operator.OneOrMore import OneOrMore
from codelimit.common.gsm.operator.Union import Union
from codelimit.common.gsm.operator.ZeroOrMore import ZeroOrMore
from codelimit.common.scope.Header import Header
from codelimit.common.scope.scope_utils import (
    get_blocks,
    get_headers,
)
from codelimit.common.token_matching.predicate.And import And
from codelimit.common.token_matching.predicate.Balanced import Balanced
from codelimit.common.token_matching.predicate.Keyword import Keyword
from codelimit.common.token_matching.predicate.Name import Name
from codelimit.common.token_matching.predicate.Not import Not
from codelimit.common.token_matching.predicate.Or import Or
from codelimit.common.token_matching.predicate.Symbol import Symbol


class Java(Language):
    def __init__(self):
        super().__init__("Java")

    def extract_headers(self, tokens: list) -> list:
        headers = get_headers(
            tokens, [Name(), OneOrMore(Balanced('(', ')'))],
            [
                Union(
                    Symbol("{"),
                    [Keyword('throws'), ZeroOrMore(And(Not(';'), Not('{'))), Symbol("{")]
                )
            ]
            , nested=True)
        return filter_headers(headers, tokens)

    def extract_blocks(self, tokens: list, headers: list) -> list:
        return get_blocks(tokens, "{", "}")


def filter_headers(headers: list[Header], tokens: list[Token]) -> list[Header]:
    result = []
    keywords = Or(Keyword('record'), Keyword('new'))
    for header in headers:
        if header.token_range.start > 0 and keywords.accept(tokens[header.token_range.start - 1]):
            continue
        else:
            result.append(header)
    return result
