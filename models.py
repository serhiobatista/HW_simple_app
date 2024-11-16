from pydantic import BaseModel


class Profile(BaseModel):
    FIO: str
    email: str

    model_config = {
        "json_schema_extra": {
            "example": [
                {
                    "FIO": "Kolesov Sergey Vladimirovich",
                    "email": "black60cat@mail.ru"
                }
            ]
        }
    }
