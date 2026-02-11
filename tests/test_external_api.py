import os
import unittest
from unittest.mock import Mock, patch

from src.external_api import report_operation


class TestReportOperation(unittest.TestCase):

    @patch("src.external_api.requests.get")
    @patch.dict(os.environ, {"API_KEY": "test_key"})
    def test_report_operation_non_rub(self, mock_get):
        action = {"operationAmount": {"amount": "2000.00", "currency": {"name": "USD", "code": "USD"}}}

        mock_response = Mock()
        mock_response.json.return_value = {"result": 150000.0}
        mock_get.return_value = mock_response

        result = report_operation(action)

        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": "test_key"},
            params={"amount": "2000.00", "from": "USD", "to": "RUB"},
        )

        self.assertEqual(result, 150000.0)

    def test_report_operation_rub(self):
        action = {"operationAmount": {"amount": "500.50", "currency": {"name": "RUB", "code": "RUB"}}}

        result = report_operation(action)
        self.assertEqual(result, 500.50)
