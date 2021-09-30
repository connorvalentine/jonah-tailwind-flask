// tailwind.config.js
// to compile run from raposa_app/app directory: npx tailwindcss -o ./static/tailwind.css    

// if you uncomment mode and purge, it will create a tailwind.css file that ONLY has the tailwind classes you used in your .html files. 
// This is something you do before hosting the website on a server because it will run faster. But while you are just using this for personal use dont worry about it.
module.exports = {
  // mode: 'jit',   // This will remove all unused styles from the tailwind.css sheet in static/css/tailwind.css file. Comment out for dev environment
  // purge: ['app/templates/**/*.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    }
}
