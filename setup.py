'''
Created on 5 Mar 2010

@author: oppianmatt
'''

# hook to find setup tools if not installed
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "django-defaultsite",
    version = "1.0",
    packages = [
        'defaultsite',
    ],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    
    # metadata for upload to PyPI
    author = "Oppian",
    author_email = "matt@oppian.com",
    description = "django-defaultsiteSets the Site object in django to something better then example.com.",
    license = "MIT",
    keywords = "django site example.com",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    url = "http://oppian.com/labs/django-defaultsite/",   # project home page, if any
)

