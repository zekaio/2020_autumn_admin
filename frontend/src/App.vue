<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  async mounted() {
    this.$router.push({
      path: '/index',
    });
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
</style>
