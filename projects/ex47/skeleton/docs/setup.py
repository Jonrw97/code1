try:
    from setuptools import setup
except ImportError:
      from distutils.core import setuptools

config = {
    'description': 'Ex47',
    'author': 'Jonatha',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
