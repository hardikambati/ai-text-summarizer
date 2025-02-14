from fastapi import Request


def get_summarizer_model(request: Request):
    return request.app.state.summarizer_model

def get_tokenizer(request: Request):
    return request.app.state.tokenizer
