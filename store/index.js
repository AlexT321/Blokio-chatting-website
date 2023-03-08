import {defineStore} from "pinia"

export const overlayVisibility = defineStore('overlay_vis', {
  state: () => { 
    return {
      count: 0, 
      name: 'Eduardo',
      call_overlay_vis: 'none',
      chat_overlay_vis: 'none',
      friends_overlay_vis: 'flex',
      add_friends_overlay_vis: 'none',
    }
  },
  getters: {
    doubleCount: (state) => state.count * 2,
  },
  actions: {
    increment() {
      this.count++
    },
    change_chat_overlay_visibility() {
      const visibility = this.chat_overlay_vis === 'none' ? 'flex' : 'none';
      this.chat_overlay_vis = visibility;
    },
    change_friends_overlay_visibility() {
      this.friends_overlay_vis = 'flex';
    },
    change_add_friends_overlay_visibility() {
      this.add_friends_overlay_vis = 'flex';
    },
    hide_friends_overlay() {
      this.friends_overlay_vis = 'none';
    },
    hide_add_friends_overlay() {
      this.add_friends_overlay_vis = 'none';
    },
    change_call_overlay_visibility() {
      const visibility = this.call_overlay_vis === 'none' ? 'flex': 'none';
      this.call_overlay_vis = visibility;
    }
  },
})