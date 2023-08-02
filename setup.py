from setuptools import setup

setup(
    name='cpmreader',
    version='0.1.0',
    description='A package to read Compumedics polysomnography files',
    url='https://github.com/shuds13/pyexample',
    author='Bastien Lechat',
    license='BSD 3-Clause',
    packages=['cpmreader'],
    install_requires=['numpy',
                      'scipy',
                      'pandas',
                      ]
)