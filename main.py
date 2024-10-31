from google.cloud import documentai_v1 as documentai
import os
import json

client = documentai.DocumentProcessorServiceClient()

project_id = "documentai-440316"
location = "us"
processor_id = "b1c7249c8dd94882"
name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

def process_document(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    request = documentai.ProcessRequest(
        name=name,
        raw_document=documentai.RawDocument(content=content, mime_type="application/pdf")
    )

    result = client.process_document(request=request)
    document = result.document
    print("Document processing complete.")
    print("Extracted Text:", document.text)

    extracted_data = {"text": document.text}
    output_path = os.path.join("output", "extracted_data.json")
    os.makedirs("output", exist_ok=True)
    with open(output_path, "w") as output_file:
        json.dump(extracted_data, output_file, indent=2)

    print(f"Extracted data saved to {output_path}")

if __name__ == "__main__":
    sample_file_path = "document-ai-project/sample_invoice.pdf"
    process_document(sample_file_path)
