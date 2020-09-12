from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Meetme@01@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kqdlcjhbtoixgm:f7269af94791a77b8aeafe393ddc884d5dcd3acf3a0b1a2bbedcdd85feeaf82b@ec2-54-235-192-146.compute-1.amazonaws.com:5432/dfdkfv9ngp8934'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods=['POST'])
def proess():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))