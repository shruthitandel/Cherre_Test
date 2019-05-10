"""
This is the test suite for lambda_function.py.
"""

from unittest import TestCase, main
from interviews.cherre.lambda_function import lambda_handler


class TestLambdaFunction(TestCase):
    def test_lambda_handle(self):
        test = lambda_handler(None, None)
        print(test)
        self.assertEqual(200, test["statusCode"])
