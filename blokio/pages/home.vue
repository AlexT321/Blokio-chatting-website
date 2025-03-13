<template>
  <div class="w-screen h-screen bg-zinc-900 flex justify-between items-center flex-col overflow-hidden">
    <Header_main/>
    <div class="h-full w-full flex xl:justify-center items-center flex-row overflow-auto">
      <Side_menu/>
      <div class="h-full w-full bg-zinc-800 flex justify-start tiny:justify-center sm:items-center flex-col gap-2 overflow-auto">
        <div class=" relative h-[45rem] w-[100%] min-w-[350px] sm:w-[50vw] 2xl:w-[78vw] min-h-[500px] justify-center bg-zinc-700">
          <Call_overlay/>
          <!-- <Message/> -->
          <ul v-for="message in messages" :key="message.id">
            <Message :username="message.username" :date="message.date" :message="message.message"/>
          </ul>
          <Chat_overlay/>
        </div>
        <div class=" h-12 2xl:w-[78vw] sm:w-[50vw] w-[100%] min-w-[350px] bg-zinc-500 rounded-3xl flex flex-row justify-center items-center pl-5 pr-5 gap-5">
          <button @click="change_chat_overlay" class="h-12 w-12 min-w-[50px] text-3xl flex justify-center items-center text-zinc-800 pb-1 hover:bg-zinc-400">+</button>
          <input  @keyup.enter="create_message" v-model="inputtext" class=" h-12 w-[90rem] min-w-[10px] pl-1 bg-zinc-500 text-white placeholder:text-zinc-800 placeholder:text-2xl border-none flex justify-center items-center" type="text" placeholder="Message User"/>
          <button @click="change_call_overlay" class=" h-8 w-8 min-w-[30px] rounded-full bg-blue-500 text-white flex justify-center items-center hover:bg-blue-400">
            <svg class=" h-4 w-4 flex justify-center items-start fill-blue-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 488.3 488.3" xmlns:v="https://vecta.io/nano"><path d="M488.3 142.5v203.1c0 15.7-17 25.5-30.6 17.7l-84.6-48.8v13.9c0 41.8-33.9 75.7-75.7 75.7H75.7C33.9 404.1 0 370.2 0 328.4V159.9c0-41.8 33.9-75.7 75.7-75.7h221.8c41.8 0 75.7 33.9 75.7 75.7v13.9l84.6-48.8c13.5-8 30.5 1.9 30.5 17.5z"/></svg>
          </button>

        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Header_main from '../layouts/Header_main.vue';
import Footer_main from '../layouts/Footer_main.vue';
import Side_menu from '../layouts/Side_menu.vue';
import Message from '../components/Home_Components/Message.vue';
import Chat_overlay from '../components/Home_Components/Chat_overlay.vue';
import Call_overlay from '../components/Home_Components/Call_overlay.vue';

import { overlayVisibility } from '../store';
import {io} from "socket.io-client";

const socket = io("http://localhost:7000")
socket.on("connect", ()=> {
  console.log(`You connected with id: ${socket.id}`)
});

//socket.emit('custom-event', 10, "Hi", {a: 'a'})

// const message = async () => {
//   try {
//     const result = await fetch("http://127.0.0.1:8000/api/messages/get_data",{
//       method:"GET",
//       headers: {"content-type": "application/json",
      
//     }
//     })
//     const data = await result.json();
//     return data;
//   } catch(err) {
//     console.log(err);
//   }
// }
// const load_information = async() => {
//   const data = await message();
//   console.log(data);
// }
// load_information();

// const send_messages = async () => {
//   try {
//     const result = await fetch("http://127.0.0.1:8000/api/messages/post_data/",{
//       method:"POST",
//       body: JSON.stringify({
//       message: "I like dogs"
//     }),
//       headers: {"Content-type": "application/json",
      
//     },
//     })
//     const data = await result.json();
//     console.log(data);
//   } catch(err) {
//     console.log(err);
//   }
// }
// send_messages();

const register_user = async () => {
  try {
    const result = await fetch("http://127.0.0.1:8000/api/auth/register", {
      method: "POST",
      headers: {"Content-type": "application/json"},
      body: JSON.stringify({
        username: "ookiecat12345789@gmail.com",
        email: "ookiecat1235689@gmail.com",
        password: "alex1234",
        password2: "alex1234"
        // password: "Cookie123",
        // last_login: new Date(),
        // is_superuser: 0,
        // username: "cat123",
        // first_name: "bob",
        // last_name: "Robert",
        // email: "bobert@gmail.com",
        // is_staff: 0,
        // is_active: 0,
        // date_joined: new Date(),
      }),
      
    });
    const data = await result.json();
    if (result.ok) {
      console.log(data.message);
    } else {
      console.log(data.message);
    }
  } catch(err) {
    console.log('An error occurred;', err);
  }
}

//register_user();

const store = overlayVisibility();
const today = new Date();
const year:Number = today.getFullYear();
const month:Number = today.getMonth() + 1;
const day:Number = today.getDate();
const formattedDate:String = `${month}/${day}/${year}`;
//const name = prompt('What is your name?');
const name:string = "fred";
const messages = [{id: "53dcbvdfsc", username: "Alex", date: "5/12/21", message: "hello there"}];
socket.emit('new-user', name);

socket.on('chat-message', data => {
  console.log(data);
});


export default {
  name: "Home",
  data() {
    return {
      messages: [{id: "53dcbvdfsc", username: "Alex", date: "5/12/21", message: "hello there"}],
      inputtext: "",
    }
  },
  mounted() {
    socket.on("chat-message", data => {
      this.messages.push({id: "53dcbvdfsc", username: `${data.name}`, date: `${formattedDate}`, message: `${data.message}`});
    });
  },
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
    create_message() {
      if (this.inputtext.length > 0) {
        socket.emit('send-chat-message', this.inputtext);
        this.messages.push({id: "53dcbvdfsc", username: `Alex`, date: `${formattedDate}`, message: `${this.inputtext}`});
        this.inputtext = "";
      }
    },
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