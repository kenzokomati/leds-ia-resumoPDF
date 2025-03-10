from crewai.tools import BaseTool
import PyPDF2 
import os

class PdfTextExtractionTool(BaseTool):
    name: str = "PDF Text Extractor"  
    description: str = "A tool to extract raw text from PDF files." 
    
    def _run(self, pdf_path: str) -> str:
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text 
        except Exception as e:
            raise Exception(f"Failed to extract text from PDF: {e}")