from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# -------------------------
# USER MODEL
# -------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")  # admin / user
    
    # Employee fields (optional for normal users)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer)
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))

    # -------------------------
    # PASSWORD HELPERS
    # -------------------------
    def set_password(self, password):
        """Hashes and sets the password securely."""
        self.password = generate_password_hash(password, method="pbkdf2:sha256")

    def check_password(self, password):
        """Verifies password against stored hash."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"
