# Taller de API Rest con Flask y VueJS en armonia

![Flask y Vuejs](flaskyvuejs.jpg)

## Necesitaremos

- Portátil, y tuyo.
- Python 3.5> 
- Internet superior a 56k
- Editor de texto enriquecido y con fundamento.
- [httpie](https://httpie.org/)
- [pipenv](https://docs.pipenv.org/)

## ¿Bibliotecas?

### Microframework Web

- **Flask**

### Base de datos

- **Flask-SQLAlchemy**: ORM
- **Flask-Migrate**: Añade herramientas para gestionar nuestra base de datos.
- **Flask-Script**: Creación de comandos personalizados
- **Faker**: Generador de información falsa

### API Rest

- **Flask-restplus**: Nos ayuda con las peticiones y autodocumentación
- **Flask-JWT**: Identificación básica.
- **Flask-marshmallow**: Convertirá los objetos ORM en JSON.

### Herramientas de desarrollo

- **httpie**: Cliente de API Rest para pruebas.
- **python-dotenv**: Implementación de un archivo de configuración.

### Instalación

```bash
pipenv install flask Flask-SQLAlchemy Flask-Migrate Flask-script Faker 
```


## Peticiones

### GET

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

### POST

```bash
http GET localhost:5000/api/v1/notice
```

```bash
http GET localhost:5000/api/v1/notice/{id}/comments
```

### PATCH

```bash
http GET localhost:5000/api/v1/notice/{id}
```

### DELETE

```bash
http GET localhost:5000/api/v1/notice/{id}
```
