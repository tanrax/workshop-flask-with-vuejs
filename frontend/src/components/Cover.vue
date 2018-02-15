<template>
  <div class="cover">
    <div class="container">
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
                    View on <a href="https://twitter.com/codinghorror/status/506010907021828096">Twitter</a>
                  </span>
                </p>
                <p class="card-footer-item">
                  <span>
                    Share on <a href="#">Facebook</a>
                  </span>
                </p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Cover',
  data () {
    return {
      news: []
    }
  },
  mounted () {
    Vue.http.get('http://localhost:5000/api/v1/notice').then(response => {
      this.news = response.body
    }, response => {
      // error callback
    })
  }
}
</script>

<style scoped>
</style>
