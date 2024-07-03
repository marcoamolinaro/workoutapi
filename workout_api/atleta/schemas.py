from typing import Annotated
from pydantic import Field, PositiveFlot

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field('Nome do Atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field('CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field('Idade do Atleta', example=25)]
    peso: Annotated[PositiveFlot, Field('Peso do Atleta', example=75.5)]
    altura: Annotated[PositiveFlot, Field('Altura do Atleta', example=1.78)]
    sexo: Annotated[str, Field('Sexo do Atleta', example='M', max_length=1)]
