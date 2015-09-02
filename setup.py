#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages
import organizations as app


def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return "LONG_DESCRIPTION Error"

setup(
    author="Ben Lopatin + arteria GmbH",
    author_email="ben.lopatin@wellfireinteractive.com",
    name='django-ar-organizations',
    version=app.__version__,
    description='Group accounts for Django',
    long_description=long_description(),
    url='https://github.com/arteria/django-ar-organizations/',
    license='BSD License',
    platforms=['OS Independent'],
    install_requires=open('requirements.txt').read().split('\n'),
    # test_suite='tests.runtests.runtests',
    include_package_data=True,
    packages=find_packages(exclude=["tests.tests", "tests.test_app", "tests"]),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
