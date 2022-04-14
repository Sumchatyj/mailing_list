# Simple notification service
##Features
- Creation and managment of your client database;
- Creation mailing list with certain parameters through a third party service;
- Open API documentation.

## How to start

Clone repository to your working directory.
In the file *mailing_list/mailing_app/messaging.py* you need to change a third party service token:

`11. TOKEN = os.getenv("TOKEN")`

Activate your venv.
Install requirements:

`$ pip install -r requirements.txt`

Do all migrations, be sure that you are in directory with manage.py:

`$ python manage.py migrate`

Then just run the server:

`$ python manage.py runserver`

API documentation available at:

<http://127.0.0.1:8000/swagger/>

## What you can do

Start mailing to your clients with filters: **tag** or **phone operators code**. Start delayed mailing due to **start_date** and **end_date** parameters, which should be passed in the form: **YYYY-MM-DD HH:MM**.

You can check statistic of your mailings:
- information of all mailings availible on this endpoint: <http://127.0.0.1:8000/mailing-stat/>
- information of specific mailing availible on this endpoint: <http://127.0.0.1:8000/message/{mailing_id}/>