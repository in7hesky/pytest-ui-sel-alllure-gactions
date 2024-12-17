# pytest-ui-sel-allure-actions
### Project Description ###

A pytest-selenium-allure framework wrapped in a docker container with github-actions integration.

System Under Test (SUT): - https://demos.bellatrix.solutions/. 

List of main tools and libraries used:

- pytest
- pytest-xdist
- selenium
- allure-pytest
- docker-compose
- github-actions workflow

## 1. Prerequisites
For local test run make sure you have installed:
- pyenv / python interpreter (the tested version can be found in `.python-version` file)
- Chrome / Firefox browser
- [Optional] Allure (2.32.0 tested) to generate reports manually. See https://allurereport.org/docs/ \
  for installation guidance

## 2. Running tests locally
### 2.1 Installing
Just `git clone` the repo to any desired location, `cd` to it and run the following (Linux):
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Done.
#### 2.2 Executing run command
Being in the project's `root` directory you may just execute:
```
pytest
```
The tests will be executed in **Chrome** and in **parallel** by default. The defaults for the command are set in `pyproject.toml`.

You may also supply some flags to change the default behaviour. To run the tests in `Firefox` and in `headless` mode, execute:
```
pytest --browser firefox --headless
```
_Note that the tests running in Firefox will fail! The reason for it is the SUT's design itself._

Furthermore, `pytest-xdist` flags can be used to change the workers count, like that:
```
pytest -n 8
```
Though the number is set to `auto` by default.
#### 3. Generating the report
Now you may proceed with generating an **allure report**. To do this, specify the path to the report's directory:
```
allure serve allure-results
```
Again, the location is set in `pyproject.toml` and can be overwritten before test run.
### Extra Notes:
_Although the docker files seem a bit redundant (mostly because my initital run strategy was more complicated before I've found some better solutions) I decided to leave it as it is because this implementation feels potentially more scalable._
