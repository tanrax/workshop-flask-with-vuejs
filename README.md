# Taller de API Rest con Flask y VueJS en armonia

## Tema 3 - Paso 5

### 🎈Checkpoint🎈

```bash
git checkout tema3-5
```

### Descripción

Terminamos de definir todos los esquemas y creamos un simple CRUD de noticias.

### Peticiones

#### GET

```bash
http GET localhost:5000/api/v1/user
```

```bash
http GET localhost:5000/api/v1/user/{id}
```

```bash
http GET localhost:5000/api/v1/notice
```

```bash
http GET localhost:5000/api/v1/notice/{id}
```

```bash
http GET localhost:5000/api/v1/notice/{id}/comments
```

#### POST

```bash
http POST localhost:5000/api/v1/notice
```

```bash
http POST localhost:5000/api/v1/notice/{id}/comments
```

#### PATCH

```bash
http PATCH localhost:5000/api/v1/notice/{id}
```

#### DELETE

```bash
http DELETE localhost:5000/api/v1/notice/{id}
```



### Siguiente

[Tema 4 Paso 1](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-1)

### Anterior

[Tema 3 Paso 4](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-4)
