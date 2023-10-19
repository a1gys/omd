from typing import Dict, List, Iterable, Optional


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
        words = []
        for text in texts:
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()
            for word in text.split():
                if word not in words:
                    words.append(word)

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
        words = []
        for text in texts:
            for char in self.chars:
                text = text.replace(char, "")
            if self.lowercase:
                text = text.lower()
            for word in text.split():
                if word not in words:
                    words.append(word)

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
