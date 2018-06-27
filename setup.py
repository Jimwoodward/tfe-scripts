from setuptools import setup, find_packages  # noqa: H301
NAME = 'tfe-scripts'
VERSION = '1.0.0'
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
REQUIRES = ['requests']
setup(
    name=NAME,
    version=VERSION,
    description="=descr here",
    author_email="email_here",
    url="",
    keywords=[""],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)