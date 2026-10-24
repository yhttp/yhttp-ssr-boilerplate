import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    cors: {
      origin: 'http://localhost:8080',
    },
  },
  plugins: [tailwindcss()],
  build: {
    manifest: true,
    outDir: '.var/static',
    cssCodeSplit: true,
    modulePreload: {
      polyfill: false,
    },
    rolldownOptions: {
      input: ['./www/master.js', './www/master.css'],
    },
  },
});
