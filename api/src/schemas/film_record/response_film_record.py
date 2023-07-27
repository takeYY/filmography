# 外部ライブラリ
from pydantic import BaseModel, Field, validator
from schemas.film_record.create.film.film_create_model import FilmCreateModel

# 独自ライブラリ
from src.domain.film_record.appreciation import AppreciationStatusEnum
from src.schemas.film_record.appreciation import FilmAppreciationCreateModel, FilmAppreciationModel
from src.schemas.film_record.film import FilmModel


class FilmRecordIdModel(BaseModel):
    value: str = Field(description="映画記録のID", example="1")


class FilmRecordResult(BaseModel):
    film_record_id: FilmRecordIdModel
    appreciation_status: str = Field(description="鑑賞状況", example="鑑賞済み")
    evaluation: int = Field(description="評価", example=5)
    note: str = Field(description="感想など", example="最高のエンターテインメント作品！")
    film: FilmModel
    film_appreciations: list[FilmAppreciationModel]


class FilmRecordResponse(BaseModel):
    """映画記録の単一レスポンス"""

    status: str = Field(description="ステータス", example="success", default="success")
    result: FilmRecordResult


class FilmRecordSystemError(BaseModel):
    status: str = Field(description="ステータス", default="error", example="error")
    error: str = Field(description="エラー情報", default="システムエラー", example="システムエラー")


class FilmRecordsResponse(BaseModel):
    """映画記録の複数レスポンス"""

    status: str = Field(description="ステータス", example="success", default="success")
    results: list[FilmRecordResult]


class FilmRecordCreateResult(BaseModel):
    """FilmRecordCreateModel -> FilmRecordCreateResult に変えた
    他のファイルにも適用させたい
    """

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


class FilmRecordCreateResponse(BaseModel):
    status: str = Field(description="ステータス", example="success", default="success")
    result: FilmRecordCreateResult
