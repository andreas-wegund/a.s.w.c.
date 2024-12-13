# Installation Instructions:

## <span style="color:darkorange"><< 1. Installation >></span>
<hr>
1. Create a folder on your local PC<br>
2. In case you don't have it: create GitHub account and clone remote repository<br>
3. Duplicate `staticfiles` folder and rename it to `static`<br>
4. Get the `.env` file and save it to the core folder of the project<br>
<br>
<br>


## <span style="color:darkorange"><< 2. SETUP >></span>
<hr>
1. Install python if not already installed on local machine (https://www.python.org/)<br>
2. Activate virtual environment<br>
3. run: pip install -r requirements.txt<br>
4. run: python manage.py makemigrations<br>
5. run: python manage.py migrate<br>
6. run: python manage.py runserver<br>
7. run: python manage.py createsuperuser<br>
<br>
<br>


## <span style="color:darkorange"><< 3. HOW TO ADD A NEW FEATURE >></span>
<hr>
1. Create a new feature branch in the repository<br>
2. Add the new feature to the features table in the admin console<br>
3. Add feature toggle as follows in the code:

```python
from features.views import feature_enabled

def view( request ):
    feature_xxx = False
    
    try:
        feature_xxx = feature_enabled( request, 'HeroButton' )
    except:
          feature_xxx = False
```

4. Use the feature_xxx in the HTML template to show the feature only if the feature is enabled.
<br>
<br>


## <span style="color:darkorange"><< 4. TAILWIND CSS >></span>
<hr>
1. Download and install NodeJS<br>
2. Create a directory node in the project root folder and enter this folder
3. Run: npm init -y   &&  npm install tailwindcss  &&  npx tailwindcss init  &&  npm install clean-css-cli
4. Update files:

```node
// tailwind.config.js
module.exports = {
  content: [
      '../templates/**/*.html', // TailwindCSS auf globaler template Ebene
      '../templates/**/*.html', // alle apps, die ggf. TailwindCSS haben
      '../**/forms.py',    // in den Forms könnten wir TailwindCSS haben
  ],
    ...
}
```

```node
// package.json
"scripts": {
    "tailwind": "tailwind build -i ../static/css/tailwind.css -o ../static/css/style.css --watch",
    "minify-css": "cleancss ../static/css/style.css -o ../static/css/style.min.css"
}
```

5. In the node folder run: npm run tailwind
6. For deployment to production run: npm run minify-css