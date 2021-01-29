# Glorious-Future
Website built to be a centralized hub for marginalized students to get scholarships to reduce the burden of student loans. 

# Live Website

When the website is pushed to AWS, the link will be included here

## Installation

Pull the GitHub repo onto your computer

Create a new virtual enviroment by running
```python
python3 -m venv [yourVenvName]
[yourVenvName]\Scripts\activate.bat
```
Install the required packages 
```python
pip install -r requirements.txt
```
We used MySQL, but you can change this inside the settings.py file to a database engine supported by Django
```python
'ENGINE': 'django.db.backends.mysql',
```
You will also need to supply your own .env file/database configurations to connect to your database


## Usage

Run a local development server (Must be inside the directory with manage.py)
```python
python manage.py runserver
```

Open the local host link and explore
