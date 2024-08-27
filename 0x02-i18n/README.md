# 0x02. i18n
## Directories
- **templates**: Holds all the jinja template files.
	- **0-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **1-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **2-index.html**: Jinja template that simply outputs “Welcome to Holberton” as page title (title) and “Hello world” as header (h1).
	- **3-index.html**: A Jinja template with the title and header parametrize with _() function.
	- **4-index.html**: A Jinja template with the title and header parametrize with _() function.
	- **4-index.html**: A Jinja template to display a user name if logged in.
	- **5-index.html**: A Jinja template to display a user name if logged in.
## Files
- **0-app.py**: Flask app with one route.
- **1-app.py**: Flask app with with Babel's default locale and timezone setup
- **2-app.py**: Flask app with the default lacale and timezone setup, and get_locale created with the babel.localeselector decorator.
- **3-app.py**: Flask app with a route that returns an index.html file with the title and header translate using the default babel's language.
- **4-app.py**: Contains a get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it.
- **5-app.py**: Mocks the login process.
- **6-app.py**: Define get_locale function to use a user’s preferred local if it is supported.
