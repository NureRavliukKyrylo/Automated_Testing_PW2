import re
from abc import ABC, abstractmethod


class CellRule(ABC):

    @abstractmethod
    def matches(self, value: str) -> bool:
        pass


class NumberRule(CellRule):

    def matches(self, value: str) -> bool:
        return value.isdigit()


class TextRule(CellRule):

    def matches(self, value: str) -> bool:
        return bool(re.search(r"[a-zA-Z]", value)) and not bool(re.search(r"\d", value))


class MixedRule(CellRule):

    def matches(self, value: str) -> bool:
        return bool(re.search(r"[a-zA-Z]", value)) and bool(re.search(r"\d", value))