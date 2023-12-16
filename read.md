# 1. Install requirements  
* pip install -r requirements.txt  


# 2. Create .env file in the SAME directory with manage.py  

### Generate SECRET KEY by following commands:
* from django.core.management.utils import get_random_secret_key
* print(get_random_secret_key())
* SECRET_KEY='GENERATED SECRET KEY'

# 3. Make migrations
* ./manage.py makemigrations
* ./manage.py migrate

# 4.Load fixtures
* ./manage.py loaddata fixtures/products/brands.json(Load all fixtures from directory)
 
