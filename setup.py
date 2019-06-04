# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name            = 'cmsplugin-photologue',
    version         = '1.1.0',
    description     = 'django CMS plugin for including photos and galleries from Photologue',
    author          = 'Jakub Dorňák',
    author_email    = 'jakub.dornak@misli.cz',
    license         = 'BSD',
    url             = 'https://github.com/misli/cmsplugin-photologue',
    packages        = find_packages(),
    include_package_data = True,
    install_requires = [
        'django-cms',
    ],
    classifiers     = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Czech',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
