from setuptools import setup, find_packages

setup(
    name="pull_md",
    version="2025.132.816",
    packages=find_packages(),
    url="https://github.com/chigwell/pull_md",
    license="MIT",
    author="Eugene Evstafev",
    author_email="chigwel@gmail.com",
    description="A simple Python package to convert URLs to Markdown.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)