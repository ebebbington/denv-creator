import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="denv-creator",
    version="0.0.1",
    author="Edward Bebbinngton",
    author_email="EdwardSBebbington@hotmail.com",
    description="Simple python script to create every file and configurations for multiple docker containers ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebebbington/denv-creator",
    packages=setuptools.find_packages(),
    scripts=['./denv-creator/index'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)