from typing import Any

from tweepy_project.domain.port import AnalizerPort, RequestAdapterPort, UtilsPort


class App:
    analizer: AnalizerPort
    utils: UtilsPort
    requests: RequestAdapterPort

    def __init__(
        self, analizer: AnalizerPort, utils: UtilsPort, requests: RequestAdapterPort
    ) -> None:
        self.analizer = analizer
        self.utils = utils
        self.requests = requests

    def __call__(self) -> Any:
        # API X y trae los tweets
        query = "#react lang:es"
        tweets = self.requests.get_tweets(query, 10)

        # clean text
        clean_tweets = self.utils.clean_tweets(tweets)

        # analiza los tweets y extrae los sentimientos
        sentiment_labels = self.analizer.give_sentiments(clean_tweets)

        # Usa mathplotlib para visualizar resultados
        self.utils.generate_graphic(sentiment_labels)
