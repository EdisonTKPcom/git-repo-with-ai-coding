// Flat ESLint config for ESLint v9
// See: https://eslint.org/docs/latest/use/configure/migration-guide
import js from '@eslint/js';

export default [
  js.configs.recommended,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: 'module',
      globals: {
        console: 'readonly',
        process: 'readonly',
        URL: 'readonly'
      }
    },
    rules: {
      indent: ['error', 4, { SwitchCase: 1 }],
      'max-len': ['warn', { code: 100, ignoreStrings: true, ignoreTemplateLiterals: true }],
      'eol-last': ['error', 'always'],
      'no-trailing-spaces': 'error',
      semi: ['error', 'always'],
      'no-eval': 'error',
      'no-unused-vars': ['warn', { args: 'after-used', ignoreRestSiblings: true }],
      'prefer-const': 'warn'
    }
  },
  {
    files: ['eslint.config.js'],
    rules: {
      indent: 'off'
    }
  },
  {
    files: ['test/**/*.js'],
    rules: {
      // test overrides here if needed
    }
  }
];
