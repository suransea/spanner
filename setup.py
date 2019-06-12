# coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrcode-spanner",
    version="0.0.1",
    author="sea",
    author_email="simpleslight@icloud.com",
    description="A qrcode command line tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0',
    url="https://github.com/suransea/spanner",
    packages=setuptools.find_packages(),
    install_requires=[
        'qrcode', 'pillow', 'image', 'pyscreenshot', 'zxing'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    entry_points={
        'console_scripts': [
            'spanner=qrcode_spanner.spanner:main',
        ]
    },
)
