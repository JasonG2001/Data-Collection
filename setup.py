from setuptools import setup
from setuptools import find_packages

setup(

    name="project",
    description="Scraper which allows you to scrape the information from the myprotein website",
    version="1.0.0",
    url="https://github.com/JasonG2001/Data-Collection",

    author="Jason Guan",
    license="MIT",
    packages=find_packages(),
    install_requires=["selenium"]

)