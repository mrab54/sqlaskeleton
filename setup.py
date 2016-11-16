from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

config = {
    'description': 'SqlASkeleton',
    'author': 'Mike Rabas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': [],
    'packages': find_packages(),
    'scripts': [],
    'name': 'sqlaskeleton',
    'entry_points': {'console_scripts': ['sqlaskeleton=sqlaskeleton.__main__:main', ]}
}

setup(**config)
