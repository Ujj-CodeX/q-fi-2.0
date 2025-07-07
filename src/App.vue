<template>
  <div id="app" style="background-color: blue;">
    <NavBar />
    </div>
    <main class="container-fluid">
      <router-view />  
    </main>
    
    <Footer />
  
</template>

<script>
import NavBar from './components/Nav.vue';
import Footer from './components/Footer.vue';


// eslint-disable-next-line vue/multi-word-component-names
export default {
  name: 'App',
  components: {
    NavBar ,Footer
  }
}
</script>

<style>

</style>
