# Ceramics_business_website
The site for the artist and ceramist contains photos of projects and their description (as well as the possibility of feedback). 
You can use this code to create your own site as a template.
You can find the website here: http://svetapokrovskaya.ru/

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

> Install Python(If it's not installed)<br>
> [Download Python3](https://www.python.org/downloads/)

Clone the repository:
```
git clone https://github.com/AlexanderZug/Ceramics_business_website.git
```

Go to folder:
```
cd Ceramics_business_website
```

Install requirements:
```
pip3 install -r requirements.txt
```

Create a file 'person_data.py' and indicate your data:

> TELEGRAM = your data
> 
> WHATS_UP = your data
> 
> VK = your data
> 
> SENTRY = your data
> 
> EMAIL_INFO = your data
> 
> MAIL_USERNAME = your data
> 
> MAIL_PASSWORD = your data
> 
> MAIL_DEFAULT_SENDER = your data
> 
> SECURITY_PASSWORD_SALT = your data

Start programm:
```
python3 app.py
```

Write the following commands in the terminal (being in the virtual environment of the project) 
to create a superuser (your admin) and assign it to the role:

> from app import db

> from admin import user_datastore

> user_datastore.create_user(email='test@test.test', password='admin')

> db.session.commit()

> from models import Role

> user = User.query.first()

> role = Role.query.first()

> user_datastore.add_role_to_user(user, role)

> db.session.commit()
