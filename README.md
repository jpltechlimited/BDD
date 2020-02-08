## Check and upgrade pip version
```
pip --version
pip install --upgrade pip
```
## Check and install virtualenv
```
pip install --user virtualenv
```
## Create virtual environment
```
virtualenv .env
```
## Set virtual environment variables
```
edit .env\Scripts\activate script:
set d365.browser=
set d365.username=
set d365.password=
set d365.mainUrl=
```
## Activate virtual environment and install requirements
```
.env\Scripts\activate
pip install -r requirements.txt
```
## Running verbose behave tests
```
behave --no-capture --no-capture-stderr --no-logcapture
```