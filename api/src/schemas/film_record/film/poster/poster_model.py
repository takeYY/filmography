# 外部ライブラリ
from pydantic import BaseModel, Field


class FilmPosterModel(BaseModel):
    poster_url: str = Field(description="映画のポスターURL", example="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg")
