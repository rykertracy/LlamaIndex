"""
Everything related to ingesting PDF data into the vector store.
"""
import os
import pymupdf4llm
import re
import utils

class PDFPreprocessor():
    def __init__(self, pdf_directory: str = "../data"):
        self.dir = pdf_directory
        self.raw_markdowns = {}
        self.bolded = []

    def process_pdfs(self):
        """Execute the LlamaMarkdownReader, which translates PDFs to markdown, provided by pymupdf4llm.

        Returns:
            self.markdowns (dict): Dictionary of markdowns that were translated from PDFs. Includes metadata.
        """
        self.raw_markdowns = utils.pdf_to_llama_markdown(self.dir, test_on_one_page=False)
        return self.raw_markdowns
    
    def clean_markdowns(self):
        markdowns=[]
        print("Cleaning Markdown Files...")
        for key in self.raw_markdowns.keys():
            text = self.raw_markdowns[key]['text']
            denoised_text = utils.denoise_text(text)
            removed_whitespace_text = utils.remove_whitespace(denoised_text)
            clean_text = utils.remove_underscores(removed_whitespace_text)
            markdowns[key] = {
                'metadata': self.raw_markdowns[key]['metadata'],
                'text': clean_text
            }
        return markdowns


class PDFIngestor():
    def __init__(self, pdf_directory: str = "../data"):
        self.dir = pdf_directory
        self.loader = PyMuPDFReader()
        self.documents = []

    def load_pdf_data(self):
        for filename in os.listdir(self.dir):
            file_path = os.path.join(self.dir, filename)
            docs = self.loader.load(file_path=file_path)
            self.documents.extend(docs)

if __name__ == "__main__":
    t = PDFPreprocessor()
    q = t.llama_pdf_to_markdown(test_on_one_page=False)
    q = t.clean_markdowns()
    md_text = q
    for key in md_text.keys():
        text = md_text[key]['text']
        print(text)