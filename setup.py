# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wencaipy',
 'wencaipy.common',
 'wencaipy.core',
 'wencaipy.fund',
 'wencaipy.index',
 'wencaipy.js',
 'wencaipy.stock',
 'wencaipy.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wencaipy',
    'version': '0.3.1',
    'description': '',
    'long_description': None,
    'author': 'romepeng',
    'author_email': 'romepeng@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
