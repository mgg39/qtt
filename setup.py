import os
import platform
import re
from pathlib import Path

from setuptools import find_packages, setup


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


def get_version(verbose=1, filename='src/qtt/version.py'):
    """ Extract version information from source code """

    with open(filename) as f:
        ln = f.readline()
        m = re.search('.* ''(.*)''', ln)
        version = (m.group(1)).strip('\'')
    if verbose:
        print('get_version: %s' % version)
    return version


def get_package_data(root_dir):
    """ Gather directories under root_dir with files in it """
    package_data = []
    for root_dir, dirs, files in os.walk(root_dir):
        if len(files) > 0:
            package_data.append(f'{os.path.join(Path(*Path(root_dir).parts[2:]), "*")}')
    return package_data


tests_require = ['coverage', 'jupyter', 'mypy', 'types-redis', 'types-python-dateutil', 'pytest']

install_requires = [
    'apscheduler', 'attrs', 'dulwich', 'h5py', 'IPython>=0.1', 'jupyter', 'lmfit', 'matplotlib>=3.0',
    'numdifftools', 'numpy>=1.15', 'opencv-python', 'pandas', 'PyQt5', 'pyqtgraph', 'pyvisa', 'pyzmqrpc', 'qcodes>=0.23.0',
    'qcodes-contrib-drivers', 'qilib', 'qiskit-terra>=0.19', 'qtpy', 'qupulse', 'redis', 'scipy', 'scikit-image',
    'shapely', 'sympy', 'imageio'
] + tests_require

if platform.system() == 'Windows':
    install_requires.append('pywin32')

rtd_requires = [
    'sphinx>=1.7', 'sphinx_rtd_theme', 'nbsphinx', 'sphinx-automodapi', 'sphinx_copybutton'
]

extras_require = {"rtd": rtd_requires}

setup(name='qtt',
      version=get_version(),
      use_2to3=False,
      author='Pieter Eendebak',
      author_email='pieter.eendebak@tno.nl',
      maintainer='Pieter Eendebak',
      maintainer_email='pieter.eendebak@tno.nl',
      description='Python-based framework for analysis and tuning of quantum dots',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://qutech.nl',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Scientific/Engineering'
      ],
      license='MIT',
      package_dir={'': 'src'},
      packages=find_packages(where='./src', exclude=["*tests*"]),
      package_data={'qtt': get_package_data('src/qtt/exampledata')},
      data_files=[],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=extras_require,
      zip_safe=False,
      )
