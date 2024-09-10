# tests/test_download.py
import pytest
from unittest.mock import patch
from main import get_data_fromApi  # Import directly from main.py

@pytest.fixture
def mock_api_response():
    mockResponse = {
        'items': [{'title': 'Test Title', 'subjects': ['TestSubject'], 'field_offices': ['TestOffice']}]
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mockResponse
        yield mockResponse

def test_downloadNonEmptyData(mock_api_response):
    data = get_data_fromApi(1)
    assert len(data['items']) > 0 # checking if data is not empty
