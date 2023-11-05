# omd
Homeworks of Python course in Avito Academy Analytics
</br>

### Issues on tests
#### Issue 1
Morse encoder test using ***doctest***
How to test the function from the root directory
```bash
python -m doctest testing/testing_encode.py
```
Above command does not output anything if tests are correct
You can add **-v** for verbose output to see info even if tests are correct
```bash
python -m doctest -v testing/testing_encode.py
```
To check if the last test works correct, we can add ***doctest*** flag  as follows
```bash
python -m doctest -v -o NORMALIZE_WHITESPACE testing/testing_encode.py
```

#### Issue 2
Morse decoder test using ***pytest.mark.parametrize***
How to test the function from the root directory
```bash
python -m pytest testing/testing_decode.py
```
To get more info on the tests, we can **-v** for verbose
```bash
python -m pytest -v testing/testing_decode.py
```

#### Issue 3
One Hot Encoder function test using ***unittest***
How to test the function from the root directory
```bash
python -m unittest testing/testing_ohe_unit.py
```
To get more info use **-v**
```bash
python -m unittest -v testing/testing_ohe_unit.py
```

#### Issue 4
One Hot Encoder function test using ***pytest***
How to test the function from the root directory
```bash
python -m pytest testing/testing_ohe_pytest.py
```
To get more info use **-v**
```bash
python -m pytest -v testing/testing_ohe_pytest.py
```

#### Issue 5
What year function test using ***unittest.mock***
How to test the function from the root directory
```bash
python -m unittest testing/testing_year_mock.py
```
Use **-v** to get more verbose output
```bash
python -m unittest -v testing/testing_year_mock.py
```
To obtain coverage report, we need to use ***coverage*** package
```bash
coverage run -m unittest -v testing/testing_year_mock.py
coverage html
```
</br>