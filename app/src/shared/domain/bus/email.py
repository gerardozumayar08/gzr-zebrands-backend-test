from pydantic import BaseModel, ConfigDict


class EmailSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sender: str
    destination: str
    subject: str
    message: str
