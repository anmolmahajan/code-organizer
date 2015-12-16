
from setuptools import setup

setup(name="code-organizer",
	version="1.0",
	description="This module sorts the source codes in the current directory based on their language.",
	url="https://github.com/anmolmahajan/code-organizer.git",
	author="Anmol Mahajan",
	author_email="mahajan.anmol@gmail.com",
	license='MIT',
	packages=["code-organizer"],
	scripts=["bin/code-organizer"],
	zip_safe=False)
