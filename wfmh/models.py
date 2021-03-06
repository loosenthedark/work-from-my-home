from wfmh import bcrypt, db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return Worker.query.get(int(user_id))


class Worker(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    profile_name = db.Column(db.String(length=20), nullable=False, unique=True)
    worker_email = db.Column(db.String(length=50), nullable=False, unique=True)
    worker_password = db.Column(db.String(length=60), nullable=False)
    wallet = db.Column(db.Integer(), nullable=False, default=1000)
    homes = db.relationship("Home", backref="wfmh_worker", lazy=True)

    def __repr__(self):
        return f"Worker {self.id}: {self.profile_name}"

    @property
    def format_wallet(self):
        return f"€{self.wallet:,}"

    @property
    def make_password_secure(self):
        return self.make_password_secure

    @make_password_secure.setter
    def make_password_secure(self, unhashed_password):
        self.worker_password = bcrypt.generate_password_hash(unhashed_password).decode(
            "utf-8"
        )

    def check_password_attempt(self, password_attempt):
        return bcrypt.check_password_hash(self.worker_password, password_attempt)

    def has_sufficient_funds(self, home_obj):
        return self.wallet >= home_obj.daily_rate

    def has_previously_booked_home(self, home_obj):
        return home_obj in self.homes


def mydefault(context):
    return str(context.get_current_parameters()['location'])

class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    summary = db.Column(db.String(length=50), nullable=False, unique=True)
    location = db.Column(db.String(length=25), nullable=False)
    owner_email = db.Column(db.String(length=50), nullable=False)
    daily_rate = db.Column(db.Integer(), nullable=False)
    reserved_by = db.Column(db.Integer(), db.ForeignKey("worker.id"))

    def __repr__(self):
        return f"Home {self.id}: {self.summary}"

    def __init__(self, summary, location, owner_email, daily_rate, reserved_by):
        self.summary = summary
        self.location = location
        self.owner_email = owner_email
        self.daily_rate = daily_rate
        self.reserved_by = reserved_by

    def book(self, user):
        self.reserved_by = user.id
        user.wallet -= self.daily_rate
        db.session.commit()

    def cancel(self, user):
        self.reserved_by = None
        user.wallet = self.daily_rate
        db.session.commit()
