<template>
  <div class="comments">
    <article v-for="comment in comments" :key="comment.id" class="message">
      <div class="message-body">
        {{ comment.text }}
      </div>
    </article>
  </div>
</template>

<script>
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
    Vue.http.get(`https://${process.env.API_URL}/api/v1/notice/${this.id}/comments`).then(response => {
      this.comments = response.body
    }, response => {
      // error callback
    })
  }
}
</script>

<style lang="sass" scoped>

$color-rosa-medio: #c91671

.message
  .message-body
    background: white
    border-color: $color-rosa-medio

.message:not(:last-child)
  margin-bottom: .2rem

</style>
