from pydantic import BaseModel
from typing import Optional

class ContenidoBase(BaseModel):
    titulo: str
    descripcion: Optional[str]
    fechaLanzamiento: str
    idGenero: str
    valoracionPromedio: Optional[float] = None
    idSubtitulosContenido: Optional[str] = None
    idDoblajeContenido: Optional[str] = None
    tipoContenido: str

    duracion: Optional[int]
    idDirector: Optional[str]

class ContenidoCreate(ContenidoBase):
    tipoContenido: str

class ContenidoUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    fechaLanzamiento: Optional[str] = None
    idGenero: Optional[str] = None
    valoracionPromedio: Optional[float] = None
    idSubtitulosContenido: Optional[str] = None
    idDoblajeContenido: Optional[str] = None

class Contenido(ContenidoBase):
    id: str #Generado Automaticamente
    class Config:
        from_attributes = True
    
class PeliculaUpdate(ContenidoUpdate):
    duracion: Optional[int] = None
    idDirector: Optional[str] = None
    class Config:
        from_attributes = True   

class SerieUpdate(ContenidoUpdate):
    pass
    class Config:
            from_attributes = True

class PeliculaCreate(ContenidoBase):
    duracion: int
    idDirector: str
    class Config:
        from_attributes = True

class Pelicula(ContenidoBase):
    id: str
    class Config:
        from_attributes = True

class SerieCreate(ContenidoBase):
    pass

class TemporadaBase(BaseModel):
    numeroTemporada: int

class TemporadaCreate(TemporadaBase):
    pass

class Temporada(TemporadaBase):
    idTemporada: str  # Generado automáticamente
    idContenido: str
    class Config:
        from_attributes = True


class EpisodioBase(BaseModel):
    idDirector: str
    numeroEpisodio: int
    duracion: int  # En minutos

class EpisodioCreate(EpisodioBase):
    pass

class Episodio(EpisodioBase):
    idEpisodio: str  # Generado automáticamente
    idContenido: str
    idTemporada: str
    class Config:
        from_attributes = True

class GeneroBase(BaseModel):
    nombre: str
    descripcion: str

class GeneroCreate(GeneroBase):
    pass

class GeneroUpdate(GeneroBase):
    pass

class Genero(GeneroBase):
    id: str # Generado automáticamente

    class Config:
        from_attributes = True

class TemporadasGet(BaseModel):
    idTemporada: str
    numeroTemporada: int
    Episodios: list[Episodio]

class SeriesGet(BaseModel):
    idSerie: str
    titulo: str
    Temporadas: list[TemporadasGet]

class TemporadaUpdate(BaseModel):
    numeroTemporada: Optional[int]

class EpisodioUpdate(BaseModel):
    numeroEpisodio: Optional[int] = None
    duracion: Optional[int] = None
    idDirector: Optional[str] = None

class Reparto(BaseModel):
    idContenido: str
    idActor: str

class RepartoUpdate(BaseModel):
    idActor: str

class Actor(BaseModel):
    id: str
    nombre: str
    nacionalidad: str
    fechaNacimiento: str

class ActorCreate(BaseModel):
    nombre: str
    nacionalidad: str
    fechaNacimiento: str

class ActorUpdate(BaseModel):
    nombre: str
    nacionalidad: str
    fechaNacimiento: str        

class Director(BaseModel):
    id: str
    nombre: str
    nacionalidad: str
    fechaNacimiento: str

class DirectorCreate(BaseModel):
    nombre: str
    nacionalidad: str
    fechaNacimiento: str

class DirectorUpdate(DirectorCreate):
    pass    