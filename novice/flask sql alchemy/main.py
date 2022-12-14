from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hda182526@localhost:5432/contoh'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f"<User {self.username}>"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        input = User(username=username, email=email)
        db.session.add(input)
        db.session.commit()
        print(username, email)
        
    data = User.query.all()
    return render_template("index.html", context=data)

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        admin = User.query.filter_by(username='admin').first()
        admin.email = 'my_new_email@example.com'
        db.session.commit()

        user = User.query.get(5)
        user.name = 'New Name'
        db.session.commit()

    return render_template("update.html")



if __name__ == "__main__":
    db.create_all()
    app.run(port=8080)