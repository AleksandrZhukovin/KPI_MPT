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
- **Model** is `Model` class in **models.py** which represents db operations
- **View** is IndexView class in **views.py** which is responsible for UI
- **ViewModel** is `ViewModel` class in **views.py** which processes requests