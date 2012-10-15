from setuptools import setup, find_packages
setup(
    name='SimplePassphrase',
    version='0.1.0',
    author='Byron D Peebles',
    author_email='byron.peebles@gmail.com',
    packages = find_packages(),
    scripts=['bin/dicewords'],
    url='http://github.org/bpeebles/simple_passphrase',
    license='LICENSE.txt',
    description='Very simple passphrase generation, with a simple Diceware implementation that tries to use good numberss',
    long_description=open('README.rst').read(),
    install_requires=[
        'argparse',
    ],
    package_dir={'simple_passphrase': 'simple_passphrase'},
    package_data={'simple_passphrase': ['words/*.txt']},
)
