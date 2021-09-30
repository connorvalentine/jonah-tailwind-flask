When compiling changes:

from within the app directory (the same dir where tailwind.config is)

run: 
npx tailwindcss -o .app/static/tailwind.css    

translation: 
npx is calling tailwindcss to generate a new .css sheet. 
the output (-o) will be to a file called tailwind.css in the folder .app/static.

When you are exploring new styles, comment out the mod:'jit'. 

YOU MUST - re-enable JIT mode to gut the .css file before committing to github. File difference is 4 mb vs 10 kb lol



https://tailwindcomponents.com/cheatsheet/






