from pathlib import Path
from setuptools import setup, find_packages
from floop.main import __version__ as version


long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name='floop',
    author="Max Richmond",
    version=version,
    packages=find_packages(),
    python_requires=">=3.9",
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='security detection',
    install_requires=[
        'panther_sdk>=0.0.19',
        'panther_utils>=0.2.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Typing :: Typed',
        'Programming Language :: Python :: 3',
    ]
)
