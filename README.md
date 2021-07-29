[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mmanchev23/healthy-at-home2/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mmanchev23/healthy-at-home2/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com)

# **Healthy at Home 2**

## **Rework of ["Healthy at Home"](https://github.com/mmanchev23/healthy-at-home)**

### **Technologies**
<ul>
    <li>
        Programming Languages - Python, Javascript, HTML5, CSS3
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
        <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Frameworks, Platforms and Libraries - Django, React.js, Node.js, NPM
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
        <img alt="React" src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"/>
        <img alt="Node.js" src="https://img.shields.io/badge/node.js-%2343853D.svg?style=for-the-badge&logo=node.js&logoColor=white"/>
        <img alt="NPM" src="https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white"/>
    </li>
    <li>
        API/Testing - Django Rest Framework, Postman
        <br/>
        <img alt="DjangoREST" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
        <img alt="Postman" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=red" />
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Deployment - Heroku and Vercel
        <br/>
        <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
        <img alt="Vercel" src="https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDEs - Visual Studio Code, PyCharm Community Edition
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
        <img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
    </li>
</ul>

### **How to start the backend application locally?**
<ol>
    <li>
        You should install Python in order to run the app.
        <br/>
        <code>
            <u>https://www.python.org/downloads/</u>
        </code>
    </li>
    <li>
        Open the project in console, IDE or text editor.
    </li>
    <li>
        Install virtual environment (if you haven't already!!!) in the backend folder. My virtual environment of choice is "Pipenv", but feel free to use other as well.
        <br/>
        <code>
            pip install pipenv
        </code>
    </li>
    <li>
        Open the virtual environment.
        <br/>
        <code>
            pipenv shell
        </code>
    </li>
    <li>
        Install the required packages:
        <br/>
        <code>
            pipenv install -r requirements.py
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. python manage.py makemigrations
        </code>
        <br/>
        <code>
            2. python manage.py migrate
        </code>
        <br/>
        <code>
            3. python manage.py runserver
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            <u>http://127.0.0.1:8000/</u>
        </code>
    </li>
</ol>

### **How to start the frontend application locally?**
<ol>
    <li>
        You should install Node.js in order to run the app.
        <br/>
        <code>
            <u>https://nodejs.org/en/download/</u>
        </code>
    </li>
    <li>
        Navigate to the frontend folder
        <br/>
        <code>
            cd frontend
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. npm install
        </code>
        <br/>
        <code>
            2. npm start
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            <u>http://localhost:3000/</u>
        </code>
    </li>
</ol>

### **Files & Directories**
- `backend` - backend application folder
  - `api` - app folder
  - `backend` - project folder
  - `db.sqlite3` - the database
  - `manage.py` - the startpoint file
  - `Pipfile` - the virtual environment
  - `Pipfile.lock` - the lock for the virtual environment
  - `Procfile` - the main deployment file
  - `requirements.txt` - the file container for all the necessery packages
- `frontend` - frontend application folder
  - `public` - static files folder
  - `src` - components folder
  - `.gitignore` - git ignore file
  - `package-lock.json` - lock for the node.js and npm environment
  - `package.json` - node.js and npm environment
- `LICENSE` - license file
- `README.md` - documentation file
