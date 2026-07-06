import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Proxy API calls to the FastAPI backend running on localhost:8000
      '/db-check': 'http://localhost:8000',
      '/api': 'http://localhost:8000'
    }
  }
})
