[
![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)
![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)
![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)
](https://pypi.org/project/ask_schools/)
[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)

<hr/>

## Top 10 downloads on odesi 

<p>
Will connect to ODESI database and retrieve the top 10 survey downloaded for the last month. It will create a JSON file containings those downloads.We can also parse the JSON file to create a RSS Feed see ```Flask_app.py```.
</p>

## Installation & Usage

**need credentials to connect to db** need a secrets.json file

```python 
#using poetry
pip install poetry
poetry run python top_downloads.py
```

To run an example of the app
```python 
poetry run python Flask_app.py
```

## Screenshots
This is an example of the app using data in downloads.json
<p float="left">
    <img src="screenshots/screenshot.png" width="700"/>
</p>

### coverage
```
Name                         Stmts   Miss  Cover
------------------------------------------------
Flask_app.py                    38     38     0%
initialization.py               47     47     0%
odesi/__init__.py                0      0   100%
odesi/odesi_queries.py           4      0   100%
odesi/query_helper.py           30      6    80%
odesi/sp_utils.py               11      2    82%
odesi_tables.py                117    117     0%
tests/__init__.py                0      0   100%
tests/test_odesi_report.py      81      2    98%
top_downloads.py                27     10    63%
------------------------------------------------
TOTAL                          355    222    37%
```

### TODO
1. Add Docker
2. Gitlab CI
3. Change repo name to 'odesi_reports'