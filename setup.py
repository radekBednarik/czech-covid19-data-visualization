from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="czech-covid19-data-visualization",
    version="0.0.1",
    author="Radek 'bednaJedna' Bednarik",
    author_email="bednarik.radek@gmail.com",
    description="Visualization of Czech official COVID 19 data provided by Ministry of Health API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/radekBednarik/czech-covid19-data-visualization",
    packages=find_packages(),
    install_requires=[
        "dash",
        "pandas",
        "czech-covid19-data-api",
        "dash-bootstrap-components",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": ["visualizer=czech_covid19_data_visualization.app:main"]
    },
)