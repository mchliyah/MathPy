import sys
import os
from __main__ import MathPy
from setuptools import setup, find_packages

os.environ['ANACONDA3_PATH'] = "C:\\ProgramData\\Anaconda3\\envs\\Calculator\\Library\\bin\\"

base = None

# GUI applications require a different base on Windows (the default is for a console application).
if sys.platform == "win32":
    base = "Win32GUI"

elif sys.platform == "win64":
    base = "Win64GUI"

setup(
    packages=find_packages(),
    scripts="__main__.py",
    icon="Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico",
    name=MathPy.__name__,
    version=MathPy.__version__,
    base=base,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    include_package_data=True,
    install_requires=['tkinter', 'matplotlib', 'sympy', 'numpy', 'itertools', 'random'],

    # metadata to display on PyPI
    author=MathPy.__author__,
    author_email="najmi.achraf@gmail.com",
    description="GUI Calculator",
    license="MIT License",
    keywords=['gui', 'executable'],
    url="",  # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/AchrafNajmi/MathPy/issues",
        "Documentation": "https://github.com/AchrafNajmi/MathPy/blob/master/Release%20Notes.txt",
        "Source Code": "https://github.com/AchrafNajmi/MathPy",
    },
    python_requires='>=3.7',
    classifiers=[
        "License :: MIT :: AchrafNajmi/MathPy",
        "License :: OSI Approved :: Python Software Foundation License",
        'Programming Language :: Python :: 3.7',
        "Operating System :: Microsoft :: Windows"
    ]

    # could also include long_description, download_url, etc.
)
