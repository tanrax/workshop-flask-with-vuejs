# Taller de API Rest con Flask y VueJS en armonia

![Flask y Vuejs](flaskyvuejs.jpg)

## Indice
- Tema 1: Flask
    - [1-1 Hola Flask](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema1-1)
    - [1-2 Hola API Rest](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema1-2)
    - [1-3 Preparamos proyecto](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema1-3)
- Tema 2: API Rest
    - [2-1 Hola Flask-restplus](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema2-1)
    - [2-2 Primeras llamadas](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema2-2)
    - [2-3 Completamos las peticiones](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema2-3)
- Tema 3: Base de datos
    - [3-1 ORM con SQLAlchemy](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-1)
    - [3-2 Migraciones](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-2)
    - [3-3 Generando información para desarrollo](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-3)
    - [3-4 Esquemas para crear JSONs](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-4)
    - [3-5 CRUD y definiciones finales](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema3-5)
- Tema 4: Vue-cli
    - [4-1 Hola Vue-cli](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-1)
    - [4-2 Plantilla HTML](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-2)
    - [4-3 Vue-resource: Peticiones desde VueJS](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-3)
    - [4-4 Guardamos un dato nuevo](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-4)
    - [4-5 Segunda página y rutas con vue-router](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-5)
    - [4-6 Compilamos e integramos con Flask](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-6)
    - [4-7 Finalizamos el proyecto](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-7)

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
- **Flask-CORS**: Nos permitirá peticiones desde el exterior.

### Herramientas de desarrollo

- **httpie**: Cliente de API Rest para pruebas.
- **python-dotenv**: Implementación de un archivo de configuración.

### Instalación

Si estas en Debian/Ubuntu, antes necesitarás.

```bash
sudo apt-get install python3-venv
```

¡Ahora sí!

```bash
python3 -m venv
source venv/bin/activate
git clone git@github.com:tanrax/workshop-flask-with-vuejs.git
cd workshop-flask-with-vuejs
pip3 install -r requirements.txt
```

## Peticiones objetivo

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
http POST localhost:5000/api/v1/notice
```

```bash
http POST localhost:5000/api/v1/notice/{id}/comments
```

### PATCH

```bash
http PATCH localhost:5000/api/v1/notice/{id}
```

### DELETE

```bash
http DELETE localhost:5000/api/v1/notice/{id}
```

## ¿Empezamos?

[Tema 1 Paso 1](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema1-1)

## ¡Pista para programadores!

Para seguir el taller sin perderte puedes ir saltando a los 🎈checkpoints🎈 de la siguiente manera.

```bash
git checkout tema1-1
```


