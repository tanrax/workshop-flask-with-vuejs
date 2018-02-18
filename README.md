# Taller de API Rest con Flask y VueJS en armonia

## Tema 4 - Paso 6

### 🎈Checkpoint🎈

```bash
git checkout tema4-6
```

### Descripción

Compilamos VueJS y lo integramos con Flask

### Peticiones

Primero compilamos VueJS

```bash
npm run build
```

Nos creará una carpeta llamada **dist**.

Copiamos *index.html* dentro de una carpeta llamada *templates*, y *static* lo copiamos a la raíz de nuestro proyecto.

Solo nos queda servir los nuevos archivos. Creamos un archivo llamado **web.py**. Y dentro pegamos.

```python
# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
from flask import Flask, render_template

# =========================
# Extensions initialization
# =========================
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
```

Lo ejecutamos.

```bash
python3 web.py
```

Y no olvidemos de mantener levando el API.

```bash
python3 app.py
```

En nuestro navegador favorito, abrimos una pesataña con la siguiente dirección.

```bash
localhost:8000
```

Si has llegado hasta aquí, y todo ha funcionado correctamente, solo me queda felicitarte: acabas de crear un API en Flask y tienes un frontend moderno en VueJS totalmente SPA.

### Siguiente

[Tema 4 Paso 7](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-7)

### Anterior

[Tema 4 Paso 5](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-5)
