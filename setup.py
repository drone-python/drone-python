import re
from setuptools import setup, find_packages


with open('drone/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name="drone",
    version=version,
    author="Greg Taylor",
    author_email="gtaylor@gc-taylor.com",
    description="Drone CI plugin utilities and HTTP API client",
    long_description=open('README.rst').read(),
    license="MIT License",
    keywords="drone ci test plugin api",
    url='https://github.com/drone/drone-python',
    install_requires=['future'],
    entry_points={
        'console_scripts': [
            'create-drone-py-plugin = drone.cli.plugin_creator:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={'': ['LICENSE', '*.txt', '*.rst']},
    tests_require=['nose'],
    test_suite='nose.collector',
)
