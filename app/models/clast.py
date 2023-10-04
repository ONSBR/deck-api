from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class ClastUsinasModel(BaseModel):
    """ """

    codigo_usina: List[int]
    nome_usina: List[str]
    tipo_combustivel: List[str]
    indice_ano_estudo: List[int]
    valor: List[float]


class ClastModificacoesModel(BaseModel):
    """ """

    codigo_usina: List[int]
    nome_usina: List[str]
    data_inicio: List[date]
    data_fim: List[Optional[date]]
    custo: List[float]


class ClastGenerateModel(BaseModel):
    """ """

    usinas: ClastUsinasModel
    modificacoes: ClastModificacoesModel
