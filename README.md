# Engine
Engine is a custom CMS project built using Wagtail with additional modifications such as predefined page models and StreamField blocks.

Speed and efficiency are the main objectives, Engine is built to be compatible with PyPy 7.3.4, which is on average 7.6x faster than the traditional CPython. The aim is to build the fastest and most lightweight project, future projects can be built on top of Engine.

## Installation
### Prerequisites
Must have an installation of PyPy 7.3.4 for best compatibility, equivalent or newer Python installations can be used provided you check whether the code and dependencies are compatible. 

Remember to use a virtual environment before installing packages!

```python
pip install -r requirements.txt
```

## Usage
Running the development server:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Synchronise the database with the `migrate` command, this needs to be run after you make database related changes in code and the `makemigrations` command.

Create a superuser with `createsuperuser`, you only need to do this once.

## Roadmap
v1.0.0 is currently being developed. Refer to the Roadmap v1.0.0 GitHub project board for details on what has to be done, what's being done and what has been done.
