# standard imports
from fastapi import (
    Depends,
    status,
    APIRouter,
)
from fastapi.responses import JSONResponse

# internal imports
from utils.dependencies import (
    get_tokenizer,
    get_summarizer_model,
)
from api.schemas import TextSummarizationSchema
from api.service import TextSummarizationService


router = APIRouter()


@router.get("/health", tags=["System health"])
def get_health():
    """
    Health status
    """
    return JSONResponse(
        content={"data": "Server is up and running"}, status_code=status.HTTP_200_OK
    )


@router.post("/summarize", tags=["Summarizer"], response_model=None)
async def post_summarize(
    payload: TextSummarizationSchema,
    summarizer_model=Depends(get_summarizer_model),
    tokenizer=Depends(get_tokenizer),
):
    """
    Summarize a text based on input
    """
    text = payload.text
    summary = TextSummarizationService(
        summarizer_model=summarizer_model, tokenizer=tokenizer
    ).summarize_text(input_text=text)
    return JSONResponse(content={"data": summary}, status_code=status.HTTP_200_OK)
