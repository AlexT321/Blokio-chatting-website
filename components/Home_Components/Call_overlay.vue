<template>
  <div :style="{display: call_overlay_vis}" class=" h-auto w-[100%] bg-zinc-900 flex-col justify-center items-center p-10 gap-5">
    <div class=" w-[150vh] flex justify-center items-center">
      <div class=" h-10 w-10 bg-white rounded-full"></div>
    </div>
    <div class=" w-[150vh] flex justify-center items-center gap-5">
      <button class=" h-10 w-10 bg-zinc-600 rounded-full flex justify-center items-center text-white text-xl pb-1 hover:bg-zinc-500">+</button>
      <button class=" h-10 w-10 bg-zinc-600 rounded-full flex justify-center items-center hover:bg-zinc-500">
        <svg class=" h-6 w-6 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 478 478" xmlns:v="https://vecta.io/nano"><path d="M394 196.1c0-11.9-9.7-21.6-21.6-21.6s-21.6 9.7-21.6 21.6c0 61.7-50.2 111.8-111.8 111.8s-111.8-50.2-111.8-111.8c0-11.9-9.7-21.6-21.6-21.6S84 184.2 84 196.1c0 78.2 58.1 143 133.4 153.5v85.2h-55.6c-11.9 0-21.6 9.7-21.6 21.6s9.7 21.6 21.6 21.6h154.5c11.9 0 21.6-9.7 21.6-21.6s-9.7-21.6-21.6-21.6h-55.6v-85.2C335.9 339.1 394 274.2 394 196.1zM239 0h0c-46.4 0-84 37.6-84 84v110.7c0 46.4 37.6 84 84 84h0c46.4 0 84-37.6 84-84V84c0-46.4-37.6-84-84-84zm.1 55.9c-15.1 0-27.4 12.3-27.4 27.4v.6h0l-.2 99.9c0 6.9-5.6 12.4-12.4 12.4h0c-6.9 0-12.4-5.6-12.4-12.4V83.3h0v-.1c0-28.9 23.5-52.4 52.4-52.4 6.9 0 12.5 5.6 12.5 12.5 0 7-5.6 12.6-12.5 12.6z"/></svg>
      </button>
      <button class=" h-10 w-10 bg-zinc-600 rounded-full flex justify-center items-center hover:bg-zinc-500">
        <svg  class=" h-6 w-6 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230.629 230.629" xmlns:v="https://vecta.io/nano"><path d="M230.629 59.325H0v150.989h230.629V59.325zM115.314 183.373c-26.814 0-48.553-21.738-48.553-48.554s21.738-48.553 48.553-48.553 48.555 21.739 48.555 48.553-21.74 48.554-48.555 48.554zM88.041 20.315h54.547l17.943 28.93H70.1l17.941-28.93zm56.406 114.504c0 16.089-13.043 29.133-29.133 29.133s-29.131-13.044-29.131-29.133 13.043-29.132 29.131-29.132 29.133 13.043 29.133 29.132z"/></svg>
      </button>
      <button class=" h-10 w-10 bg-zinc-600 rounded-full flex justify-center items-center hover:bg-zinc-500">
        <svg class=" h-6 w-6 fill-white" xmlns="http://www.w3.org/2000/svg" width="24" height="24" xmlns:v="https://vecta.io/nano"><path d="M4.96 15.526l2.595-1.274a.7.7 0 0 0 .407-.579l.056-1.032a.66.66 0 0 1 .437-.579c2.097-.779 4.403-.779 6.5 0a.66.66 0 0 1 .437.579l.109 1.032a.7.7 0 0 0 .394.589l2.595 1.274.662.331a.71.71 0 0 0 .308.07.69.69 0 0 0 .467-.179 3 3 0 0 0 .992-2.559l-.03-.235-.016-.122c-.006-.056-.014-.111-.026-.166l-.04-.162c-.55-2.151-4.078-3.843-8.456-4.008h-1.245c-4.372.165-7.9 1.857-8.483 4l-.04.162c-.012.054-.02.11-.026.165l-.017.122-.03.235a3 3 0 0 0 .993 2.558.69.69 0 0 0 .467.179.71.71 0 0 0 .308-.07z"  stroke-miterlimit="10" stroke-width="1.5"/></svg>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
//import {mapState} from 'vuex';
import { overlayVisibility } from '~~/store';
import { mapState } from 'pinia';

const store = overlayVisibility();

export default {
  name: "Call_overlay",
  computed: {
    ...mapState(overlayVisibility, ["call_overlay_vis"])
  }
};
</script>


<style lang="stylus" scoped>

</style>