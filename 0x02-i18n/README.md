# 0x02. i18n
## Directories
- **templates**: Holds all the jinja template files.
	- **0-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **1-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **2-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **3-index.html**: A Jinja template with the title and header parametrize with _() function
## Files
- **0-app.py**: Flask app with one route.
- **1-app.py**: Flask app with with Babel's default locale and timezone setup
- **2-app.py**: Flask app with the default lacale and timezone setup, and get_locale created with the babel.localeselector decorator.
- **3-app.py**: Flask app with a route that returns an index.html file with the title and header translate using the default babel's language.
