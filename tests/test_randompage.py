# tests/test_randompage.py
import pytest
import json
from unittest.mock import patch, mock_open
from main import get_data_fromApi, get_data_fromFile, format_data

@pytest.fixture
def mock_api_response():
    mockResponse = {
        'items': [{'title': 'Test Title', 'subjects': ['TestSubject'], 'field_offices': ['TestOffice']}]
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mockResponse
        yield mockResponse

def test_extractTitle(mock_api_response):
    data = get_data_fromApi(1)
    assert data['items'][0]['title'] == 'Test Title'

def test_extractSubjects():
    mock_data = {
        'items': [{'title': 'Test Title', 'subjects': ['TestSubject'], 'field_offices': ['TestOffice']}]
    }
    with patch('builtins.open', mock_open(read_data=json.dumps(mock_data))):
        data = get_data_fromFile('dummy_location')
        assert data['items'][0]['subjects'] == ['TestSubject']

def test_extractFieldOffices(mock_api_response):
    data = get_data_fromApi(1)
    assert data['items'][0]['field_offices'] == ['TestOffice']

@patch('builtins.print')
@patch('builtins.open', new_callable=mock_open)
def test_printThornSeparatedFile(mock_file, mock_print, mock_api_response):
    data = mock_api_response
    format_data(data, 'test.csv')

    # Check the content of the CSV file
    mock_file.assert_called_once_with('test.csv', 'w', newline='', encoding='utf-8')
    handle = mock_file()
    handle.write.assert_any_call('TitleþSubjectsþField Offices\r\n')
    handle.write.assert_any_call('Test TitleþTestSubjectþTestOffice\r\n')

    # Check printed output
    mock_print.assert_any_call('Test TitleþTestSubjectþTestOffice')
