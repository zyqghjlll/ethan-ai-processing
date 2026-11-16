import unittest
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from main import app


class ClassificationTests(unittest.TestCase):
    def test_endpoint_calls_classifier(self):
        with patch('main.classify_text', new_callable=AsyncMock) as classify:
            classify.return_value = 'billing'
            with TestClient(app) as client:
                response = client.post('/classify', json={'text': 'I was charged twice'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {'category': 'billing'})
            classify.assert_awaited_once_with('I was charged twice')
