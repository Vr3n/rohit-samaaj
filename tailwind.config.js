/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/**/*.{html, js}",
    "./templates/**/*.{html, js}",
    "./templates/*.{html, js}",
  ],
  theme: {
    extend: {},
    daisyui: {
      themes: ["light"],
    },
  },
  plugins: [require("daisyui")],
};
