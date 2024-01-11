# codewars
codewars exercises


## Setting up Python env
```
python3 -m venv .venv
```

Activate the enviornment
```
source .venv/bin/activate
```

Freeze your requirements
``` 
pip freeze > requirements.txt
```

Install the requirements
```
pip install -r requirements.txt
```

Deactivate the enviornment
```
deactivate
```

## Codewars Testing framework install
If you need the testing framework.

```
pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test
```