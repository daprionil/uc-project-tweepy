import abc
from typing import Any, List


class RequestAdapterPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_tweets(
        self,
        query: str,
        max_results: int,
    ) -> Any:
        raise NotImplementedError


class UtilsPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clean_text(self, text: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def generate_graphic(self, sentiments: List[str], tweets: List[str]) -> List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def clean_tweets(self, tweets: List[str]) -> List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def generate_positive_analythics(
        self, sentiments: List[str], tweets: List[str]
    ) -> None:
        raise NotImplementedError


class AnalizerPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def give_sentiments(self, tweets: List[str]) -> List[str]:
        raise NotImplementedError
