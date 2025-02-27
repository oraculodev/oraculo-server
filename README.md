# oraculo-server

## About
[About](https://oraculodev.com/about)

## License
This project is licensed under the MIT [LICENSE](License) – see the LICENSE file for details.

## requirements

-   install docker

## setup

copy file `.env.exemple` to `.env` on `/config` folder

## how to build and run locally

run `docker-compose up`

for the first time:

-   run `docker-compose exec oraculo-api python manage.py createsuperuser` create an admin user

for import github reposositories:

-   configure an env var `GITHUB_API_KEY` for grant access to your github repositories
-   configure an env var `GITHUB_ORG_NAME` related to your organization
-   run `docker-compose exec oraculo-api python manage.py import_github_repos`

application urls

-   admin - http://localhost:8000/admin
-   api - http://localhost:8000/api

## how to test

run `docker-compose exec oraculo-api python manage.py test`

## how to create and apply migrations

create migration
run `docker-compose exec oraculo-api python manage.py makemigrations`

apply migration
run `docker-compose exec oraculo-api python manage.py migrate`

## add sample data in local ou development environment

run `docker-compose exec oraculo-api python manage.py loaddata sample-data.json`
