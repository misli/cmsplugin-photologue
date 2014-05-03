# encoding: utf-8

from distutils.core import setup

setup(
    name             = 'cmsplugin_photologue',
    version          = '1.0',
    description      = 'Simple Django CMS plugin for including photos and galleries from Photologue in Your pages',
    long_description = 'Simple Django CMS plugin for including photos and galleries from Photologue in Your pages',
    author           = 'Jakub Dorňák',
    author_email     = 'jdornak@redhat.com',
    license          = 'BSD',
    url              = 'https://github.com/misli/cmsplugin-photologue',
    packages         = ['cmsplugin_photologue'],
    package_data     = {'cmsplugin_photologue': ['templates/*']},
)
