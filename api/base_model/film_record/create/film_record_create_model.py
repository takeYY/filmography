from base_model.film_record.create.appreciation.film_appreciation_create_model import FilmAppreciationCreateModel
from base_model.film_record.create.film.film_create_model import FilmCreateModel
from pydantic import BaseModel, Field, validator
from src.domain.film_record.appreciation import AppreciationStatusEnum


class FilmRecordCreateModel(BaseModel):
    appreciation_status: AppreciationStatusEnum = Field(
        default=AppreciationStatusEnum.NOT_WATCHED,
        example=AppreciationStatusEnum.WATCHED,
        description="映画の鑑賞状況. [鑑賞済み, 未鑑賞]のどちらかを取る.",
    )
    evaluation: int = Field(
        default=0,
        example=4,
        description="映画に対する自身の評価. 0より大きい数字である必要がある.",
        gt=0,
        le=5,
    )
    note: str | None = Field(
        default=None,
        example="とっても良かった",
        description="映画に対する自身の思い.",
        max_length=300,
    )
    film: FilmCreateModel = Field(
        description="映画createモデル",
    )
    appreciations: list[FilmAppreciationCreateModel] = Field(
        default=[],
        description="映画鑑賞",
    )

    @validator("appreciation_status")
    def validate_appreciation_status(cls, v: AppreciationStatusEnum):
        if not v:
            raise ValueError("appreciation_status is required.")

        return v

    @validator("film")
    def validate_film(cls, v: FilmCreateModel):
        if not v:
            raise ValueError("film is required.")

        return v
