from flask import Flask, render_template
import settings

app = Flask(__name__)




@app.route("/")
def main():
    # Initialize SQL server
    app.config['MYSQL_DATABASE_USER'] = DB_USER
    app.config['MYSQL_DATABASE_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_DATABASE_DB'] = DB_NAME
    app.config['MYSQL_DATABASE_HOST'] = DB_HOST
    mysql.init_app(app)

    # Connect to the Database
    conn = mysql.connect()

    # To query information in the database
    cursor = conn.cursor()



    return render_template('index.html')


if __name__ == "__main__":
    app.run()
