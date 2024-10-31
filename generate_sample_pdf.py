import os
from fpdf import FPDF

output_dir = "document-ai-project"
output_file = f"{output_dir}/sample_invoice.pdf"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Sample Invoice", ln=True, align='C')
pdf.cell(200, 10, txt="Invoice Number: 12345", ln=True)
pdf.cell(200, 10, txt="Date: 2024-10-31", ln=True)
pdf.cell(200, 10, txt="Total Amount: $500.00", ln=True)

pdf.output(output_file)
print(f"Sample invoice saved to {output_file}")