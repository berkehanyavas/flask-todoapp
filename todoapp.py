from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/berke/Desktop/kodlama/todo app/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bitti = db.Column(db.Boolean)
    
@app.route("/")
def index():
    gorevler = Todo.query.all()
    return render_template("index.html",gorevler = gorevler)

@app.route("/ekle",methods = ["POST"])
def Todoekle():
    title = request.form.get("title")
    yenigorev = Todo(title = title, bitti = False)
    db.session.add(yenigorev)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/bitti/<string:id>")
def gorevbitir(id):
    gorev = Todo.query.filter_by(id = id).first()
    gorev.bitti = not gorev.bitti
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/sil/<string:id>")
def gorevsil(id):
    gorev = Todo.query.filter_by(id=id).first()
    db.session.delete(gorev)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)