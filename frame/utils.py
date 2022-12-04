import socket
import pytest
import random
import string
from requests import request


class Utils:

    @staticmethod
    # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    def get_ip() -> str:
        return '192.168.0.104'

    def skipped(el: tuple, lst: list) -> tuple:
        if any(map(lambda x: x in el, lst)):
            return pytest.param(el, marks=pytest.mark.skip)
        return el

    def xfailed(el: tuple, lst: list) -> tuple:
        if any(map(lambda x: x in el, lst)):
            return pytest.param(el, marks=pytest.mark.xfail)
        return el

    def random_letters(size):
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))

    def random_digits(size):
        return ''.join(random.choice(string.digits) for _ in range(size))

    def random_symbols(size):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
    