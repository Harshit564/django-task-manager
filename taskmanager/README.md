# Welcome to TaskManager's documentation!

This is an awesome **Django Project**!!

With this code you can start a **complex** Django Project very quickly, with just a few steps!

Some of the TaskManager Django Project functionalities are:

- **Internationalization** and **localization** to support different languages.
- Project structure
- Template Inheritance
- robots.txt and humans.txt configured

Check out the requirements and the quick start guide!

## Requirements

The requirements necessary to use this Django Project are:

- [Python 3](https://www.python.org/downloads/) and [pip3](https://www.python.org/dev/peps/pep-0439/#the-pip-bootstrap)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
- **GNU gettext** (to use Internationalization)

[GNU gettext on windows](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#gettext-on-windows)

## Quick Start Guide

Here are the details of the manual installation and configuration:

### Download TaskManager Django Project

First, you need to download the project from GitHub, as a zip file or using your terminal:

    $ git clone https://github.com/jazzify/django-task-manager.git

This will download the repository in your current direcotry.

### Secret Django Key

This project has the **DJANGO_KEY** setting variable hidden.

You can generate your DJANGO_KEY <http://www.miniwebtool.com/django-secret-key-generator>

Keep reading to include your new Django key into your project.

### Project Name

This project is named *TaskManager*, so if you are using this 
Boilerplate to create your own project, you'll have to change 
the name in a few places:

    - *taskmanager_project* **folder** (your top project container)
    - *taskmanager_project/taskmanager* **folder** (your project name)
    - in *taskmanager_project/taskmanager*
        - edit **wsgi.py** and change **"taskmanager.settings"** accordingly.
    - in *taskmanager_project/taskmanager/settings*
        - edit the **base.py** file and change the declarations of **ROOT_URLCONF** and **WSGI_APPLICATION**
    - in taskmanager_project edit manage.py file and change os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskmanager.settings")

### Virtual environments and Settings Files

Create a Development virtual environment with Python 3 installed::

    $ mkvirtualenv tb_dev

You must add the line:

    $ export DJANGO_SETTINGS_MODULE="taskmanager.settings.development"
    (On windows) set DJANGO_SETTINGS_MODULE=taskmanager.settings.development

Secret Key:

    Create secret.py file with **SECRET_KEY = 'your-django-secret-key'** inside

with your project name and your own secret key.

Next, install the packages in each environment::

    $ pip install -r requirements.txt

Next, apply the basic migrations::

    $ python manage.py migrate
    $ python manage.py makemigrations

And check that everything works by starting the server::

    $ python manage.py runserver

## Internationalization and Localization

### Settings

The default language for this Project is **English**, and we use internatinalization to translate the text into Spanish.

If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found <http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx>

For example, if you want to use German you should include::

    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )

You can also specify a dialect, like Luxembourg's German with::

    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )

Note: the name inside the translation function _("") is the language name in the default language (English).

More information in <https://docs.djangoproject.com/en/2.0/topics/i18n/>

### Translation

Go to the terminal, inside the taskmanager_project folder and create the files to translate with::

    $ python manage.py makemessages -l ca

change the language "ca" for your selected language.

Next, go to the locale folder of your language::

    $ cd taskmanager/locale/ca/LC_MESSAGES

where taskmanager is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings <https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#localization-how-to-create-language-files>

Once the translation is done, compile your messages with::

    $ python manage.py compilemessages -l ca
