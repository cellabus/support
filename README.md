support.cellabus.com
====================

Support website for Cellabus.  This will be a simple Q/A site based on Flask
with data exported from Uservoice.

Layout
------

The plan is that this will contain an index page of questions grouped by
section.  Each question will be a link to a page with the question/answer.

Architecture
------------

This is based on [base-flask](https://github.com/albertyw/base-flask).  It will
serves data from the various articles as simple HTML templates.

Development
-----------

With virtualenvwrapper:
```bash
mkvirtualenv app -p python3.5
pip install -r requirements.txt
ln -s .env.development .env
python app/serve.py
```

Testing
-------

```bash
pip install -r requirements-test.txt
cd app
coverage run -m unittest discover
```

Production
----------

```bash
ln -s .env.production .env
bin/setup.sh
```
