<template>
  <div>
    <div class="w-full h-[8vh] min-h-[50px] flex items-center pl-5 gap-2 border-b-zinc-800 border-b-2">
      <div class="h-10 w-10 rounded-full bg-white"></div>
      <div class=" h-[8vh] w-full  flex flex-col justify-center">
        <div class=" flex flex-row gap-2">
          <h1 class="text-white">{{username }}</h1>
          <h2 class=" text-white">{{ date }}</h2>
        </div>
        <p class="text-white">{{ message }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: ['message', 'date', 'username']
};
</script>

<style scoped></style>
