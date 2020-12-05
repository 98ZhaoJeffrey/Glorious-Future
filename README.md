# Glorious-Future
Website built to be a centralized hub for marginalized students to get scholarships to reduce the burden of student loans. 

## Installation

Create a new virtual enviroment by running
```python
python3 -m venv [yourVenvName]
[yourVenvName]\Scripts\activate.bat
```
Install the required packages 
```python
pip install -r requirements.txt
```

Alternatively, if you have Docker, you can pull the image here

```docker
docker pull [image name here]
```

## Usage

Run a local development server (Must be inside the directory with manage.py)
```python
python manage.py runserver
```

Or if you used docker, run 

```docker
docker run [rest of the command]
```

Open the local host link and explore
