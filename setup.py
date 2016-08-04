from setuptools import setup
from setuptools.extension import Extension



with open('base/VERSION') as version_file:
    version = version_file.read().strip()

def readme():
    with open('base/README.rst') as f:
        return f.read()

extensions = [
    Extension(
        "base/cythonfile",
        ["base/cythonfile.c"]
    )
]

setup(name='base',
      version=version,
      description='a package',
      long_description=readme(),
      url='https://github.com/markm541374/base',
      author='markm541374',
      license='MIT',
      packages=['base'],
      package_dir={'base':'base'},
      package_data={'base':['data/*','VERSION','README.rst']},
      ext_modules= extensions,
      zip_safe=False)
