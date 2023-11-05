from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b
                        in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class OheTest(unittest.TestCase):
    def test_single_string(self):
        transformed = fit_transform("Way down We Go")
        expected = [("Way down We Go", [1])]
        self.assertEqual(transformed, expected)

    def test_multiple_unique_strings(self):
        alphabet = ["apple", "banana", "circle", "dice", "egg"]
        transformed = fit_transform(alphabet)
        expected = [
            ("apple", [0, 0, 0, 0, 1]),
            ("banana", [0, 0, 0, 1, 0]),
            ("circle", [0, 0, 1, 0, 0]),
            ("dice", [0, 1, 0, 0, 0]),
            ("egg", [1, 0, 0, 0, 0])
        ]
        self.assertEqual(transformed, expected)

    def test_multiple_repeated_strings(self):
        chocolates = ["kitkat", "bounty", "milky", "bounty", "mars", "milky"]
        transformed = fit_transform(chocolates)
        expected = [
            ("kitkat", [0, 0, 0, 1]),
            ("bounty", [0, 0, 1, 0]),
            ("milky", [0, 1, 0, 0]),
            ("bounty", [0, 0, 1, 0]),
            ("mars", [1, 0, 0, 0]),
            ("milky", [0, 1, 0, 0])
        ]
        self.assertEqual(transformed, expected)

    def test_no_duplicates(self):
        transformed = fit_transform(["red", "green", "blue"])
        for color, ohe_list in transformed:
            for i, value in enumerate(ohe_list):
                for other_ohe_list in transformed:
                    if ohe_list != other_ohe_list:
                        self.assertNotIn(value, other_ohe_list)

    def test_with_duplicates(self):
        drinks = ["tea", "coffee", "tea", "juice", "alcohol", "juice"]
        transformed = fit_transform(drinks)
        for i, ohe in enumerate(transformed):
            drink = ohe[0]
            ohe_list = ohe[1]
            for j, other_ohe in enumerate(transformed):
                other_drink = other_ohe[0]
                if i != j and drink == other_drink:
                    self.assertIn(ohe_list, other_ohe)
                elif drink != other_drink:
                    self.assertNotIn(ohe_list, other_ohe)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_mixed_input(self):
        mixed = ["random", "words", ["first", "second", "third"]]
        with self.assertRaises(TypeError):
            fit_transform(mixed)
