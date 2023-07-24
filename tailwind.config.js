/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#f5f6fa",
          100: "#eaecf4",
          200: "#cfd5e8",
          300: "#a6b2d3",
          400: "#7588bb",
          500: "#4e6297",
          600: "#415288",
          700: "#36436e",
          800: "#2f3a5d",
          900: "#2b334f",
          950: "#1d2134",
        },
        secondary: {
          50: "#f8f5ee",
          100: "#efe8d2",
          200: "#e0d1a8",
          300: "#ceb376",
          400: "#bf9850",
          500: "#b08442",
          600: "#976a37",
          700: "#79502f",
          800: "#67432d",
          900: "#58392b",
          950: "#331d15",
        },
      },
    },
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
};
