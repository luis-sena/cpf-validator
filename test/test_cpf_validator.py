import unittest
from app import app


class TestCPFValidator(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_cpf(self):
        valid_cpf = '12345678909'  # Substitua por um CPF válido
        response = self.app.post('/validate', json={'cpf': valid_cpf})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'valid': True})

    def test_invalid_cpf(self):
        invalid_cpf = '12345678900'  # Substitua por um CPF inválido
        response = self.app.post('/validate', json={'cpf': invalid_cpf})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'valid': False})

    def test_missing_cpf(self):
        response = self.app.post('/validate', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'CPF is required'})


if __name__ == '__main__':
    unittest.main()
