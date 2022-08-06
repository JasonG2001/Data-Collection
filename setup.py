from setuptools import setup
from setuptools import find_packages

setup(
    name = "Data-collection pipeline",
    description = "Scraper which allows you to scrape the information from the myprotein website",
    url = "https://github.com/JasonG2001/Data-Collection",

    author = "Jason Guan",
    license = "MIT",
    packages = find_packages()
    install_requires = ["selenium", "time", "web_navigator", "urllib.request", "uuid", "os", "json"],

)