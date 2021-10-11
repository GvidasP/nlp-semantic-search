<template>
  <h1 class="text-center mt-3 text-dark">Financial News Search</h1>

  <section>
    <FinancialTimesSearch placeholder="Paieška Financial Times portale" />
  </section>
  <section><FTinWSJ placeholder="Strapsnių iš FT paieška WSJ" /></section>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';

import FinancialTimesSearch from './components/FinancialTimesSearch.vue';
import FTinWSJ from './components/FTinWSJ.vue';

export default defineComponent({
  name: 'App',
  components: {
    FinancialTimesSearch,
    FTinWSJ,
  },
});
</script>
