<template>
  <div class="w-screen h-screen bg-zinc-900 flex justify-between items-center flex-col overflow-hidden">
    <Header_main/>
    <div class="h-full w-full flex xl:justify-center items-center flex-row overflow-auto">
      <Side_menu/>
      <div class="h-full w-full bg-zinc-800 flex justify-start tiny:justify-center sm:items-center flex-col gap-2 overflow-auto">
        <div class=" relative h-[45rem] w-[100%] min-w-[350px] sm:w-[50vw] 2xl:w-[78vw] min-h-[500px] justify-center bg-zinc-700">
          <Call_overlay/>
          <Message/>
          <Chat_overlay/>
        </div>
        <div class=" h-12 2xl:w-[78vw] sm:w-[50vw] w-[100%] min-w-[350px] bg-zinc-500 rounded-3xl flex flex-row justify-center items-center pl-5 pr-5 gap-5">
          <button @click="change_chat_overlay" class="h-12 w-12 min-w-[50px] text-3xl flex justify-center items-center text-zinc-800 pb-1 hover:bg-zinc-400">+</button>
          <input  class=" h-12 w-[90rem] min-w-[10px] pl-1 bg-zinc-500 text-white placeholder:text-zinc-800 placeholder:text-2xl border-none flex justify-center items-center" type="text" placeholder="Message User"/>
          <button @click="change_call_overlay" class=" h-8 w-8 min-w-[30px] rounded-full bg-blue-500 text-white flex justify-center items-center hover:bg-blue-400">
            <svg class=" h-4 w-4 flex justify-center items-start fill-blue-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 488.3 488.3" xmlns:v="https://vecta.io/nano"><path d="M488.3 142.5v203.1c0 15.7-17 25.5-30.6 17.7l-84.6-48.8v13.9c0 41.8-33.9 75.7-75.7 75.7H75.7C33.9 404.1 0 370.2 0 328.4V159.9c0-41.8 33.9-75.7 75.7-75.7h221.8c41.8 0 75.7 33.9 75.7 75.7v13.9l84.6-48.8c13.5-8 30.5 1.9 30.5 17.5z"/></svg>
          </button>

        </div>
      </div>
    </div>
    <Footer_main/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Header_main from '~/layouts/Header_main.vue';
import Footer_main from '~/layouts/Footer_main.vue';
import Side_menu from '~/layouts/Side_menu.vue';
import Message from '~/components/Home_Components/Message.vue';
import Chat_overlay from '~/components/Home_Components/Chat_overlay.vue';
import Call_overlay from '~/components/Home_Components/Call_overlay.vue';

import { overlayVisibility } from '~~/store';


const store = overlayVisibility();

export default {
  name: "Home",
  components: {
    Header_main,
    Footer_main,
    Side_menu,
    Message,
    Chat_overlay,
    Call_overlay,
  },
  head() {
    return {
      title: "Blokio/Home",
    }
  },
  methods: {
    change_chat_overlay() {
      return store.change_chat_overlay_visibility();
    },
    change_call_overlay() {
      return store.change_call_overlay_visibility();
    },
  },
};
</script>

<style>

</style>