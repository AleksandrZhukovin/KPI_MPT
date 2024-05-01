from unittest import TestCase
from main import decoder
import subprocess


subprocess.run(['chmod uog=rwx main.py'], shell=True)


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

    def test_empty_string(self) -> None:
        self.assertEqual('', decoder(''))

    def test_stdin_valid_input(self) -> None:
        result = subprocess.run(['echo uryyb jbeyq | python3 main.py'], shell=True, stdout=subprocess.PIPE)
        self.assertEqual('Decoded text is: hello world\n\n', result.stdout.decode('utf-8'))

    def test_stdin_invalid_input(self) -> None:
        try:
            result = subprocess.run(['echo hello фыЪ汉字 | python3 main.py'], shell=True, stderr=subprocess.PIPE)
        except ValueError:
            self.assertEqual('String must contain only Latin alphabet, digits and special characters\n', result.stderr.decode('utf-8'))

    def test_exit_code_when_correct(self) -> None:
        with self.assertRaises(SystemExit) as cm:
            subprocess.run(['echo uryyb jbeyq | python3 main.py'], shell=True)
        self.assertEqual(cm.exception.code, 0)

    def test_exit_code_when_incorrect(self) -> None:
        with self.assertRaises(SystemExit) as cm:
            subprocess.run(['echo hello фыЪ汉字 | python3 main.py'], shell=True)
        self.assertEqual(cm.exception.code, 1)
