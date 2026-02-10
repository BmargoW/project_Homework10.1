from unittest.mock import mock_open, patch

from src.utils import uploading_content


# тест при работе с файлом, содержащим данные
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


# тест при обращению к несуществующему файлу
def test_uploading_content_not_found_json():
    mock_data = "not found file"
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        result = uploading_content("dummy.json")
        assert result == []
