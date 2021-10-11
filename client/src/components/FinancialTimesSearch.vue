<template>
  <p class="text-center text-dark mt-5">
    Paieška pagal frazę Financial Times portale
  </p>
  <div class="mx-auto mb-5 w-50 input-group">
    <input
      type="text"
      class="form-control"
      :placeholder="placeholder"
      :aria-label="placeholder"
      v-model="searchText"
      v-on:keyup.enter="handleSearch"
    />
    <button type="button" class="btn btn-primary" disabled v-if="loading">
      <span
        class="spinner-border spinner-border-sm"
        role="status"
        aria-hidden="true"
      ></span>
      Loading...
    </button>
    <button
      v-else
      type="button"
      class="btn btn-primary"
      v-on:click="handleSearch"
    >
      Search
    </button>
  </div>
  <div class="alert alert-danger" role="alert" v-if="errors.length">
    <p>
      <b>Prašome ištaisyti šias klaidas:</b>
    </p>
    <ul class="list-group">
      <li
        class="list-group-item list-group-item-danger"
        v-for="error in errors"
        :key="error"
      >
        {{ error }}
      </li>
    </ul>
  </div>
  <table class="table">
    <thead>
      <tr>
        <th scope="col" class="col-sm-1">Index</th>
        <th scope="col" class="col-sm-1">Relevance</th>
        <th scope="col" class="col-sm-1">Tag</th>
        <th scope="col" class="col-sm-2">Headline</th>
        <th scope="col" class="col-sm-5">Summary</th>
        <th scope="col" class="col-sm-2">Link</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(article, index) in articles" :key="index">
        <td>{{ index }}</td>
        <td>{{ article.relevance }}</td>
        <th scope="row">{{ article.tag }}</th>
        <td>{{ article.headline }}</td>
        <td>{{ article.summary }}</td>
        <td>
          <a :href="article.link" class="link-primary">{{ article.link }}</a>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';

type Article = {
  relevance: number;
  tag: string;
  headline: string;
  summary: string;
  link: string;
};

interface SearchState {
  articles: Article[];
  searchText: string;
  loading: boolean;
  errors: string[];
}

export default defineComponent({
  data: (): SearchState => {
    return {
      articles: [],
      searchText: '',
      loading: false,
      errors: [],
    };
  },

  props: {
    placeholder: String,
  },

  methods: {
    handleSearch() {
      this.errors = [];

      if (!this.searchText) {
        this.errors.push('Įveskite paieškos žodį!');
      } else {
        this.loading = true;

        axios
          .get<Article[]>('http://127.0.0.1:5000/api', {
            params: { search: this.searchText },
          })
          .then((res) => {
            this.articles = res.data;
            console.log(res.data);
          })
          .catch((err) => console.log(err))
          .finally(() => (this.loading = false));
      }
    },
  },
});
</script>
