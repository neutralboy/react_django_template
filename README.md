#React Django Template

This repo was created by me to avoid the hassles of all the npm setup and webpack config
I had been using this very Initial Setup to create Django backed ReactApp
and so far it has made my job easy.

I hope it works well with you too! If not then raise an issue here.

Prerequisites:
- You should know Django and its file structure pretty well
- Knowledge of Django-Rest-Framework is absolutely necessary
- You should also know how to customize npm **package.json**

### Setup steps

1. Run the following commands in the project root directory that is at ./react_django_template

	- `sudo pip3 install -r requirements.txt`

2. Run the following commands in the ./react_django_template/static/frontend_app

	- `npm run dev` for development mode
	- `npm run prod` for production mode

3. Then finally run the django development server at project root directory that is at ./react_django_template
	- `python3 manage.py runserver`
