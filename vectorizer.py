from typing import Dict, List, Iterable


class CountVectorizer:
    """
    Transforms given sequence (text) into numerical vector
    vector represents the number of occurence of a word in
    the given sequence
    fit_transform and transform functions return
    vector, where elements in alphabetical order
    """
    chars = ".,!?:"

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase
        self._vocabulary = None

    def fit_transform(self, texts: Iterable) -> List[List[int]]:
        words = []
        for text in texts:
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()

            words.extend(text.split())
        words = sorted(set(words))

        self._vocabulary = {word: index for index, word in enumerate(words)}

        vector = [[0]*len(words) for _ in range(len(texts))]
        for i, text in enumerate(texts):
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()
            for word in text.split():
                ind = words.index(word)
                vector[i][ind] += 1
        return vector

    def fit(self, texts: Iterable):
        words = []
        for text in texts:
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()

            words.extend(text.split())
        words = sorted(set(words))

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
                    ind = words.index(word)
                    vector[i][ind] += 1
                except ValueError:
                    continue
        return vector

    def get_feature_names(self) -> List[str]:
        if not self._vocabulary:
            raise ValueError("Vocabulary is not fitted")
        return list(self._vocabulary.keys())

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
