<template>
  <div
    class="w-screen h-screen bg-zinc-900 flex justify-between items-center flex-col overflow-hidden"
  >
    <Header_main />
    <div class="h-full w-full flex xl:justify-center justify-center items-center flex-row">
      <Side_menu />
      <div
        class="h-full w-full bg-zinc-800 flex justify-start tiny:justify-center sm:items-center flex-col gap-2 overflow-auto"
      >
        <div
          class="relative w-[100%] min-w-[300px] h-20 flex flex-row items-center justify-start pl-4 gap-2"
        >
          <div class="h-12 w-12 bg-blue-500 flex justify-center items-center">
            <svg
              class="h-8 w-8 fill-blue-300"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 472.615 472.615"
              xmlns:v="https://vecta.io/nano"
            >
              <circle cx="236.308" cy="117.504" r="111.537" />
              <path
                d="M369 246.306l-5.297-3.493c-28.511 39.583-74.993 65.402-127.395 65.402s-98.894-25.825-127.404-65.416l-4.451 2.942C41.444 288.182 0 360.187 0 441.87v24.779h472.615V441.87c0-81.321-41.077-153.048-103.615-195.564z"
              />
            </svg>
          </div>
          <button @click="change_friends_overlay" class="h-12 w-32 bg-zinc-500 text-white hover:bg-zinc-400">Friends</button>
          <button @click="change_add_friends_overlay" class="h-12 w-32 bg-zinc-500 text-white hover:bg-zinc-400">Add Friends</button>
          <NuxtLink to="profile" class="h-12 w-36 bg-zinc-500 text-white flex justify-center items-center hover:bg-zinc-400">Profile / Settings</NuxtLink>
        </div>
        <div class="flex-col w-[100%] min-w-[300px]" :style="{display: friends_overlay_vis}">
          <div
            class="w-[160vh] h-20 flex flex-row items-center justify-start pl-4 gap-4"
          >
            <div class="h-14 w-14 rounded-full bg-white"></div>
            <input
              class="rounded-3xl bg-zinc-500 h-14 w-[35vw] lg:w-[60vh] min-w-[350px] text-white placeholder:text-white pl-5 text-lg "
              placeholder="Search"
            />
          </div>
          <div class="w-[160vh] h-[65vh] flex flex-col pl-16">
            <div
              class="h-14 w-44 flex flex-row justify-start items-center gap-3 pl-1 rounded-xl hover:bg-zinc-700"
            >
              <div class="h-10 w-10 rounded-full bg-white"></div>
              <div class="text-white text-lg">Username</div>
            </div>
          </div>
        </div>
        <div class="w-[100%] min-w-[300px]" :style="{display: add_friends_overlay_vis}">
          <div class="w-[160vh] h-[75vh] flex flex-col justify-start pl-4 gap-5">
            <h1 class="text-white">Add Friend</h1>
            <input class=" h-14 w-[35vw] lg:w-[60vh] min-w-[350px] bg-zinc-500 placeholder:text-white pl-5" placeholder="Enter Username"/>
            <button class=" w-52 h-14 bg-blue-500 text-white rounded-2xl hover:bg-blue-400">Send Friend Request</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Header_main from "~/layouts/Header_main.vue";
import Side_menu from "~/layouts/Side_menu.vue";
import Footer_main from "~/layouts/Footer_main.vue";

import { overlayVisibility } from '~~/store';
import { mapState } from 'pinia';

const store = overlayVisibility();

export default {
  components: {
    Header_main,
    Side_menu,
    Footer_main,
  },
  head() {
    return {
      title: "Blokio/Friends",
    };
  },
  methods: {
     change_friends_overlay() {
      store.hide_add_friends_overlay();
      return store.change_friends_overlay_visibility();
    },
     change_add_friends_overlay() {
      store.hide_friends_overlay();
      return store.change_add_friends_overlay_visibility();
    },
  },
  computed: {
    ...mapState(overlayVisibility,["friends_overlay_vis","add_friends_overlay_vis"])
  }
};
</script>

<style scoped></style>