from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('My work experience')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(300), nullable=False)
    term = db.Column(db.Integer, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    # Добавляем ограничение на таблицу
    __table_args__ = (
        db.CheckConstraint('term > 0', name='check_term_positive'),
        db.CheckConstraint("length(company) > 0", name='check_company_not_empty'),
        db.CheckConstraint("length(term) > 0", name='check_term_not_empty')
    )

    def __repr__(self):
        return f'work{self.id}. {self.company} - {self.term} rub.'


@app.route('/')
def main():
    works = Work.query.all()
    return render_template('index.html', works_list=works)


@app.route('/in_stock/<company_id>', methods=['PATCH'])
def modify_work(company_id):
    work = Work.query.get(company_id)
    work.in_stock = request.json['in_stock']
    db.session.commit()

@app.route('/add', methods=['POST'])
def add_work():
    data = request.json
    work = Work(**data)
    db.session.add(work)
    db.session.commit()

    return 'OK'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)