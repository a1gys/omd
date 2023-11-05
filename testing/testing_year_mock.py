import urllib.request
import json
import unittest
from unittest.mock import patch, Mock


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля
    'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class TestWhatYear(unittest.TestCase):

    @patch("urllib.request.urlopen")
    def test_year_ymd(self, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({
            "currentDateTime": "2023-11-05T12:34:56Z"
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        expected = what_is_year_now()
        self.assertEqual(expected, 2023)

    @patch("urllib.request.urlopen")
    def test_year_dmy(self, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({
            "currentDateTime": "05.11.2023T12:34:56Z"
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        expected = what_is_year_now()
        self.assertEqual(expected, 2023)

    @patch("urllib.request.urlopen")
    def test_year_invalid(self, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({
            "currentDateTime": "2023/11/05T12:34:56Z"
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        with self.assertRaises(ValueError):
            what_is_year_now()
