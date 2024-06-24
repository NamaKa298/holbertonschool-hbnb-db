
from src.models.country import Country
from src.models.city import City
from src import db


class City(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, name: str, country_code: str, **kw) -> None:
        super().__init__(**kw)
        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        from src.persistence import db

        country = Country.get(data["country_code"])

        if not country:
            raise ValueError("Country not found")

        city = City(**data)

        db.session.add(city)
        db.session.commit()

        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        from src.persistence import db

        city = City.get(city_id)

        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        db.update(city)

        return city
