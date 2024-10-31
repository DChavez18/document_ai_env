# Document AI Invoice Processor

This project uses Google Cloud's Document AI to automate document processing, specifically extracting information from invoices. It processes a PDF file, extracts key fields (like invoice number, date, and total amount), and saves the extracted text to a JSON file for further analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Output](#output)
- [Future Iterations](#future-iterations)

---

## Project Overview

The **Document AI Invoice Processor** leverages Google Cloud's Document AI API to process and extract structured information from invoices in PDF format. This project is ideal for automating tasks such as tracking invoice details, digitizing paper documents, or generating structured data from scanned files.

---

## Getting Started

### Prerequisites

- **Google Cloud Account**: Set up a Google Cloud project and enable billing.
- **Document AI API**: Ensure the Document AI API is enabled for your project.
- **Python**: Python 3.7+ is required, along with `pip` to manage packages.

---

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/document-ai-invoice-processor.git
   cd document-ai-invoice-processor

## Set Up Virtual Environment

```bash
python3 -m venv document_ai_env
source document_ai_env/bin/activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Google Cloud Authentication

1. **Place your Google Cloud JSON key in the credentials folder.**
2. **Set the environment variable for authentication:**

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials/documentai-key.json"
```
## Update Project Variables

In main.py, update the project_id, location, and processor_id with your specific Google Cloud project details.

## Usage

### To process a sample invoice:

1. **Place the PDF Document**:
   - Place a sample PDF in the `document-ai-project` folder or specify the correct path in `main.py`.

2. **Run the Script**:

   ```bash
   python main.py
  

3. **View Extracted Data**
  - Check the terminal output for extracted text.
  - View the structured output saved in output/extracted_data.json.

## Output

  After running the script, you should see:

  - Extracted Text: Printed in the terminal, showing key information like the invoice number, date, and total amount.

  - Saved JSON: A structured JSON file is saved to output/extracted_data.json, containing the extracted data.

## Future Iterations

1. **Expand Field Extraction**
   - Add specific fields to the extraction, such as vendor name, payment terms, or line items on the invoice.

2. **Batch Processing of Multiple Documents**
   - Adapt the script to process multiple PDF files in a batch, saving outputs for each document in a unique file.

3. **Database Integration**
   - Save the extracted data to a database (e.g., SQLite, PostgreSQL) for easier data retrieval and management.

4. **Web Interface**
   - Build a simple web interface to upload documents and display extracted data in real-time using Flask or Django.

5. **Automated Error Handling**
   - Implement error handling to handle different document types, missing fields, or failed API calls gracefully.
