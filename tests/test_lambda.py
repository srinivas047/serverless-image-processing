import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        event = {"bucket": "test-bucket", "key": "test.jpg"}
        result = lambda_handler(event, None)
        self.assertEqual(result["statusCode"], 200)

