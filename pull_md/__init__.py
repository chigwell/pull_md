import requests


def pull_markdown(url):
    """Converts the given URL to markdown format using the pull.md service."""
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL. Please include http:// or https://")

    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"URL returned status code: {response.status_code}")

    response = requests.get(f"https://pull.md/{url}")
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()