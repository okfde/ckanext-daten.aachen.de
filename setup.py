from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-aachen_theme',
    version=version,
    description="Theme for daten.aachen.de",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Matt Fullerton',
    author_email='matt.fullerton@okfn.de',
    url='http://www.okfn.de',
    license='MIT License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.aachen_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        aachen_theme=ckanext.aachen_theme.plugin:AachenThemePlugin
    ''',
)
