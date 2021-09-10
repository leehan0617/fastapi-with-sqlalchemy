import unittest
from component.token_manager import create_jwt, validate_jwt


class TokenManagerTest(unittest.TestCase):

    def test_create_token(self):
        id = 'test_id'
        token = create_jwt(id)
        print(token)

    def test_validate_jwt(self):
        id = 'test_id2'
        token = create_jwt(id)
        token2 = token + 'asdf'
        maybe_true = validate_jwt(token)
        maybe_false = validate_jwt(token2)
        self.assertTrue(maybe_true)
        self.assertFalse(maybe_false)
