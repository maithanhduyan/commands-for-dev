/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'custom-orange': '#fd7f5d',
        'brand-orange': '#FF3D00',
      },
    },
  },
  plugins: [],
}

