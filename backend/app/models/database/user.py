from app.extensions import db, Model


class User(Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    tel = db.Column(db.VARCHAR(255), nullable=False, unique=True)
    sex = db.Column(db.VARCHAR(255), nullable=False)
    grade = db.Column(db.VARCHAR(255), nullable=False)
    campus = db.Column(db.VARCHAR(255), nullable=False)
    college = db.Column(db.VARCHAR(255), nullable=False)
    dormitory = db.Column(db.VARCHAR(255), nullable=False)
    first = db.Column(db.VARCHAR(255), nullable=False)
    second = db.Column(db.VARCHAR(255), nullable=False)
    adjust = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(255), nullable=False)

    def to_dict(self):
        return {**{c.name: getattr(self, c.name) for c in self.__table__.columns},
                'adjust': '是' if self.adjust else '否'}

    def to_list(self) -> list:
        return [x for x in self.to_dict().values()]
