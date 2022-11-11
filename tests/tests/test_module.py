import typing
import unittest
from panther_sdk import PantherEvent
import floop


class TestModule(unittest.TestCase):
    def test_root_module_api(self) -> None:
        self.assertIsInstance(floop.__main__.run, typing.Callable)  # type: ignore
