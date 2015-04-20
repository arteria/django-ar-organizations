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
    url='https://github.com/wellfire/django-organizations/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=1.4',
        'django-extensions>=0.9',
        'django-compat>=1.0.2',
        'jsonfield>=1.0.3',
    ],
    # test_suite='tests.runtests.runtests',
    include_package_data=True,
    packages=find_packages(exclude=["tests.tests", "tests.test_app", "tests"]),
    zip_safe=False
)
