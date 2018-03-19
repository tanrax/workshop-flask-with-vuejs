<template>
  <div class="cover">
    <div class="container">
      <!-- Add notice -->
      <button @click="showAddForm = !showAddForm" class="button is-primary plus">
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
          <div v-for="notice in news" :key="notice.id" class="column is-one-third" v-bind:class="{'is-12': comments == notice.id}">
               <div class="card nobackground">
                  <div class="card-content">
                    <p class="title">
                        {{ notice.title }}
                    </p>
                    <p class="subtitle">
                        {{ getTopURL(notice.url) }}
                    </p>
                  </div>
                <footer class="card-footer">
                  <a class="card-footer-item" :href="notice.url">
                    <span>
                      Ver más <i class="fas fa-arrow-right"></i>
                    </span>
                  </a>
                  <a @click="comments != notice.id ? comments = notice.id : comments = 0" v-bind:class="{'active': comments == notice.id}" class="card-footer-item">
                    <span>
                        Comentarios <i class="far fa-comment"></i>
                    </span>
                  </a>
                </footer>
              </div>
              <comments v-if="comments == notice.id" :id="notice.id"></comments>
            </div>
          </div>
        </section>
        <!-- End Links -->
      </div>
    </div>
</template>

<script>
import Vue from 'vue'
import Comment from '@/components/Comment'

export default {
  name: 'Cover',
  components: {
    'comments': Comment
  },
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
  mounted () {
    this.updatePag(this.pag)
  },
  created: function () {
    window.addEventListener('scroll', this.handleScroll)
  },
  destroyed: function () {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    updatePag: function (pag) {
      // Carga nueva información
      this.pag = pag
      Vue.http.get(`http://${process.env.API_URL}/api/v1/notice/pag/${this.pag}`).then(response => {
        for (let notice of response.body) {
          this.news.push(notice)
        }
        this.$nextTick(function () {
          // De forma aleatoria cambiamos los fondos de las tarjetas
          let cards = document.querySelectorAll('.card.nobackground')
          for (let index = 0; index < cards.length; index++) {
            cards[index].classList.add('fondo' + this.numeroAleatorioEntre(1, 8))
            cards[index].classList.remove('nobackground')
          }
        })
      }, response => {
        // error callback
      })
    },
    addNotice: function () {
      Vue.http.post(`http://${process.env.API_URL}/api/v1/notice`, {
        title: this.title,
        url: this.url,
        user_id: 1
      }).then(response => {
        // Refresco la información
        this.updatePag(this.pag)
        // Oculto el formulario
        this.showAddForm = false
        // Limpiamos las variables
        this.title = ''
        this.url = ''
      }, response => {
        // error callback
      })
    },
    showComments: function (id) {
      Vue.http.get(`http://${process.env.API_URL}/api/v1/notice/${id}/comments`).then(response => {
        this.comments = response.body
      }, response => {
        // error callback
      })
    },
    getTopURL: function (url) {
      let split1 = url.indexOf('//') !== -1 ? url.split('//')[1] : url
      let split2 = split1.indexOf('/') !== -1 ? split1.split('/')[0] : split1
      let domain = split2
      if (domain.substring(0, 4) === 'www.') {
        domain = split2.slice(4)
      }
      return domain
    },
    numeroAleatorioEntre: function (iniMin, iniMax) {
      return Math.floor(Math.random() * (iniMax - iniMin + 1) + iniMin)
    },
    handleScroll: function (event) {
      // current position
      let scrollPosition = window.pageYOffset
      // window height
      let windowSize = window.innerHeight
      // body height
      let bodyHeight = document.body.offsetHeight
      let distanceBottom = bodyHeight - windowSize - scrollPosition
      if (distanceBottom < 350) {
        this.pag += 1
        this.updatePag(this.pag)
      }
    }
  }
}

</script>

<style lang="sass" scoped>
$color-rosa-medio: #c91671
$color-rosa-claro: #c15691

.column
  transition: 1s all

button.plus
  display: block
  margin: 0 auto
.card
  .card-content
    .title, .subtitle
      color: white
  .card-footer
    background: white
    span
      color: $color-rosa-medio
  a.active
    background-color: $color-rosa-medio
    span
      background-color: $color-rosa-medio
      color: white
.pagination
  a
    background-color: $color-rosa-medio
    color: white
    &:hover
      background-color: $color-rosa-claro

.fondo1
  background-color: #08534E
.fondo2
  background-color: #92c6bf
.fondo3
  background-color: #4d3250
.fondo4
  background-color: #aba8c6
.fondo5
  background-color: #93733a
.fondo6
  background-color: #c15691
.fondo7
  background-color: #c91671
.fondo8
  background-color: #7c1242

</style>
