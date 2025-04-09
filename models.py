from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
import database
import enum

class FormatEnum(str, enum.Enum):
    vinyle = "vinyle"
    dvd = "dvd"

class Musique(database):
    __tablename__ = "musiques"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    artiste = Column(String)
    immatriculation = Column(String, unique=True, index=True)
    format = Column(Enum(FormatEnum))
    type_musique = Column(String)
