from fastapi import APIRouter, HTTPException
import pandas as pd
import io
from fastapi.responses import PlainTextResponse
from inewave.newave import Clast
from app.models.clast import ClastGenerateModel
from app.templates.newave.clast import ClastTemplate

router = APIRouter(
    prefix="/newave",
    tags=["newave"],
)


@router.post("/clast", response_class=PlainTextResponse)
async def generate(
    data: ClastGenerateModel,
):
    # Tratamento de exceções mais simples possível.
    try:
        arq = Clast.read("".join(ClastTemplate))
        arq.usinas = pd.DataFrame(data.usinas.model_dump())
        arq.modificacoes = pd.DataFrame(data.modificacoes.model_dump())
        buffer = io.StringIO()
        arq.write(buffer)
        return buffer.getvalue()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro na geração do arquivo clast.dat: {e}",
        )
