# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 3

### 🎈Checkpoint🎈

```bash
git checkout tema3-3
```

### Descripción

Incluimos un script para generar información falsa para un desarrollo.

### Peticiones

```python
from werkzeug.security import generate_password_hash
from models import db, User, Notice, Comment
from faker import Factory
from random import randint

# Spanish
fake = Factory.create('es_ES')

# Reload tables
db.drop_all()
db.create_all()

# Make 100 fake users
for num in range(100):
    profile = fake.simple_profile()
    username = profile['username']
    mail = profile['mail']
    password = generate_password_hash('123')
    # Save in database
    my_user = User(username=username, mail=mail, password=password)
    db.session.add(my_user)

print('Users created')

# Make 1000 fake news
for num in range(1000):
    title = fake.sentence()
    url = fake.uri()
    user_id = randint(1, 100)
    # Save in database
    my_notice = Notice(title=title, url=url, user_id=user_id)
    db.session.add(my_notice)

print('News created')

# Make 10000 fake comments
for num in range(10000):
    text = fake.text()
    notice_id = randint(1, 1000)
    user_id = randint(1, 100)
    # Save in database
    my_comment = Comment(text=text, notice_id=notice_id, user_id=user_id)
    db.session.add(my_comment)

print('Comments created')

# Save
db.session.commit()
```

### Siguiente

[Tema 3 Paso 4](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-4)

### Anterior

[Tema 3 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-2)
