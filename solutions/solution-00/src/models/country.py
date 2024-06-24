from src.models.country import Country
from src.persistence import db
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = 'country'
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(3), primary_key=True)

    def __repr__(self) -> str:
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "code": self.code,
        }

    @classmethod
    def get_all(cls) -> list["Country"]:
        return cls.query.all()

    @classmethod
    def get(cls, code: str) -> "Country | None":
        return cls.query.filter_by(code=code).first()

    @classmethod
    def create(cls, name: str, code: str) -> "Country":
        country = cls(name=name, code=code)
        db.session.add(country)
        db.session.commit()
        return country
