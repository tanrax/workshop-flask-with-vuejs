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

```bash 
from models import db, User
my_user = User()
my_user.username = 'Juana'
my_user.mail = 'juana@arco.fr'
my_user.password = 'noinglaterra'
db.session.add(my_user)
db.session.commit()
```

Listamos todos.

```bash 
from models import db, User
my_users = User.query.all()
```

Obtenemos uno.

```bash 
from models import db, User
my_users = User.query.get(1)
```


Actualizamos.

```bash 
from models import db, User
my_user = User.query.get(1)
my_user.username = 'Simba'
my_user.mail = 'rey@leon.af'
my_user.password = 'Hakuna matata'
db.session.add(my_user)
db.session.commit()
```

Borramos.

```bash 
from models import db, User
my_user = User.query.get(1)
db.session.delete(my_user)
db.session.commit()
```


### Siguiente

[Tema 3 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-2)

### Anterior

[Tema 2 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema2-2)
