import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PreProcessing",
    version="0.0.1",
    author="Ashutosh Singh",
    author_email="ashutosh71195@gmail.com",
    description="Package for preprocessing image, text and tabular data for ML, DL algorithms",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ),
)

