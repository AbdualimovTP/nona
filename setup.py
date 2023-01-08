from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1", "numpy>=1", "scikit-learn>=1", "tqdm>=4"]

setup(
    name="nona",
    version="0.0.1",
    author="Timur Abdualimov",
    author_email="timur.atp@yandex.ru",
    description="Python gap filling toolkit",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AbdualimovTP/nona",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
