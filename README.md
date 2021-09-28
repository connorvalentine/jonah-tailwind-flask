# Flask + TailwindCSS Starter Template
**Now updated with the [Tailwind JIT compiler mode](https://tailwindcss.com/docs/just-in-time-mode#enabling-jit-mode)**

With the (new highly efficient) Tailwind JIT compiler, purging of unused styles takes place both in development and production. 

## Key Features
- Basic Flask app scaffolding
- TailwindCSS setup using npm

## How to use
Setup and activate a virtual python environment before proceeding.

## download python. latest version is fine
https://www.python.org/downloads/

## download github app
https://desktop.github.com/

## clone repository to your computer using the app (enter this link when asked to)
https://github.com/connorvalentine/flask-tailwind.git

## Now we are going to install the python packages we need. 
- We make sure that every person running this code has the same version of the package installed with a requirements.txt file. 

  Open a new mac terminal and navigate to the same folder as the repo (./flask-tailwind)
  from that folder, enter these into the the terminal.
  1. create the virtual environment folder. This is where python and all the packages we install will live.
    `python3 -m venv env` 

  2. Activate the virtual environment by running:
   `source env/bin/activate`

  3. Install the required python packages with:
   `pip install -r requirements.txt`

  4. Now we install the required .css management files in the package.json file
   `npm install`
   
3. In one terminal run `npm run dev` to run Tailwind in JIT watch mode during development - this will start real time compilation of styles used in your HTML templates
4. In second terminal run `python run.py` to start the Flask development server (debug mode is ON). As you add/remove Tailwind classes in HTML templates, the watcher running in step 3 will automatically regenerate your `app\static\main.css` file which is picked up the flask server running in step 4.
4. When ready for production, kill the Flask development server in step 3 and run  `npm run build:prod` to prepare CSS build ready for production

Enjoy!
