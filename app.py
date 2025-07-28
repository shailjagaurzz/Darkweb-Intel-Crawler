from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from crawler.parser import parse_leaks
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leak_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Leak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100))
    emails = db.Column(db.Text)
    passwords = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    leaks = {}
    history = Leak.query.order_by(Leak.id.desc()).limit(5).all()

    if request.method == 'POST':
        keyword = request.form.get('keyword').strip()

        if not keyword:
            flash('Please enter a keyword (email, name, etc.)', 'warning')
            return render_template('index.html', leaks=leaks, history=history)

        leaks = parse_leaks(keyword)

        if leaks.get('emails') or leaks.get('passwords'):
            flash('⚠️ Data leak detected!', 'danger')

            new_leak = Leak(
                keyword=keyword,
                emails=", ".join(leaks.get('emails', [])),
                passwords=", ".join(leaks.get('passwords', []))
            )
            db.session.add(new_leak)
            db.session.commit()
        else:
            flash('✅ No leak found.', 'success')

    return render_template('index.html', leaks=leaks, history=history)

if __name__ == '__main__':
    app.run(debug=True)
