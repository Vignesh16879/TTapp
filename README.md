# TTapp
Features:
1.

## Demo

1. Clone the Github repo:
   
```
git clone https://github.com/Vignesh16879/TTapp.git

cd fcsapp/
```
2. Install all the requirements
```
pip install -r requirements.txt
```

4. Activate the virtual enviroment
   
```
source .venv/bin/activate
```

5. Make migration on the local server
   
```
python3 manage.py makemigrations Scheduler

python3 manage.py migrate
```

6. Run server on [localhost](http://127.0.0.1:8000)
   
```
python3 manage.py runserver
```
