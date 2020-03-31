from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='my-commons',
    version='0.1.0',
    author='Andreas Verleysen',
    author_email='andreas.verleysen@gmail.com',
    packages=['commons'],
    license='LICENSE.txt',
    description='Functionality I keep on rewriting',
    long_description=open('README.md').read(),
    install_requires=requirements,  # this is required because we want to pip install from git which will not read the requirements.txt file
)
