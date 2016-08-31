virtualenv -p python3 --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
