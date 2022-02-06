from wfmh import db

class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    summary = db.Column(db.String(length=50), nullable=False, unique=True)
    location = db.Column(db.String(length=25), nullable=False)
    owner_email = db.Column(db.String(length=50), nullable=False)
    daily_rate = db.Column(db.Integer(), nullable=False)
    # worker = db.Column(db.Integer(), db.ForeignKey('worker.id'))

    def __repr__(self):
        return f'Home {self.id}: {self.summary}'
