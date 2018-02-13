# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 1

### 🎈Checkpoint🎈

```bash
git checkout tema3-1
```

### Descripción

Conectamos la base de datos con Flask con Flask-SQLAlchemy

### Peticiones

Creamos un usuario.

```python 
from models import db, User
my_user = User()
my_user.username = 'Juana'
my_user.mail = 'juana@arco.fr'
my_user.password = 'noinglaterra'
db.session.add(my_user)
db.session.commit()
```

Listamos todos.

```python 
from models import db, User
my_users = User.query.all()
```

Obtenemos uno.

```python 
from models import db, User
my_users = User.query.get(1)
```


Actualizamos.

```python 
from models import db, User
my_user = User.query.get(1)
my_user.username = 'Simba'
my_user.mail = 'rey@leon.af'
my_user.password = 'Hakuna matata'
db.session.add(my_user)
db.session.commit()
```

Borramos.

```python 
from models import db, User
my_user = User.query.get(1)
db.session.delete(my_user)
db.session.commit()
```

Definición de tablas.

```python 
class User(db.Model):
    '''
    Table user
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    mail = db.Column(db.String(200))
    password = db.Column(db.String(106))

    def __repr__(self):
        return '<User Table {0}>'.format(self.username)
```

```python 
db.create_all()
```

### Siguiente

[Tema 3 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-2)

### Anterior

[Tema 2 Paso 3](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema2-3)
