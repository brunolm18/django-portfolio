set -o errexit

#poetry install 
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate