import os
import re

from setuptools import find_packages, setup


root = os.path.dirname(__file__)
with open(os.path.join(root, 'yhttp_ssr_boilerplate', 'manifest.py')) as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(
        f.read(),
    ).group(1)

setup(
    name='yhttp-ssr-boilerplate',
    version=version,
    description='A server-side-rendered YHTTP starter application.',
    packages=find_packages(where='.', exclude=['tests']),
    package_data={
        'yhttp_ssr_boilerplate': ['templates/**/*.mako'],
    },
    install_requires=[
        'yhttp >= 9.4.2, < 10',
        'yhttp-mako >= 3.1, < 4',
        'yhttp-auth >= 11.1, < 12',
        'yhttp-dbmanager >= 9.1, < 10',
        'yhttp-media >= 4.1, < 5',
        'yhttp-sqlalchemy >= 6.1, < 7',
    ],
    entry_points={
        'console_scripts': [
            'yhttp-ssr-boilerplate = yhttp_ssr_boilerplate:app.climain',
        ],
    },
    python_requires='>=3.11',
)
