# Crockpot
Software Design and Documentation Project




# Install
1.) Download pip  
2.) Install mysql  
3.) Install requirements.txt  
4.) Install MYSQL sql  
  ```
  sudo apt-get install python-pip python-dev build-essential
  sudo pip install --upgrade pip
  sudo pip install --upgrade virtualenv

  sudo apt-get install mysql-server


  sudo pip install -r requirements.txt

  mysql -u root -p < sample.sql
  root
  ```



# Running on localhost
If you haven't already, go to the directory where you installed installed Crockpot and run the following  
 ```
 export FLASK_APP=run
  export FLASK_CONFIG=development
  ```
  
To run the program use the following command: `flask run`  
Navigate to localhost:5000 to view the webpage  
If you update any of the code, you must re-run the command above.  
