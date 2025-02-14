class TextSummarizationService:
    """
    Text summarization specific services.
    """

    def __init__(self, summarizer_model, tokenizer):
        self.summarizer_model_instance = summarizer_model
        self.tokenizer_instance = tokenizer

    def summarize_text(self, input_text: str) -> str:
        inputs = self.tokenizer_instance(
            "summarize: " + input_text,
            return_tensors="pt",
            max_length=512,
            truncation=True,
        )
        outputs = self.summarizer_model_instance.generate(
            inputs["input_ids"],
            max_length=100,
            min_length=40,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )

        summary = self.tokenizer_instance.decode(outputs[0], skip_special_tokens=True)
        return summary
