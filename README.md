# Authentication on Flask using Postgresql - Beginner

## Setting up

### Venv

```bash
# create a ven

python3 -m venv "nameofyourvenv"

# activate a ven

source myvenv/bin/activate
```

### Postgres
```psql
# create the db

CREATE DATABASE authflask
GRANT ALL PRIVILEGES ON DATABASE authflask TO youruser;

# create table

CREATE SEQUENCE accounts_id_seq START 1;

CREATE TABLE accounts ( 
    id INT DEFAULT nextval('accounts_id_seq') PRIMARY KEY, 
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(255) NOT NULL, 
    email VARCHAR(100) NOT NULL
);

# to connect to database

psql -U youruser yourdb
```

### Flask app

```
# in venv activated
pip install Flask psycopg2-binary
```

# Launch project
```python
export POSTGRES_USER='youruser'
export POSTGRES_PASSWORD='yourpassword'
python3 app.py
```

# Documentation

- https://flask.palletsprojects.com/en/2.3.x/
- https://pypi.org/project/psycopg2/
