# 外部ライブラリ
from pydantic import BaseModel, Field


class JumanppResult(BaseModel):
    mrph_index: int = Field(
        description="形態素のインデックス",
        example=1,
        ge=1,
    )

    mrph_id: int = Field(
        description="形態素ID",
        example=1,
        ge=1,
    )

    prev_mrph_id: int = Field(
        description="前の形態素ID",
        example=0,
    )

    span: list[int] = Field(
        description="???",  # TODO: 謎なので解明したい
        example=[0, 0],
    )

    doukei: list = Field(
        description="???",  # TODO: 謎なので解明したい
        example=[],
    )

    midasi: str = Field(
        description="見出し",
        example="待つ",
    )

    yomi: str = Field(
        description="読み",
        example="まつ",
    )

    genkei: str = Field(
        description="原形",
        example="待つ",
    )

    hinsi: str = Field(
        description="品詞",
        example="動詞",
    )

    hinsi_id: int = Field(
        description="品詞ID",
        example=2,
    )

    bunrui: str = Field(
        description="品詞細分類",
        example="*",
    )

    bunrui_id: int = Field(
        description="品詞細分類ID",
        example=0,
    )

    katuyou1: str = Field(
        description="活用型",
        example="子音動詞タ行",
    )

    katuyou1_id: int = Field(
        description="活用型ID",
        example=6,
    )

    katuyou2: str = Field(
        description="活用形",
        example="基本形",
    )

    katuyou2_id: int = Field(
        description="活用形ID",
        example=2,
    )

    imis: str = Field(
        description="意味情報",
        example="代表表記:待つ/まつ",
    )

    fstring: str = Field(
        description="???",  # TODO: 謎なので解明したい
        example="",
    )

    repname: str = Field(
        description="代表表記",
        example="待つ/まつ",
    )

    ranks: list[int] = Field(
        description="???",  # TODO: 謎なので解明したい
        example=[1],
    )


class JumanppResponse(BaseModel):
    status: str = Field(
        description="ステータス",
        default="success",
        example="success",
    )
    results: list[JumanppResult]


class JumanppSystemError(BaseModel):
    status: str = Field(
        description="ステータス",
        default="error",
        example="error",
    )
    error: str = Field(
        description="エラー情報",
        default="システムエラー",
        example="システムエラー",
    )
