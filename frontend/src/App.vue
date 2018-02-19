<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="sass">
// Colores
$color-verde-oscuro: #08534E
$color-verde-claro: #92c6bf
$color-morado-oscuro: #4d3250
$color-morado-claro: #aba8c6
$color-marron: #93733a
$color-rosa-claro: #c15691
$color-rosa-medio: #c91671
$color-rosa-oscuro: #7c1242

.logo
  width: 8rem

.subtitle
  display: flex
  align-items: center

.button.is-primary
  background-color: $color-rosa-claro
  &:hover
    background-color: $color-rosa-medio

.card-content
  min-height: 16rem

</style>
