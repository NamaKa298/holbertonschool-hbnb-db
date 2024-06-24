from datetime import datetime
from uuid import uuid4
from src import db
from typing import Any
from abc import abstractmethod


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36),
                   primary_key=True, default=lambda: str(uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def get(cls, id) -> "Any | None":
        from src.persistence import db

        return db.get(cls.__name__.lower(), id)

    @classmethod
    def get_all(cls) -> list["Any"]:
        from src.persistence import db

        return db.get_all(cls.__name__.lower())

    @classmethod
    def delete(cls, id) -> bool:
        from src.persistence import db

        obj = cls.get(id)

        if not obj:
            return False

        return db.delete(obj)

    @abstractmethod
    def to_dict(self) -> dict: ...

    @staticmethod
    @abstractmethod
    def create(data: dict) -> Any: ...

    @staticmethod
    @abstractmethod
    def update(entity_id: str, data: dict) -> Any | None: ...
