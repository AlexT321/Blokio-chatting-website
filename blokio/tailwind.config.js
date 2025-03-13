module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.{js,vue,ts}",
    "./pages/**/*.{js,vue,ts}",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    extend: {
      screens: {
        'tiny': {'raw': '(min-height: 640px)'},
        'laptop': {'raw': '(min-height: 800px) and (min-width: 1024px)'}
      }
    }
  },
  plugins: [],
}