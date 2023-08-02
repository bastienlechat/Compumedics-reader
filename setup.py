from setuptools import setup

setup(
    name='cpmreader',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Bastien Lechat',
    author_email='shudson@anl.gov',
    license='BSD 2-clause',
    packages=['cpmreader'],
    install_requires=['numpy',
                      'scipy',
                      'pandas',
                      ]
)