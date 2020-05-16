[
![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)
![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)
![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)
](https://pypi.org/project/ask_schools/)
[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)

<hr/>
### top 10 odesi downloads

<p>
Will connect to ODESI database and retrieve the top 10 survey downloaded during the previous month. It will create a JSON file containings those downloads.
</p>

## Usage


**need credentials to connect to db** need a secrets.json file

```python 
#using poetry
pip install poetry
poetry run python top_downloads.py
```
To run an example of the app
```python 
python app.py
```

## Screenshots
This is a mockup, it will only send if one of the services has been down for at least 10 minutes
<p float="left">
    <img src="screenshots/screenshot.png" width="200"/>
</p>



### TODO
1. Add Docker