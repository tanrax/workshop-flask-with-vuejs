# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 6

### 🎈Checkpoint🎈

```bash
git checkout tema3-6
```

### Descripción

Nos identificamos y protegemos algunas rutas.

### Peticiones

#### Nos Identificamos

Buscamos un nombre de usuario.

```bash
http GET :5000/api/v1/user/1
```

Con cualquiera de ellos nos vamos a identificar en nuestra API. Usamos un correo cualquiera y la contraseña *123*.

```bash
http POST :5000/api/v1/auth mail=wserra@hotmail.com password=123
```

Nos devolverá un token.

``` json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjAxMDE0MzgsImlhdCI6MTUyMDEwMTEzOCwibmJmIjoxNTIwMTAxMTM4LCJpZGVudGl0eSI6MX0.bi_u1j_YqpUZ4uwHv8k5p1Vof1AIfTYPU75dYj7oZEI"
}
```

Este conjunto de letras alfanuméricas nos identifica dentro del API. Cada vez que necesitemos entrar en una zona protegida, usaremos el token.

Si ahora intentas listar todos los usuarios no te dejará.

```bash
http GET :5000/api/v1/user/
```

A no ser que uses tu token.

``` bash
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjAxMDE0MzgsImlhdCI6MTUyMDEwMTEzOCwibmJmIjoxNTIwMTAxMTM4LCJpZGVudGl0eSI6MX0.bi_u1j_YqpUZ4uwHv8k5p1Vof1AIfTYPU75dYj7oZEI" localhost:5000/api/v1/user
```

Para lograr la integración de JWT se ha modificado **app.py**. Primero se ha importado las bibliotecas.

``` python
from flask_jwt import JWT, jwt_required, current_identity
```

Después lo hemos configurado.

``` python
# Por defecto usa Username y Password para la identificación, en su lugar le decimos que usaremos Mail y Password
app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
# Le configuramos la duración del token. En este caso le he dicho que dure 30 días.
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
# La ruta para identificarse. Por defecto sería '/auth/', y aquí le digo '/api/v1/auth/'
app.config['JWT_AUTH_URL_RULE'] = PRE_URL + 'auth'
```

Luego lo conectamos con la base de datos.

``` python
# =========================
# Authenticate
# =========================
def authenticate(mail, password):
    # POST /auth
    my_user = User.query.filter_by(mail=mail).first()
    if my_user and check_password_hash(
            my_user.password,
            password):
        return my_user
    else:
        return None


def identity(payload):
    return User.query.get(payload['identity'])


jwt = JWT(app, authenticate, identity)
```

En estos momentos hemos blindado la ruta para ver todos los usuarios (/api/v1/user). Solo hemos usado un **decorador especial de jwt** que antes hemos importado.

``` python
@jwt_required()
```

En nuestro código quedaría de la siguiente forma.

``` python
# User
@api.route(PRE_URL + 'user')
class UserList(Resource):

    @jwt_required()
    def get(self):
        all_users = User.query.all()
        return users_schema.jsonify(all_users)
```


### Siguiente

[Tema 3 Paso 7](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-7)

### Anterior

[Tema 3 Paso 5](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-5)
