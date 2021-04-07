from app.extensions import db, Model


class User(Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    phone = db.Column(db.VARCHAR(255), nullable=False, unique=True)
    sex = db.Column(db.VARCHAR(255), nullable=False)
    grade = db.Column(db.VARCHAR(255), nullable=False)
    campus = db.Column(db.VARCHAR(255), nullable=False)
    academy = db.Column(db.VARCHAR(255), nullable=False)
    domitory_info = db.Column(db.VARCHAR(255), nullable=False)
    first_aspiration = db.Column(db.VARCHAR(255), nullable=False)
    second_aspiration = db.Column(db.VARCHAR(255), nullable=False)
    if_adjustable = db.Column(db.Integer, nullable=False)
    self_intro = db.Column(db.VARCHAR(255), nullable=False)
    mail_address = db.Column(db.CHAR(30))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'tel': self.phone,
            'sex': self.sex,
            'grade': self.grade,
            'campus': self.campus,
            'college': self.academy,
            'dormitory': self.domitory_info,
            'first': self.first_aspiration,
            'second': self.second_aspiration,
            'adjust': self.if_adjustable,
            'description': self.self_intro,
            'mail': self.mail_address
        }

        # return {**{c.name: getattr(self, c.name) for c in self.__table__.columns},
        #         'adjust': '是' if self.adjust else '否'}

    def to_list(self) -> list:
        return [x for x in self.to_dict().values()]
