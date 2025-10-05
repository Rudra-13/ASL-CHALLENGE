from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
import os
import configparser
# FLASK APP SETUP
# -------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 🔧 FIXED: Explicitly tell Flask where templates and static folders are
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
app.secret_key = "supersecretkey"

# Ensure instance folder exists
os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'site.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# -------------------------
# LOAD ADMIN CONFIG FROM FILE
# -------------------------
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "config.ini"))
ADMIN_USERNAME = config["admin"]["username"]
ADMIN_PASSWORD = config["admin"]["password"]

# -------------------------
# CREATE TABLES IF NEEDED
# -------------------------
with app.app_context():
    db.create_all()
# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken. Please choose another.", "danger")
            return redirect(url_for("register"))

        # Hash password
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(
            username=username,
            password=hashed_password,
            role="user",
            name=request.form.get("name"),
            gender=request.form.get("gender"),
            age=request.form.get("age"),
            department=request.form.get("department"),
            position=request.form.get("position"),
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("auth/register.html")



# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check DB for user (including admin)
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["username"] = user.username
            session["role"] = user.role
            flash(f"Welcome {user.role.title()}!", "success")
            return redirect(url_for("datalist"))

        flash("Invalid credentials", "danger")

    return render_template("auth/login.html")


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have logged out.", "info")
    return redirect(url_for("home"))


# -------------------------
# DATALIST
# -------------------------
@app.route("/datalist")
def datalist():
    users = User.query.all()
    return render_template("datalist.html", users=users, role=session.get("role"))


# -------------------------
# CRUD (Only for Admin)
# -------------------------
@app.route("/create", methods=["GET", "POST"])
def create():
    if session.get("role") != "admin":
        flash("Only admin can add employees.", "danger")
        return redirect(url_for("datalist"))

    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"], method="pbkdf2:sha256")

        new_user = User(
            username=username,
            password=password,
            role="user",
            name=request.form.get("name"),
            gender=request.form.get("gender"),
            age=request.form.get("age"),
            department=request.form.get("department"),
            position=request.form.get("position"),
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Employee added!", "success")
        return redirect(url_for("datalist"))

    return render_template("createpage.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if session.get("role") != "admin":
        flash("Only admin can update employees.", "danger")
        return redirect(url_for("datalist"))

    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.name = request.form.get("name")
        user.gender = request.form.get("gender")
        user.age = request.form.get("age")
        user.department = request.form.get("department")
        user.position = request.form.get("position")
        db.session.commit()
        flash("Employee updated!", "success")
        return redirect(url_for("datalist"))

    return render_template("update.html", user=user)


@app.route("/delete/<int:id>")
def delete(id):
    if session.get("role") != "admin":
        flash("Only admin can delete employees.", "danger")
        return redirect(url_for("datalist"))

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Employee deleted!", "info")
    return redirect(url_for("datalist"))


# -------------------------
# ERRORS
# -------------------------
@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html"), 500


# -------------------------
# APP INIT + ADMIN SEED
# -------------------------
if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists("site.db"):
            db.create_all()

        # 👇 Ensure admin always exists
        if not User.query.filter_by(username="admin").first():
            admin_user = User(
                username="admin",
                password=generate_password_hash("admin123", method="pbkdf2:sha256"),
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()

    app.run(debug=True)
