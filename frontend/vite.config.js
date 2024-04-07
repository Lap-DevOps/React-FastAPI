import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwingcss from 'tailwindcss'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  css: {
    postcss: {
      plugins: [
        tailwingcss()
      ]
    }
  }
})
