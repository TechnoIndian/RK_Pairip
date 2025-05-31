import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RK_Pairip",
    version="3.0",
    author="RK_TECHNO_INDIA",
    author_email="TechnoIndia555@gmail.com",
    description="Recover String & Remove Pairip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Technoindian/RK_Pairip",
    keywords='RKPairip',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'RKPairip=RKPairip.__main__:RK_Techno_IND',
        ],
    },
)
