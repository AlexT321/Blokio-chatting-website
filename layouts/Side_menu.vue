<template>
  <div class="hidden h-full w-80 min-w-[250px] bg-zinc-900 sm:flex justify-start items-center flex-col gap-5 pt-10 p-2 overflow-auto">
    <NuxtLink to="/home" class=" text-white h-10 w-52 bg-zinc-500 flex justify-start items-center pl-5 hover:bg-zinc-400">Home</NuxtLink>
    <NuxtLink to="/friends" class=" text-white h-10 w-52 bg-zinc-500 flex justify-start items-center pl-5 hover:bg-zinc-400">Friends +</NuxtLink>
    <h1 class=" text-white h-10 w-52 bg-blue-500 flex items-center pl-5 rounded-2xl">Conversations</h1>
    <div class="h-10 w-52 flex flex-row items-center gap-3 rounded-xl hover:bg-zinc-800">
      <div class="h-10 w-10 bg-white rounded-full"></div>
      <button class=" text-white text-xl">Username 1</button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default {
  
};
</script>

<style>

</style>