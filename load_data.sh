docker-compose exec web python manage.py loaddata menuitem_fixtures
docker-compose exec web python manage.py loaddata ingredient_fixtures
docker-compose exec web python manage.py loaddata reciperequirement_fixtures
docker-compose exec web python manage.py loaddata purchases_fixtures