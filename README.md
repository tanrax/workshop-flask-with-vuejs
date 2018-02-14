# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 4

### 🎈Checkpoint🎈

```bash
git checkout tema3-4
```

### Descripción

Convertimos nuestras consultas a la base de datos en JSON.

### Peticiones

```python
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'mail')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@api.route(PRE_URL + 'user')
class UserList(Resource):

    def get(self):
        all_users = User.query.all()
        return users_schema.jsonify(all_users)


@api.route(PRE_URL + 'user/<int:id>')
class UserSingle(Resource):

    def get(self, id):
        my_user = User.query.get(id)
        if my_user:
            return user_schema.jsonify(my_user)
        else:
            return {'message': 'No existe el usuario'}, 400
```

```python
http GET :5000/api/v1/user/2
```

```python
http GET :5000/api/v1/user
```

### Siguiente

[Tema 3 Paso 4](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-4)

### Anterior

[Tema 3 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-2)
