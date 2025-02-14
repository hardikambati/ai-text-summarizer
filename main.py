# standard imports
from fastapi import (
    FastAPI,
)
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

# 3rd party imports
from transformers import T5ForConditionalGeneration, T5Tokenizer

# internal imports
from api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs on startup
    """
    print("[model] Loading summarizer model...")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    app.state.summarizer_model = model
    app.state.tokenizer = tokenizer
    print("[model] Model locaded successfully")

    yield
    print("Shutting down")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# routes
app.include_router(router)
