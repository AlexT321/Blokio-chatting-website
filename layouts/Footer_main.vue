<template>
  <div id="container" class=" w-full absolute align-bottom hidden md:flex">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" height="300" width="100%" preserveAspectRatio="xMinYMid meet">
      <path fill="rgb(59 130 246)" fill-opacity="1" d="M0,96L60,112C120,128,240,160,360,176C480,192,600,192,720,181.3C840,171,960,149,1080,144C1200,139,1320,149,1380,154.7L1440,160L1440,320L1380,320C1320,320,1200,320,1080,320C960,320,840,320,720,320C600,320,480,320,360,320C240,320,120,320,60,320L0,320Z " transform="scale(1.42333)" />
    </svg>
  </div> 
  <div id="container" class=" w-full h-10 align-bottom bg-blue-500 sm:hidden">

  </div>
  <!-- <div class=" h-6 w-screen bg-blue-500"></div> -->
</template>

<script lang="ts">
export default {
  name: "footer_main",
};
</script>

<style scoped>
  #container {
    bottom: 0;
  }
</style>