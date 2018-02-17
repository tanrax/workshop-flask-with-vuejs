# Taller de API Rest con Flask y VueJS en armonia

## Tema 4 - Paso 4

### 🎈Checkpoint🎈

```bash
git checkout tema4-4
```

### Descripción

Añadiremos una nueva noticia por medio de VueJS

### Peticiones

Ordenamos los resultados

```python
my_news = Notice.query.order_by(Notice.created_at.desc()).slice(start, end)
```

Añadimos un formulario para añadir nuevas noticias

```html
<!-- Add notice -->
<section class="section">
<div class="field">
  <div class="control">
    <input class="input" type="text" placeholder="Titulo">
  </div>
</div>
<div class="field">
  <div class="control">
    <input class="input" type="text" placeholder="Enlace">
  </div>
</div>
<div class="field">
  <div class="control">
    <button class="button">Enviar</button>
  </div>
</div>
</section>
<!-- End Add notice -->
```

No lo quiero siempre visible, por lo que integro un botón.

```html
<!-- Add notice -->
<button @click="showAddForm = !showAddForm" class="button is-primary">
<i class="fas fa-plus"></i>
</button>
<section v-if="showAddForm" class="section">
<div class="field">
  <div class="control">
    <input class="input" type="text" placeholder="Titulo">
  </div>
</div>
<div class="field">
  <div class="control">
    <input class="input" type="text" placeholder="Enlace">
  </div>
</div>
<div class="field">
  <div class="control">
    <button class="button">Enviar</button>
  </div>
</div>
</section>
<!-- End Add notice -->
```

```javascript
import Vue from 'vue'

export default {
  name: 'Cover',
  data () {
    return {
      news: [],
      pag: 1,
      showAddForm: false
    }
  },
  mounted () {
    this.updatePag(this.pag)
  },
  methods: {
    updatePag: function (pag) {
      this.pag = pag
      Vue.http.get(`http://localhost:5000/api/v1/notice/pag/${this.pag}`).then(response => {
        this.news = response.body
      }, response => {
        // error callback
      })
    }
  }
}
```

Me dispongo a enviar la información. Captura los input con VueJS y hago una petición POST.

```html
<!-- Add notice -->
<button @click="showAddForm = !showAddForm" class="button is-primary">
<i class="fas fa-plus"></i>
</button>
<section v-if="showAddForm" class="section">
<div class="field">
  <div class="control">
    <input v-model="title" class="input" type="text" placeholder="Titulo">
  </div>
</div>
<div class="field">
  <div class="control">
    <input v-model="url" class="input" type="text" placeholder="Enlace">
  </div>
</div>
<div class="field">
  <div class="control">
    <button @click="addNotice" class="button">Enviar</button>
  </div>
</div>
</section>
<!-- End Add notice -->
```

```javascript
import Vue from 'vue'

export default {
  name: 'Cover',
  data () {
    return {
      news: [],
      pag: 1,
      showAddForm: false,
      title: '',
      url: ''
    }
  },
  mounted () {
    this.updatePag(this.pag)
  },
  methods: {
    updatePag: function (pag) {
      this.pag = pag
      Vue.http.get(`http://localhost:5000/api/v1/notice/pag/${this.pag}`).then(response => {
        this.news = response.body
      }, response => {
        // error callback
      })
    },
    addNotice: function () {
      Vue.http.post('http://localhost:5000/api/v1/notice', {
        title: this.title,
        url: this.url,
        user_id: 1
      }).then(response => {
        // Refresco la información
        this.updatePag(this.pag)
        // Oculto el formulario
        this.showAddForm = false
      }, response => {
        // error callback
      })
    }
  }
}
```

### Siguiente

[Tema 4 Paso 5](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-5)

### Anterior

[Tema 4 Paso 3](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-3)
