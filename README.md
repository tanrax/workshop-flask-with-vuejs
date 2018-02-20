# Taller de API Rest con Flask y VueJS en armonia

## Tema 4 - Paso 5

### 🎈Checkpoint🎈

```bash
git checkout tema4-5
```

### Descripción

Mostramos los comentarios usando un nuevo componente

### Peticiones

#### Un componente dentro de otro

Nos aseguramos que en nuestro esquema de noticias tenemos *id*.

```python
# Notice
class NoticeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'url', 'user_id', '_links')

    _links = ma.Hyperlinks({
        'comments': ma.URLFor('comments', id='<id>'),
        'user': ma.URLFor('user_single', id='<user_id>')
    })
```

Creamos un nuevo componente, llamado *Comment*.

```html
<template>
  <div class="comments">
    Soy un comentario!
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Comment',
  data () {
    return {
    }
  }
}
</script>

<style scoped>
</style>
```

Lo importamos dentro de nuestro Componente Cover.

```javascript
import Comment from '@/components/Comment'

export default {
  name: 'Cover',
  components: {
    'comments': Comment
  },
  ...
```

Ahora ya podemos añadir nuestro componente como si fuera una etiqueta nueva.

```html
<comments></comments>
```

#### Mostrando u ocultado los comentarios

```html
<a @click="comments = notice.id" class="card-footer-item">
    <span>
        Comentarios
    </span>
</a>
</footer>
</div>
<comments v-if="comments == notice.id"></comments>
```

```javascript
...
  data () {
    return {
      news: [],
      pag: 1,
      showAddForm: false,
      title: '',
      url: '',
      comments: 0
    }
  },
...
```

#### Renderizando los comentarios de cada noticia

Le damos al componente la *id* de la noticia que debe obtener los comentarios. Sería más correcto dar la *url* de comentarios, pero me parece más claro para entender el funcionamiento.

```html
<comments v-if="comments == notice.id" :id="notice.id"></comments>
```

Y lo recogemos.

```javascript
import Vue from 'vue'

export default {
  name: 'Comment',
  props: ['id'],
  data () {
    return {
      comments: []
    }
  },
  mounted: function () {
    Vue.http.get(`http://localhost:5000/api/v1/notice/${this.id}/comments`).then(response => {
      this.comments = response.body
    }, response => {
      // error callback
    })
  }
}
```

Mostramos los resultados en el componente.

```html
<template>
  <div class="comments">
    <article v-for="comment in comments" :key="comment.id" class="message">
      <div class="message-body">
        {{ comment.text }}
      </div>
    </article>
  </div>
</template>
```

### Siguiente

[Tema 4 Paso 6](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-6)

### Anterior

[Tema 4 Paso 4](https://github.com/tanrax/workshop-flask-with-vuejs/tree/tema4-4)
