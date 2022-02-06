from wfmh import db


class Worker(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    profile_name = db.Column(db.String(length=20), nullable=False, unique=True)
    worker_email = db.Column(db.String(length=50), nullable=False, unique=True)
    worker_password = db.Column(
        db.String(length=60), nullable=False)
    wallet = db.Column(db.Integer(), nullable=False, default=1000)
    homes = db.relationship('Home', backref='wfmh_worker', lazy=True)

    def __repr__(self):
        return f'Worker {self.id}: {self.profile_name}'


class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    summary = db.Column(db.String(length=50), nullable=False, unique=True)
    location = db.Column(db.String(length=25), nullable=False)
    owner_email = db.Column(db.String(length=50), nullable=False)
    daily_rate = db.Column(db.Integer(), nullable=False)
    reserved_by = db.Column(db.Integer(), db.ForeignKey('worker.id'))

    def __repr__(self):
        return f'Home {self.id}: {self.summary}'
