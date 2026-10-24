import js from '@eslint/js';
import globals from 'globals';

export default [
  { ignores: ['.var/**', 'node_modules/**'] },
  js.configs.recommended,
  {
    files: ['www/**/*.js', '*.mjs'],
    languageOptions: {
      globals: {
        ...globals.browser,
      },
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
  },
];
