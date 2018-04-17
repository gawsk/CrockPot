# Crockpot
Software Design and Documentation Project




# Install
1.) Download pip
2.) Install mysql
3.) Install requirements.txt
4.) Install MYSQL sql
5.) Create instance folder and add 'config.py' inside
6.) Add a random secret key to 'config.py'
  ```
  sudo apt-get install python-pip python-dev build-essential
  sudo pip install --upgrade pip
  sudo pip install --upgrade virtualenv

  sudo apt-get install mysql-server


  sudo pip install -r requirements.txt

  mysql -u root -p < sample.sql
  root

  mkdir instance
  echo "SECRET_KEY = 'ENTER RANDOMIZED KEY HERE'" > instance/config.py
  ```


# Running on localhost
If you haven't already, go to the directory where you installed installed Crockpot and run the following
 ```
 export FLASK_APP=run.py
 export FLASK_CONFIG=development
  ```

To run the program use the following command: `flask run`
Navigate to localhost:5000 to view the webpage
If you update any of the code, you must re-run the command above.


For testing, use Selenium:
-Requires a webbrowser driver (Recommend PhantomJS headless browser)
  http://phantomjs.org/download.html
-Move to folder in PATH
  Ex: sudo mv phantomjs /usr/local/bin
-Recommend use Katalon Automation Recorder to help create testcases

