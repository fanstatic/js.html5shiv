from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '3.7.4.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'html5shiv', 'test_html5shiv.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.html5shiv',
    version=version,
    description="Fanstatic packaging of html5shiv",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    url='https://bitbucket.org/fanstatic/js.html5shiv',
    license='BSD',
    packages=find_packages(),namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'html5shiv = js.html5shiv:library',
            ],
        },
    extras_require={
        'testing': [
            'setuptools-hg',
            'pytest',
            'tox',
            ],
        },
    )

