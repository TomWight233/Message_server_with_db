
import os
import psycopg
from flask import Flask, request, redirect, url_for, render_template
from markupsafe import escape

# We're going to write a function that constructs an URL for the database
def get_database_url():
    # The app can run in two 'modes' — production mode, or development mode.
    # This is determined by the `APP_ENV` environment variable.
    # Having dev and production modes is quite a common pattern and you will
    # see it in many real-world applications.
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url.replace("postgres://", "postgresql://", 1)
    

# We're going to write a function that sets up the database with the right table
def setup_database(url):
    # We connect using the URL
    connection = psycopg.connect(url)

    # Get a 'cursor' object that we can use to run SQL
    cursor = connection.cursor()

    # Execute some SQL to create the table
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (message TEXT);")
    cursor.execute("INSERT INTO messages (message) VALUES ('first message');")

    # And commit the changes to ensure that they 'stick' in the database.
    connection.commit()

# We run the two functions above
POSTGRES_URL = get_database_url()
setup_database(POSTGRES_URL)

app = Flask(__name__)

@app.route('hello')
def get_hello():
    return "Hello world!"



if __name__ == '__main__':
    # We also run the server differently depending on the environment.
    # In production we don't want the fancy error messages — users won't know
    # what to do with them. So no `debug=True`
    if os.environ.get("APP_ENV") == "PRODUCTION":
        app.run(port=5000, host='0.0.0.0')
    else:
        app.run(debug=True, port=5000, host='0.0.0.0')
