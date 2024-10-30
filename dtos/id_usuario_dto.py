from pydantic import BaseModel, field_validator

from util.validators import *


class IdUsuarioDto(BaseModel):
    id: int

    @field_validator("id")
    def validar_id_usuario(cls, v):
        msg = is_greater_than(v, "Id do Usuário", 0)
        if msg: raise ValueError(msg)
        return v