from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field('Nome do Atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field('CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field('Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field('Peso do Atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field('Altura do Atleta', example=1.78)]
    sexo: Annotated[str, Field('Sexo do Atleta', example='M', max_length=1)]
    
class AtletaIn(Atleta):
    pass
    
class AltetaOut(Atleta, OutMixin):
    pass
    

