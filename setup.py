import os

from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    # Application name:
    name="PI",

    # Version number (initial):
    version="0.1",

    # Application author details:
    author="Sergio Casas",
    author_email="sdcasas@gmail.com",

    # Details
    url="https://github.com/sdcasas/pi.git",

    # Packages
    # packages=["app"],
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Parque Informático",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        'Django >=1.11',
    ],

    long_description=README,

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)