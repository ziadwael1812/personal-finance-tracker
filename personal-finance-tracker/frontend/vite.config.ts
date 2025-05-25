import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 3000, // Or your preferred port
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Your backend API URL
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, '') // if your backend doesn't have /api prefix
      }
    }
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/setupTests.ts', // if you have a setup file
  }
}) 