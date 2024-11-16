from pydantic import BaseModel


class Profile(BaseModel):
    FIO: str
    emai: str

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
