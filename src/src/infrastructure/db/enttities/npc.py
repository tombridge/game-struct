from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NPCModel(Base):
    """Модель NPC для хранения в базе данных."""

    __tablename__ = "npcs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False, default=100)
    strength = Column(Integer, nullable=False, default=10)
    agility = Column(Integer, nullable=False, default=10)
    intelligence = Column(Integer, nullable=False, default=10)
    location = Column(String, nullable=False, default="unknown")

    def __repr__(self):
        return f"<NPC {self.id}: {self.name} ({self.health} HP) at {self.location}>"
