from setuptools import setup

_classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Software Development :: Testing'
    ]

setup(
    name="pytest-expect",
    version="1.1.0",
    url="https://github.com/gsnedders/pytest-expect",
    license="MIT License",
    description="py.test plugin to store test expectations and mark tests based on them",
    classifiers=_classifiers,
    maintainer="Geoffrey Sneddon",
    maintainer_email="geoffers@gmail.com",

    install_requires=[
        "pytest",
        "u-msgpack-python"
    ],

    packages=["pytest_expect"],

    entry_points={
        'pytest11': [
            'pytest_expect = pytest_expect.expect',
        ]
    }
)
