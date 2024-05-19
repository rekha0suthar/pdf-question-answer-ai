import os
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from langchain.schema import Document

# Get the Hugging Face token from the environment
hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")
if not hf_token:
    raise ValueError("Hugging Face Hub token is not set")

# Load the model and tokenizer without the deprecated parameter
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad", token=hf_token)
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad", token=hf_token)

# Initialize the Hugging Face QA pipeline with the loaded model and tokenizer
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def get_answer_from_pdf(pdf_doc, question):
    # Construct the file path from the filename
    file_path = os.path.join("/app/uploads", pdf_doc.filename)
    pdf_text = extract_text_from_pdf(file_path)

    # Prepare the input for the QA pipeline
    input_data = {
        "context": pdf_text,
        "question": question
    }

    # Run the QA pipeline with the text and the question
    answer = qa_pipeline(input_data)
    return answer['answer']

