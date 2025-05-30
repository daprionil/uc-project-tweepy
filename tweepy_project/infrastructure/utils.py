import re
from typing import List

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from ..domain.port import UtilsPort


class Utils(UtilsPort):
    def __init__(self) -> None:
        pass

    def clean_text(self, text: str) -> str:
        stop_words = set(stopwords.words("spanish"))
        lemmatizer = WordNetLemmatizer()

        text = text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)
        # Eliminar URLs
        text = re.sub(r"@\w+", "", text)
        # Eliminar menciones
        text = re.sub(r"#\w+", "", text)
        # Eliminar hashtags
        text = re.sub(r"[^a-zA-Záéíóúüñ\s]", "", text)
        # # Eliminar caracteres especiales
        words = text.split()
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        return " ".join(words)

    def clean_tweets(self, tweets: List[str]) -> List[str]:
        return [self.clean_text(tweet) for tweet in tweets]
