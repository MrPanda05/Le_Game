/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      skew: {
        '180': '180deg',
        '360': '360deg',
      }
    },
  },
  plugins: [],
}