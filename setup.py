import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cisco_support",
    version="0.3.1",
    author="Dennis Roth",
    author_email="rothdennis92@gmail.com",
    description="Python implementation of the Cisco Support APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rothdennis/cisco_support",
    project_urls={
        "Bug Tracker": "https://github.com/rothdennis/cisco_support/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)