import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv2dictionary",
    version="0.0.2",
    author="Cole Malphrus",
    author_email="cole@malphrus.tech",
    description="converts csv to a dictionary",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/colemalphrus/csv2dictionary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)