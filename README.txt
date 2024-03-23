Docker Images:
    -Postgres
        --> docker pull postgres
        --> docker run --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

Install Dependencies
    - pip install -r requiremnets.txt

Migrate
    -flask db init
    -flask db migrate
    -flask db upgrade

Run App
    - cd src
    - flask run
        --debug