# czech COVID19 data visualization
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Visualization of Czech official COVID 19 data provided by Ministry of Health API.

## What's you need to get it going

- Python 3.6+ with pip
- ... and that's about it
- it may be good to use virtualenv when installing this to keep all those packages separate. In that case, install `pip install pipenv` then run `pipenv --python 3.8` (or version you have installed on you computer) when thats done run `pipenv shell` and in the virtual env finally install this package - see below.

## How to use
Here's how to get it going on your machine:

- clone the repo

    ```
    git clone https://github.com/radekBednarik/czech-covid19-data-visualization.git
    ```

- get in to the root of this project and run:

    ```
    python setup.py install

    ```

- then run:

    ```
    python app_runner.py
    ```

- copy URL diplayed int the console into your browser and that's it.