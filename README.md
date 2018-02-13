# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 2

### 🎈Checkpoint🎈

```bash
git checkout tema3-2
```

### Descripción

Implementamos un sistema de migraciones.

### Peticiones

#### Flask-migrate

models.py

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
```

Iniciamos.

```python
python3 models.py db init
```

Creamos migración.

```python
python3 models.py db migrate
```

Actualizamos la base de datos.

```python
python3 models.py db upgrade
```

#### Flask-script

```python
from flask_script import Manager

from myapp import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()
```

```python
python3 manage.py hello
```

### Siguiente

[Tema 3 Paso 3](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-3)

### Anterior

[Tema 3 Paso 1](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-1)
