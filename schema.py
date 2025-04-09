from pydantic import BaseModel, field_validator
import re

class MusiqueBase(BaseModel):
    titre: str
    artiste: str
    immatriculation: str
    format: str
    type_musique: str

    @field_validator('immatriculation')
    def check_immatriculation(cls, v, values):
        pattern = r"^([A-Z]{2})/(\d{3})/(RAP|POP|RNB)/(\d{4})$"
        match = re.match(pattern, v)
        if not match:
            raise ValueError("Format d'immatriculation invalide")

        if 'artiste' in values:
            initiales = ''.join([a[0].upper() for a in values['artiste'].split()[:2]])
            if match.group(1) != initiales:
                raise ValueError("Initiales de l'artiste invalides")

        if not (60 <= int(match.group(2)) <= 300):
            raise ValueError("Durée de musique invalide")

        if '6' in match.group(4):
            raise ValueError("Identifiant invalide (ne doit pas contenir 6)")
        return v

class MusiqueCreate(MusiqueBase):
    pass

class Musique(MusiqueBase):
    id: int
    class Config:
        orm_mode = True
