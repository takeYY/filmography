# 外部ライブラリ
from pydantic import BaseModel, Field


class WordRequest(BaseModel):
    target: str = Field(
        description="形態素解析の対象文字列",
        example="すもももももももものうち",
    )
