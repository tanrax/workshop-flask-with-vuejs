<template>
  <div class="cover">
    <div class="container">
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
      <!-- Links -->
      <section class="section">
        <div class="columns is-multiline">
            <div v-for="notice in news" :key="notice.id" class="column is-one-third">
               <div class="card">
                  <a :href="notice.url">
                    <div class="card-content">
                      <p class="title">
                          {{ notice.title }}
                      </p>
                      <p class="subtitle">
                          {{ notice.url }}
                      </p>
                    </div>
                  </a>
                <footer class="card-footer">
                  <p class="card-footer-item">
                    <span>
                      <i class="fas fa-arrow-up"></i>
                    </span>
                  </p>
                  <p class="card-footer-item">
                    <span>
                      <i class="fas fa-arrow-down"></i>
                    </span>
                  </p>
                  <p class="card-footer-item">
                    <span>
                        Comentarios
                    </span>
                  </p>
                </footer>
              </div>
            </div>
          </div>
        </section>
        <!-- End Links -->
        <!-- Paginator -->
        <nav class="pagination" role="navigation" aria-label="pagination">
          <a v-if="pag != 1"  @click="updatePag(pag - 1)" class="pagination-previous">Anterior</a>
          <a class="pagination-next" @click="updatePag(pag + 1)">Siguiente</a>
        </nav>
        <!-- End Paginator -->
      </div>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Cover',
  data () {
    return {
      news: [],
      pag: 1,
      showAddForm: false,
      title: '',
      url: '',
      comments: []
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
    },
    showComments: function (id) {
      Vue.http.get(`http://localhost:5000/api/v1/notice/${id}/comments`).then(response => {
        this.comments = response.body
      }, response => {
        // error callback
      })
    }
  }
}
</script>

<style scoped>
</style>
