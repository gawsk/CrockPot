from flask import Flask, render_template
from flaskext.mysql import MySQL
import settings

app = Flask(__name__)




@app.route("/")
def main():
    # Initialize SQL server
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = settings.DB_USER
    app.config['MYSQL_DATABASE_PASSWORD'] = settings.DB_PASSWORD
    app.config['MYSQL_DATABASE_DB'] = settings.DB_DATABASE
    app.config['MYSQL_DATABASE_HOST'] = settings.DB_HOST
    mysql.init_app(app)

    # Connect to the Database
    conn = mysql.connect()

    # To query information in the database
    cursor = conn.cursor()



    return render_template('index.html')


if __name__ == "__main__":
    app.run()
