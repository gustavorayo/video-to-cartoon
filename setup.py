from setuptools import setup, find_packages
import os


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='art-fid',
      version='0.0.1',
      author='Gustavo Rayo',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['pycli = pycli.__main__:main']
      },
      install_requires=['numpy>=1.19.5'],
      python_requires='>=3.8')