<template>
  <h1 class="text-center mt-3 text-dark">Financial News Search</h1>
  <Search placeholder="Paieška" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';

import Search from './components/Search.vue';

export default defineComponent({
  name: 'App',
  components: {
    Search,
  },
});
</script>
