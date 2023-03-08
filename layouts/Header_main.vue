<template>
  <header class=" bg-blue-500 w-screen h-16 flex items-center justify-between sm:justify-center flex-row gap-2 sm:gap-5 pl-4">
    <div class="sm:hidden flex justify-center items-center">
      <svg class="fill-blue-200" xmlns="http://www.w3.org/2000/svg" width="48" height="48" xmlns:v="https://vecta.io/nano"><path d="M41 14H7a2 2 0 0 1 0-4h34a2 2 0 0 1 0 4zm0 12H7a2 2 0 0 1 0-4h34a2 2 0 0 1 0 4zm0 12H7a2 2 0 0 1 0-4h34a2 2 0 0 1 0 4z"/></svg>
    </div>
    <NuxtLink to="/" class="w-10 h-10 bg-blue-200 hover:bg-blue-100"></NuxtLink>
    <div class="text-white hidden sm:flex items-center mr-auto sm:text-2xl">Blokio</div>
    <NuxtLink to="/home" class="h-full w-32 sm:w-40 bg-blue-300 flex justify-center items-center text-white cursor-pointer text-sm sm:text-lg hover:bg-blue-200" >Go to Dashboard</NuxtLink>
    <div  class=" w-10 h-10 bg-blue-200 rounded-full mr-5 hidden"></div>
  </header>
</template>

<script lang="ts">
import Vue from 'vue'
export default {
  name: "Header_main",
  props: {
    dashboard_vis: {
      type: String,
      default: "none",
    },
    profile_vis: {
      type: String,
      default: "none",
    },
  },
  computed: {
    dashboard_style() {
      return {display: this.dashboard_vis}
    },
    profile_style() {
      return {"background-color": this.profile_vis}
    },
  },
};
</script>

<style>

</style>