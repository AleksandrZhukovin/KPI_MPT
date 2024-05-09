# MVVM (Model-View-ViewModel) pattern

### Run
Run `pip install -r requrements.txt` to install required packages.<br>
Run
```
flask db init
flask db migrate
flask db upgrade
```
to start database.<br>
Run `flask run` from *lab2.2* dir to start server

### Structure
- **Model** is `Post` class in **models.py** which represents model for database table for storing posts
- **View** is **index.html** in *templates* dir which is responsible for UI
- **ModelView** is `IndexView` class in **views.py** which controls requests and data creation with help of `route` decorator