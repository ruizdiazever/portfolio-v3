# Frontend

## First steps

```bash
npm create vite@latest $name -- --template svelte
cd $name
npm install --save svelte-routing
npx svelte-add@latest tailwindcss
npm install

# Svelte 3
npm init svelte@next $name
cd $name
npm install
npx svelte-add@latest tailwindcss postcss autoprefixer svelte-preprocess
npm i -D flowbite-svelte
npm install
```

- [Sverdle game](http://localhost:5174/sverdle)
- [About](http://localhost:5174/about)

## Commands

```bash
cd frontend
npx vite build     # Build for production
npx vite preview   # Locally preview production build
```

Update npm packages

```bash
ncu --upgrade # Upgrade package in latest major version
npm install   # Install
```
