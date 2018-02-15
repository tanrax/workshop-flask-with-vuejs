# Taller de API Rest con Flask y VueJS en armonia

1# Tema 4 - Paso 3

### 🎈Checkpoint🎈

```bash
git checkout tema4-3
```

### Descripción

Conectamos con nuestra API por medio de Vue-resource. Una biblioteca encargada de gestionar las llamadas por AJAX.

### Peticiones

```bash
cd frontend
npm install --save vue-resource
```

En main.js

```javascript
import VueResource from 'vue-resource'
Vue.use(VueResource)
```

En nuestro componente

```javascript
import Vue from 'vue'

mounted () {
    Vue.http.get('http://localhost:5000/api/v1/notice').then(response => {
      this.news = response.body
    }, response => {
      // error callback
    })
  }
```

Request header field Access-Control-Allow-Origin is not allowed 

```python
from flask_cors import CORS
CORS(app)
```

Ninguna

### Siguiente

[Tema 4 Paso 4](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-4)

### Anterior

[Tema 4 Paso 2](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-2)
