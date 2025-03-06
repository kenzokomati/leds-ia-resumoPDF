import os
from crewai.tools import BaseTool
# import pypdf2
import fitz  # PyMuPDF

class PDFExtractorTool(BaseTool):
    name: str = "PDF Text Extractor"
    description: str = "Tool to extract text from multiple PDF files."

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extracts text from a single PDF file using fitz (PyMuPDF)."""
        try:
            doc = fitz.open(pdf_path)  # Open the PDF
            text = ""
            for page_num in range(len(doc)):  # Loop through all pages
                page = doc.load_page(page_num)  # Load the page
                text += page.get_text("text")  # Extract text from the page
            return text.strip() if text else "⚠️ No text extracted from this PDF."
        except Exception as e:
            return f"❌ Error processing {pdf_path}: {str(e)}"

    def _run(self, pdf_path: str) -> str:
        """Extracts text from the given PDF file path."""
        return self.extract_text_from_pdf(pdf_path)
