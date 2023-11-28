Before use this install libs from requirements.txt
#pip install -r requirements.txt
Create .env file in the SAME directory with manage.py
#Generate SECRET KEY by following commands:
#from django.core.management.utils import get_random_secret_key
#print(get_random_secret_key())
#SECRET_KEY='GENERATED SECRET KEY'
Make migrations
#./manage.py makemigrations
#./manage.py migrate
 
