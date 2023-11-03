from typing import Dict, List, Iterable, Optional
from itertools import chain


class CountVectorizer:
    """
    Transforms given sequence (text) into numerical vector.
    Vector represents the number of occurences of a word in
    the given sequence.
    fit_transform and transform functions return vector,
    where elements preserve initial order
    """
    chars = ".,!?:"

    def __init__(self,
                 lowercase: bool = True,
                 updated_chars: Optional[str] = None):
        self.lowercase = lowercase
        if updated_chars:
            self.chars += updated_chars
        self._vocabulary = None

    def fit_transform(self, texts: Iterable) -> List[List[int]]:
        words = self._get_words(texts)
        self._vocabulary = {word: index for index, word in enumerate(words)}
        vector = [[0]*len(words) for _ in range(len(texts))]
        for i, text in enumerate(texts):
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()
            for word in text.split():
                vector[i][self._vocabulary[word]] += 1
        return vector

    def fit(self, texts: Iterable):
        words = self._get_words(texts)
        self._vocabulary = {word: index for index, word in enumerate(words)}

    def transform(self, texts: List[str]) -> List[str]:
        words = self.get_feature_names()
        vector = [[0]*len(words) for _ in range(len(texts))]

        for i, text in enumerate(texts):
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()
            for word in text.split():
                try:
                    vector[i][self._vocabulary[word]] += 1
                except KeyError:
                    continue
        return vector

    def get_feature_names(self) -> List[str]:
        if not self._vocabulary:
            raise ValueError("Vocabulary is not fitted")
        return list(self._vocabulary.keys())

    def _get_words(self, texts: Iterable) -> List[str]:
        words = []
        if self.lowercase:
            flattened_words = [text.lower().split() for text in texts]
        else:
            flattened_words = [text.split() for text in texts]
        flattened_words = list(chain.from_iterable(flattened_words))
        for word in flattened_words:
            for char in self.chars:
                word = word.replace(char, "")
            if word not in words:
                words.append(word)
        return words

    @property
    def vocabulary(self) -> Dict[str, int]:
        return self._vocabulary

    @vocabulary.deleter
    def vocabulary(self):
        self._vocabulary.clear()

    @vocabulary.setter
    def vocabulary(self, updated_vocab: Dict[str, int]):
        if not updated_vocab:
            raise ValueError("Updated vocabulary is empty")
        difference = updated_vocab.keys() - self._vocabulary.keys()

        if difference:
            self._vocabulary = updated_vocab


if __name__ == "__main__":
    vectorizer = CountVectorizer()
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
        ]
    count_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    print(f"Features: {feature_names}")
    print(f"Count matrix: {count_matrix}")
