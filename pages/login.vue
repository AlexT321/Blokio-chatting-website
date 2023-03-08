<template>
  <div class=" w-screen h-screen bg-zinc-900 flex justify-center tiny:items-center overflow-auto">
    <form class=" h-[75vh] md:w-[50vh] w-[10rem] min-h-[500px] min-w-[270px]  bg-zinc-600 rounded-[40px] flex items-center  justify-between flex-col overflow-hidden">
      <div class=" w-full h-20 bg-blue-500 "></div>
      <main class="laptop:h-[90%] laptop:w-[90%] flex justify-center items-center flex-col p-4 laptop:gap-2">
        <h1 class=" text-[2.5rem] text-white underline  mb-2">Login</h1>
        <div class="h-fit w-[100%] laptop:w-[80%] flex flex-col justify-start items-start">
          <h2 class="w-[100%] min-w-[200px] text-white  text-lg mb-3">Email:</h2>
          <input class=" border-none h-8  w-[100%]  min-w-[200px] rounded-3xl mb-3"/>
        </div>
        <div class="h-fit w-[100%] laptop:w-[80%] flex flex-col justify-start items-start">
          <h2 class="w-[100%] min-w-[200px] text-white text-lg  mb-3">Password:</h2>
          <input class=" border-none h-8 w-[100%] min-w-[200px] rounded-3xl mb-3"/>
        </div>
        <NuxtLink to="/forgot_password" class=" text-white text-sm mb-10 cursor-pointer hover:underline">Forgot Password?</NuxtLink>
        <button class=" w-32 h-8 bg-gray-400 rounded-2xl text-white text-sm lg:text-lg cursor-pointer hover:bg-gray-300">Login</button>
      </main>
      <div class="w-full h-8 bg-blue-500 flex justify-center items-center">
        <NuxtLink to="/sign_up" class=" text-white text-sm cursor-pointer hover:underline">Create an Acoount</NuxtLink>
      </div>
    </form>
  </div>
</template>


<script lang="ts">
import Vue from 'vue'
export default{
  head() {
    return {
      title: "Blokio/Login",
      meta: [
        {charset: "utf-8",},
        {name: "viewport", content: "width=device-width, initial-scale=1"},
        {
          hid: "Blokio Login Page",
          name: "Blokio Login",
          content: "Login page for Blokio",
        },
      ]
    };
  }
};
</script>

<style scoped>
</style>