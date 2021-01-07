from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-css-properties",
    description="Experimental Datasette output plugin using CSS properties",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-css-properties",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-css-properties/issues",
        "CI": "https://github.com/simonw/datasette-css-properties/actions",
        "Changelog": "https://github.com/simonw/datasette-css-properties/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_css_properties"],
    entry_points={"datasette": ["css_properties = datasette_css_properties"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-css-properties[test]"],
    python_requires=">=3.6",
)
