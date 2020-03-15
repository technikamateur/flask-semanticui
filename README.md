# Flask-Semantic-UI

### Build status
[![Build Status](https://travis-ci.com/technikamateur/flask-semanticui.svg?token=Wquo1zyY6o7zisYoQDTw&branch=master)](https://travis-ci.com/technikamateur/flask-semanticui)

### About
This simple extension adds Semantic UI support to your Flask project. It has currently no support for WTForms. This will come in a later version. But you can all semantic UI features, like icons, animations, ... You name it.

Based on [Semantic UI v2.4.1](https://github.com/Semantic-Org/Semantic-UI-CSS).

### How to use
Your `__init__.py` file should be something like this:
```python
from flask_semanticui import SemanticUI

...

def create_app():
    app = Flask(__name__)
    SemanticUI(app)

...
```
You can also take a look at the `sample.py`. Maybe it will help, but I think it's pretty easy.

### License
This work is licensed under GPLv3. See `LICENSE.txt` for details.
