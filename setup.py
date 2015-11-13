from setuptools import setup, find_packages


setup(
    name="drone",
    version="0.1",
    author="Greg Taylor",
    author_email="gtaylor@gc-taylor.com",
    description="Drone CI plugin utilities and HTTP API client",
    long_description=open('README.rst').read(),
    license="MIT License",
    keywords="drone ci test plugin api",
    url='https://github.com/gtaylor/drone-python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={'': ['*.txt', '*.rst']},
    tests_require=['nose'],
    test_suite='nose.collector',
)
