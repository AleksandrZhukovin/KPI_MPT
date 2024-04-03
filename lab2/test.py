from unittest import TestCase
from .main import decoder


class TestDecoder(TestCase):
    def test_simple_string(self) -> None:
        self.assertEqual('hello world', decoder('uryyb jbeyq'))

    def test_string_with_special_symbols(self) -> None:
        self.assertEqual('1hel-_lo2 ()world*!?', decoder('1ury-_yb2 ()jbeyq*!?'))

    def test_string_with_wrong_alphabet(self) -> None:
        try:
            decoder('hello фыЪ汉字')
        except ValueError as error:
            self.assertEqual(error.__str__(), 'String must contain only Latin alphabet, digits and special characters')
        else:
            self.assertEqual(1, 0)
