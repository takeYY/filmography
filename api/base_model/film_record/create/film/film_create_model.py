from pydantic import BaseModel, Field, validator


class FilmCreateModel(BaseModel):
    tmdb_id: int = Field(
        default=None,
        example=281,
        description="TMDbのID",
        gt=0,
    )

    @validator("tmdb_id")
    def validate_tmdb_id(cls, v: int):
        if not v:
            raise ValueError("tmdb_id is required.")

        return v
