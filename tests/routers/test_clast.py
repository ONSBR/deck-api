from inewave.newave import Clast
from app.app import get_app
from app.models.clast import (
    ClastUsinasModel,
    ClastModificacoesModel,
    ClastGenerateModel,
)
import pandas as pd
from fastapi.testclient import TestClient
from datetime import date


app = get_app(".")
client = TestClient(app)


def test_generate_clast():
    filepath = "./tests/mocks/files/clast.dat"
    fs_arq = Clast.read(filepath)
    # Converte o objeto Timestamp do pandas, padrão do DataFrame,
    # para string como data, para serializar na request
    df = fs_arq.modificacoes.copy()
    df["data_inicio"] = df["data_inicio"].apply(
        lambda d: d.date().isoformat() if not pd.isna(d) else None
    )
    df["data_fim"] = df["data_fim"].apply(
        lambda d: d.date().isoformat() if not pd.isna(d) else None
    )
    # Confere que o arquivo lido a partir do gerado via API
    # é igual ao lido do arquivo.
    res = client.post(
        "/newave/clast",
        json={
            "usinas": fs_arq.usinas.to_dict(orient="list"),
            "modificacoes": df.to_dict(orient="list"),
        },
    )
    assert res.status_code == 200
    lines = res.text.strip('"')
    fs_req = Clast.read(lines)
    # with open("teste.dat", "w") as arq:
    #     arq.write(lines)
    assert fs_arq == fs_req
