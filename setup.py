#!/usr/bin/env python
import io
import os
import re
import shutil
import sys
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = find_version('src', 'autogluon_contrib_nlp', '__init__.py')

"""
To release a new stable version on PyPi, simply tag the release on github, 
and the Github CI will automatically publish 
a new stable version to PyPi using the configurations in 
.github/workflows/pypi_release.yml . 
You need to increase the version number after stable release, 
so that the nightly pypi can work properly.
"""
try:
    if not os.getenv('RELEASE'):
        from datetime import date
        today = date.today()
        day = today.strftime("b%Y%m%d")
        VERSION += day
except Exception:
    pass


requirements = [
    'numpy',
    'sacremoses>=0.0.38',
    'yacs>=0.1.6',
    'sacrebleu',
    'flake8',
    'regex',
    'contextvars',
    'pyarrow',
    'tokenizers>=0.7.0,<0.9.0',
    'protobuf',
    'sentencepiece',
    'pandas'
]

MODEL_ZOO_CHECKSUM_PATH = os.path.join('models',
                                       'model_zoo_checksums', '*.txt')

setup(
    # Metadata
    name='autogluon-contrib-nlp',
    version=VERSION,
    python_requires='>=3.6',
    author='GluonNLP Toolkit Contributors',
    author_email='gluonnlp-dev@amazon.com',
    description='MXNet GluonNLP Toolkit (DeepNumpy Version)',
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    url='https://github.com/sxjscience/autogluon-contrib-nlp',
    # Package info
    packages=find_packages(where="src", exclude=(
        'tests',
        'scripts',
    )),
    package_dir={"": "src"},
    package_data={'': [os.path.join('models', 'model_zoo_checksums', '*.txt')]},
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'extras': [
            'boto3',
            'tqdm',
            'jieba',
            'subword_nmt',
            'youtokentome>=1.0.6',
            'spacy>=2.0.0',
            'fasttext>=0.9.2',
            'langid',
            'nltk',
            'h5py>=2.10',
            'scipy',
            'tqdm'
        ],
        'dev': [
            'pytest',
            'pytest-env',
            'pylint',
            'pylint_quotes',
            'flake8',
            'recommonmark',
            'sphinx-gallery',
            'sphinx_rtd_theme',
            'mxtheme',
            'sphinx-autodoc-typehints',
            'nbsphinx',
            'flaky',
        ],
    },
)
