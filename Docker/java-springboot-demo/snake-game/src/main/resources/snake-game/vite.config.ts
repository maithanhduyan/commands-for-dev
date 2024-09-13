// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  base: './', // Sử dụng đường dẫn tương đối
  build: {
    outDir: '../static/dist/', // Thư mục đầu ra
    emptyOutDir: true, // Xóa sạch thư mục trước khi build
  },
});
