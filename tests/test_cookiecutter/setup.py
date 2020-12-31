from setuptools import find_packages
from setuptools import setup


setup(
    name='sample',
    version='0.1.0',
    description='A sample Python library',
    author='Jamal Mustafa',
    author_email='jimustafa@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'tqdm',
    ],
)
