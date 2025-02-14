from pydantic import BaseModel


class TextSummarizationSchema(BaseModel):
    text: str
