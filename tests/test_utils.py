from unittest.mock import mock_open, patch

from src.utils import uploading_content


def test_uploading_content_valid_json():
    mock_data = '{"key": "value"}'
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        result = uploading_content("dummy.json")
        assert result == {"key": "value"}


# Тест невалидного JSON
def test_uploading_content_invalid_json():
    mock_data = "not a json"
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        result = uploading_content("dummy.json")
        assert result == []
