from pydantic import BaseModel, field_validator, Field


class BasePerson(BaseModel):
    name: str
    # name: str = Field(... ,min_length=1, max_length=100)

    @field_validator("name")
    def name_validator(cls, value: str):
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("name must be less than 100 characters")
        elif not value.isalpha():
            raise ValueError("name must only contain letters")
        return value

class ResponsePersonSchema(BasePerson):
    id:int

class CreatePersonSchema(BasePerson):
    pass

class UpdatePersonSchema(BasePerson):
    pass