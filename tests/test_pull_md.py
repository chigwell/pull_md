import pytest
from pull_md import pull_markdown

def test_pull_markdown_valid_url(requests_mock):
    valid_url = "http://example.com"
    expected_markdown = "# Example Domain"
    requests_mock.get(valid_url, text="OK", status_code=200)
    requests_mock.get(f"https://pull.md/{valid_url}", text=expected_markdown, status_code=200)

    result = pull_markdown(valid_url)
    assert result == expected_markdown, "The markdown content was not as expected."

def test_pull_markdown_invalid_url():
    invalid_url = "example.com"
    with pytest.raises(ValueError) as excinfo:
        pull_markdown(invalid_url)
    assert "Invalid URL" in str(excinfo.value), "Error message for invalid URL was not as expected."

def test_pull_markdown_error_status_code(requests_mock):
    bad_url = "http://badexample.com"
    requests_mock.get(bad_url, status_code=404)
    requests_mock.get(f"https://pull.md/{bad_url}", status_code=404)

    with pytest.raises(ValueError) as excinfo:
        pull_markdown(bad_url)
    assert "URL returned status code: 404" in str(excinfo.value), "Error handling for bad status code was not as expected."