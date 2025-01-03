[![PyPI version](https://badge.fury.io/py/pull-md.svg?1)](https://badge.fury.io/py/pull-md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/pull-md?1)](https://pepy.tech/project/pull-md)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# Pull.md

`pull_md` is a straightforward Python package that enables developers to convert web pages to Markdown format using the `https://pull.md/` service. It provides a simple function that accepts a URL and returns the Markdown conversion of the web page.

## Installation

Get started by installing `pull_md` using pip:

```bash
pip install pull_md
```

## Usage

`pull_md` is easy to use with a simple function that takes a URL as input and outputs the Markdown. Here's a basic example of converting a webpage to Markdown:

```python
from pull_md import pull_markdown

url = "http://example.com"
markdown = pull_markdown(url)
print(markdown)
```

This function checks the validity of the URL and retrieves the Markdown from the Pull.md service, handling any errors gracefully by providing informative messages.

**Note**: `pull_md` is capable of handling web pages that use JavaScript for rendering content, such as those built with ReactJS, Angular, or Vue.js. This makes it suitable for converting modern web applications into Markdown format.

## Features

- Simple function call to convert any URL to Markdown.
- Capable of handling JavaScript-rendered pages like those built with React, ensuring broad compatibility.
- Error handling for non-existent URLs or access issues.
- Dependency only on the requests library for HTTP requests.

## Contributing

Contributions to `pull_md` are welcome! Whether it's bug fixes, feature enhancements, or improvements to the documentation, we appreciate your help. Please feel free to fork the repository and submit pull requests.

- **Fork the Repository**: Go to [GitHub repository](https://github.com/chigwell/pull_md) and use the 'fork' button to create your own copy.
- **Clone Your Fork**: `git clone https://github.com/your-username/pull_md.git`
- **Create a Branch**: `git checkout -b your-branch-name`
- **Make Changes and Commit**: `git add .` then `git commit -m "Add some changes"`
- **Push to GitHub**: `git push origin your-branch-name`
- **Submit a Pull Request**: Open your fork on GitHub, select your branch, and click on 'Compare & pull request' button.

For more information on the development process, please check our [issues page](https://github.com/chigwell/pull_md/issues).

## License

`pull_md` is released under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use it in any commercial or personal projects.
