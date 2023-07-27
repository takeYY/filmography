# 外部ライブラリ
from pydantic import BaseModel, Field


class DefaultResponse(BaseModel):
    status: str = Field(
        description="ステータス",
        default="success",
        example="success",
    )
    message: str = Field(
        description="メッセージ",
        default="Hello, world!",
        example="Hello, world!",
    )
