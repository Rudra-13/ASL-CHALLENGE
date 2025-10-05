# 🧾 Employee Data Management System (REST QUESTIONS AFTER THIS README FILE)

A full-featured **Flask-based web application** for managing employee data with secure authentication, role-based access control, and CRUD functionality.  
Built using **Python, Flask, Flask-Login, SQLite3, SQLAlchemy**, and **Werkzeug security utilities**. 

---

## 🚀 Project Overview

The **Employee Data Management System** is designed to simplify the process of managing employee information while ensuring **data integrity**, **security**, and **role-based access**.

### ✨ Key Highlights

- 🔐 **Secure Authentication System** using `werkzeug.security` password hashing.
- 👨‍💼 **Admin Role** – Has full control (Create, Read, Update, Delete employees).
- 👤 **User Role** – Can register, log in, and view employee details (read-only access).
- 🗃️ **SQLite3 Database** – Lightweight, fast, and fully integrated with SQLAlchemy ORM.
- ⚙️ **Flask-Login** for managing user sessions and authentication.
- 🎨 **Bootstrap 5 UI** for a modern and responsive frontend.
- 🧩 **Error Handling** for duplicate entries and validation issues.

---

## 🧠 How It Works

- The project starts with a **Welcome Page** offering two options:  
  👉 *Login* or *Register*.

- The **Admin** is a predefined permanent member of the system:  
Username: admin
Password: admin123

yaml
Copy code

- Once logged in, the **Admin** can:
- Add new employees
- Edit existing employee data
- Delete employees
- View all employee records

- A **User**, once registered, can log in and view the list of employees but **cannot perform CRUD operations** — implementing both **authentication and authorization** cleanly.

- All passwords are stored in a **securely hashed** format using `generate_password_hash()` and verified via `check_password_hash()`.

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|-----------|-------------------|
| **Backend** | Python, Flask |
| **Database** | SQLite3, SQLAlchemy ORM |
| **Authentication** | Flask-Login, Werkzeug Security |
| **Frontend** | HTML, CSS, Bootstrap 5 |
| **Other** | Jinja2 Templates |

---

## ⚙️ Setup & Run Instructions (Local Environment)

Follow these steps to run the project locally on your system:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/employee-data-management.git
cd employee-data-management

2️⃣ Create a Virtual Environment
Windows:
python -m venv crud
crud\Scripts\activate

macOS/Linux:
python3 -m venv crud
source crud/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
(If requirements.txt doesn’t exist, generate one using pip freeze > requirements.txt)

4️⃣ Initialize the Database
python
Then run:

from app import db
db.create_all()
exit()

5️⃣ Add Default Admin

python
from app import db
from models import User
admin = User(username='admin', role='admin')
admin.set_password('admin123')
db.session.add(admin)
db.session.commit()
exit()


6️⃣ Run the Application
python app.py

7️⃣ Access the Web App
Open your browser at:
👉 http://127.0.0.1:5000

🧭 Usage Flow
Role	Capabilities
Admin	Full CRUD on employee data
User	Can register/login and view employee list (read-only)

####Q.1 A brief description of the project?

ANS. 🧠 Project Title:

Employee Data Management System — Flask | Python | SQLite | Authentication & Authorization

🚀 Brief Description

The Employee Data Management System is a secure, full-stack web application built using Flask (Python framework) that allows efficient management of employee records with proper authentication, authorization, and role-based access control.

This project demonstrates my ability to design, develop, and deploy a complete CRUD-based web system that integrates database management, user authentication, and admin-level control, ensuring both functionality and data integrity.

💡 Key Features
🔐 User Authentication & Security

Implemented secure login and registration using Flask-Login and Werkzeug Security.

Passwords are encrypted using generate_password_hash() before being stored in the database — ensuring data confidentiality and protection against breaches.

Prevented duplicate registration and ensured unique username constraints via SQLAlchemy ORM validation.

👨‍💼 Role-Based Access (Admin vs User)

The Admin (default: username → admin, password → admin123) can:

Perform all CRUD operations (Create, Read, Update, Delete) on employee data.

Manage employee details such as Name, Gender, Age, Department, and Position.

The User, after registration and login, has read-only access to the employee list — ensuring proper authorization control and data security.

🖥️ Frontend Experience

Simple and responsive UI built with HTML, CSS, and Bootstrap for a clean and user-friendly interface.

The homepage welcomes the user with options to Login or Register.

Role-based navigation dynamically changes according to user privileges (Admin/User).

🧩 Backend Logic

Developed using Flask with structured routing (@app.route) for modular navigation.

SQLite3 serves as the backend database — lightweight yet efficient for this scale.

SQLAlchemy ORM used to interact with the database — eliminating raw SQL queries and ensuring security and maintainability.

Implemented error handling pages (403, 404, 500) for enhanced user experience and debugging.

⚙️ Technology Stack
Category	Technologies Used
Language	Python
Framework	Flask
Database	SQLite3
ORM	SQLAlchemy
Security	Werkzeug (Password Hashing), Flask-Login
Frontend	HTML5, CSS3, Bootstrap
Tools	VS Code, Flask CLI
📈 Highlights & Learning

Built a secure multi-role authentication system using Flask’s session management.

Strengthened knowledge in Flask blueprints, form handling, and Flask-SQLAlchemy integration.

Gained experience in implementing real-world authorization flow and database-driven user management.

Understood how to handle IntegrityErrors, database constraints, and session persistence effectively.

🎯 Outcome

This project is a strong demonstration of my:

Backend development skills using Flask and Python.

Understanding of database design, authentication systems, and secure coding practices.

Ability to create scalable, well-structured, and user-friendly applications — a critical skill for any backend or full-stack development role.

###Q.2 Clear instructions on how to set up and run it locally ?
ANS. ⚙️ Setup & Run Instructions (Local Environment)

Follow these steps to set up and run the Employee Data Management System locally on your machine:

🪜 1. Clone the Repository
git clone https://github.com/yourusername/employee-data-management.git
cd employee-data-management


(If this is not yet on GitHub, replace with your local project folder path.)

🧱 2. Create a Virtual Environment

Create and activate a virtual environment to isolate dependencies.

For Windows:

python -m venv crud
crud\Scripts\activate



📦 3. Install Dependencies

Install all required Python packages:

pip install -r requirements.txt


(If you don’t have a requirements.txt file yet, you can create one by running:)

pip freeze > requirements.txt

🧩 4. Initialize the Database

Open Python shell (inside your virtual environment):

python


Then run the following:

from app import db
db.create_all()
exit()


This will create the database.db (SQLite) file.

🔑 5. Add Default Admin User

In the same Python shell:

from app import db
from models import User
admin = User(username='admin', role='admin')
admin.set_password('admin123')
db.session.add(admin)
db.session.commit()
exit()


Now you have a default Admin with:

Username: admin

Password: admin123

🚀 6. Run the Application

Start the Flask development server:

python app.py


or

flask run

🌐 7. Access the Application

Open your browser and go to:
👉 http://127.0.0.1:5000

🧭 8. Usage

Admin: Login using admin / admin123 to manage employees (CRUD operations).

User: Register a new account to view the employee list (read-only access).


###Q.Instructions on how to run your test cases?
ANS. Testing the Application

This project includes automated tests written using pytest to ensure key functionalities like registration, login, and CRUD operations work as expected.

✅ 1️⃣ Install Test Dependencies

Make sure pytest and Flask-Testing are installed:

pip install pytest Flask-Testing

✅ 2️⃣ Directory Structure (Recommended)

Place your test file in a folder named tests/:

project_root/
│
├── app.py
├── models.py
├── templates/
├── static/
├── tests/
│   └── test_app.py
└── requirements.txt

✅ 3️⃣ Example Test File (tests/test_app.py)

Here’s an example you can include to show recruiters how you validate your app logic:

import pytest
from app import app, db
from models import User
from werkzeug.security import check_password_hash

@pytest.fixture
def client():
    # Create a test client and an in-memory database
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        admin = User(username='admin', role='admin', password='hashedpass')
        db.session.add(admin)
        db.session.commit()
    yield app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ASL Challenge" in response.data or b"Employee" in response.data

def test_register_user(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)
    assert b"Registration successful" in response.data

def test_login_user(client):
    with app.app_context():
        user = User(username='loginuser', role='user', password='hashedpass')
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data={
        'username': 'loginuser',
        'password': 'hashedpass'
    }, follow_redirects=True)
    assert response.status_code == 200

✅ 4️⃣ Run the Tests

In your terminal, simply run:

pytest -v


-v stands for “verbose” mode for detailed output.

All tests inside the tests/ folder will automatically run.

You’ll see green ✅ for passing tests and red ❌ for failing ones.

✅ 5️⃣ Optional — Generate a Test Report

You can also generate an HTML report (useful for portfolio or team projects):

pip install pytest-html
pytest --html=report.html


Then open the generated report.html in your browser to see a clean, visual summary.

🧭 Testing Scope (Suggested)

You can write test cases for:

Test Area	Description
Registration	Verify new user creation and duplicate username prevention
Login	Validate correct credentials and password hashing
CRUD Operations	Ensure admin-only operations work correctly
Access Control	Confirm normal users can’t access restricted admin routes
Error Pages	Check if custom 403/404/500 pages render correctly

##Q.4 Any assumptions or design choices you made?
ANS.
Assumptions & Design Choices
-- Assumptions

Single Admin Account:

The system assumes one permanent admin user (username: admin, password: admin123).

The admin account is auto-created when the database initializes.

Employee and User Overlap:

Each employee record is associated with a user, but admin can manage all employee data regardless of creator.

Simple Authentication Flow:

Authentication is based on Flask-Login, assuming session-based management is sufficient for a local or small-scale deployment.

SQLite for Local Storage:

The project uses SQLite for simplicity and portability.

It’s assumed the app runs in a local or small-server environment, not under heavy concurrent load.

Limited Role Types:

Only two roles exist: admin (full CRUD permissions) and user (view-only access).

Form Validation:

Basic form validation (such as required fields and duplicate username checks) is handled at the Flask layer — not using client-side JavaScript frameworks.

---- Design Choices

Framework Selection – Flask
Flask was chosen for its lightweight nature, modularity, and suitability for smaller projects that can scale later with Blueprints.

Database Layer – SQLAlchemy ORM
SQLAlchemy allows smooth integration with Python objects and avoids manual SQL queries.
This decision ensures maintainability, type safety, and easier migration to other databases.

Security – Werkzeug + Flask-Login

Passwords are hashed using generate_password_hash() (PBKDF2-SHA256).

Passwords are never stored or transmitted in plain text.

Flask-Login is used to handle session management and user authentication securely.

User Experience (UX)

Clean, intuitive interface built with HTML/CSS and Jinja templates.

Admins can perform full CRUD operations, while users are limited to viewing their data.

Flash messages are used for instant feedback (e.g., “This username already exists”).

Error Handling

Duplicate username or database constraint violations are caught gracefully, flashing descriptive error messages instead of crashing the app.

Scalability Consideration

Although SQLite is used for now, the app can easily switch to MySQL or PostgreSQL with minor configuration changes in the database URI.

Code Organization

Separated logic into multiple files:

app.py → Main application routes and logic

models.py → Database models and helpers

templates/ → HTML front-end templates

static/ → CSS and JS files

Testing & Maintainability

Unit tests (using pytest) ensure functionality correctness and code reliability.

Modular design makes it easy to extend roles or add new models later.