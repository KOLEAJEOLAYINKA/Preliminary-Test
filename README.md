# Bincom Test 🤹

A web-based platforms used to display individual polling unit and store all parties result <br />
<br />

### Setup 💻
After cloning repository,

- Install your virtual environment by running 
```{r}
python3 -m venv venvironment
```

-  Activate Your virtual environment on window by running
```{r}
venvironment\Scripts\activate
```

- Activate Your virtual environment on linux or mac os by running
```{r}
source venvname/bin/activate
```

- Assign Django secrete key to the variable in `.env.example` file

- Rename `.env.example` to `.env`

- install all required dependency by running 
```{r}
pip install Django
pip install mysqlclient
pip install python-dotenv
```
Verify the dependencies listed in the requirement.txt file located in the root directory for additional installations.

- merge migration  by running
```{r}
python3 manage.py makemigrate --merge
python3 manage.py migrate
```

- Run the Apllication 
```{r}
python3 manage.py runserver
```

**Note** In case you encounter an error after running the application, Create some entry in the DB and don't let your databease be empty if the error persists [Create issue in the repo](https://github.com/KOLEAJEOLAYINKA/Preliminary-Test/issues) 

### Technologies 🛠
- [Django](https://www.djangoproject.com/)
