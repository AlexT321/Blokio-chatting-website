<template>
  <div
    id="main-content"
    class="w-screen h-screen bg-zinc-900 flex justify-between items-center flex-col overflow-hidden"
  >
    <Header_main />
    <div
      class="h-full xl:w-full w-screen flex flex-row flex-en justify-center items-center gap-5 md:gap-0 overflow-hidden ml-[2vh]"
    >
      <div class="flex flex-col gap-12 ">
        <div
          class="h-fit xl:w-[100vh] w-screen lg:text-[3vw] sm:text-[5vw] text-[10vw] text-white pl-2 xl:pl-0"
        >
          Welcome to Blokio a new chatting website to stay communicated with
          your friends
        </div>
        <NuxtLink
          to="/sign_up"
          class="xl:h-20 xl:w-72 h-16 w-40 bg-gray-500 rounded-2xl flex justify-center items-center text-white text-lg xl:text-2xl ml-3 xl:ml-0 hover:bg-gray-400"
          >Create Account</NuxtLink
        >
      </div>
      <video id="robot_video" class=" w-[30vw] h-[30vw] hidden xl:flex  overflow-hidden" autoPlay muted>
        <source src="~~/assets/robot_zoom.mov" type="video/mp4; codecs='hvc1'">
        <source src="~~/assets/robot_zoom.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
    </div>
    <Footer_main />
  </div>
</template>

<script lang="ts">
import Header_main from "~/layouts/Header_main.vue";
import Footer_main from "~/layouts/Footer_main.vue";

export default {
  name: "IndexPage",
  components: {
    Header_main,
    Footer_main,
  },
  data() {
    return {
      videoSrc: '../../blokio/assets/test-vid.mp4',
    }
  },
  head() {
    return {
      title: "Blokio",
      meta: [
        {
          hid: "Chatting Website",
          name: "Blokio a chatting website",
          content:
            "information about the purpose of the website and how to sign up",
          keywords: "Blokio, Chatting, Chatting Website",
        },
      ],
    };
  },
};
</script>

<style scoped>
#main-content {
  background-image: url("../../blokio/assets/circuit_background.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

</style>
