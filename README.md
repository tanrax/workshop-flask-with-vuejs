# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 6

### 🎈Checkpoint🎈

```bash
git checkout tema3-5
```

### Descripción

Nos identificamos y protegemos algunas rutas.

### Peticiones

#### Nos Identificamos

Buscamos un nombre de usuario.

```bash
http GET :5000/api/v1/user/1
```

Y nos identificamos con el mail y la contraseña *123*.

```bash
http POST :5000/api/v1/auth mail=wserra@hotmail.com password=123
```

Nos devolverá un token

``` json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjAxMDE0MzgsImlhdCI6MTUyMDEwMTEzOCwibmJmIjoxNTIwMTAxMTM4LCJpZGVudGl0eSI6MX0.bi_u1j_YqpUZ4uwHv8k5p1Vof1AIfTYPU75dYj7oZEI"
}
```

Ya tenemos nuestro token para identificarnos. De una ruta que hemos protegido, vamos a dar nuestro token y para que nos devuelva lo que necesitamos.

``` bash
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjAxMDE0MzgsImlhdCI6MTUyMDEwMTEzOCwibmJmIjoxNTIwMTAxMTM4LCJpZGVudGl0eSI6MX0.bi_u1j_YqpUZ4uwHv8k5p1Vof1AIfTYPU75dYj7oZEI" localhost:5000/api/v1/user
```

### Siguiente

[Tema 4 Paso 1](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-1)

### Anterior

[Tema 3 Paso 5](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-5)
