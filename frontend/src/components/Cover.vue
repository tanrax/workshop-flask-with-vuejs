<template>
  <div class="cover">
    <div class="container">
      <!-- Links -->
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
      pag: 1
    }
  },
  mounted () {
    Vue.http.get(`http://localhost:5000/api/v1/notice/pag/${this.pag}`).then(response => {
      this.news = response.body
    }, response => {
      // error callback
    })
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
</script>

<style scoped>
</style>
