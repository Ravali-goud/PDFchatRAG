import os
import fitz  # PyMuPDF
import camelot  # For table extraction

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return None
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None


def extract_tables_from_pdf(pdf_path):
    """Extract tables from a PDF file."""
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return None
    try:
        tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")
        return [table.df for table in tables]
    except Exception as e:
        print(f"Error extracting tables: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    pdf_path = r"C:\Users\grava\Downloads\example.pdf"  # Replace with the correct path

    # Extract text
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    if text:
        print("Extracted Text:\n", text)

    # Extract tables
    print("\nExtracting tables from PDF...")
    tables = extract_tables_from_pdf(pdf_path)
    if tables:
        print("Extracted Tables:")
        for idx, table in enumerate(tables):
            print(f"\nTable {idx + 1}:\n", table)
