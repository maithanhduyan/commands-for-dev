#### Create new venv on Windows
> py -3 -m venv venv
> venv\Scripts\activate

> pip install -r requirements.txt

> python app.py

## Clear Cache
~~~
python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

~~~