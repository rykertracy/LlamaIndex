"""
Testing the ingest functions
"""
import unittest
from ingest import PDFPreprocessor, PDFIngestor
import os

class TestPDFPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = PDFPreprocessor(pdf_directory="../data")

    def test_pdf_to_markdown(self):
        result = self.preprocessor.pdf_to_markdown()
        self.assertIsNotNone(result)  # Example assertion

class TestPDFIngestor(unittest.TestCase):
    def setUp(self):
        self.ingestor = PDFIngestor(pdf_directory="../data")

    def test_load_pdf_data(self):
        self.ingestor.load_pdf_data()
        self.assertTrue(len(self.ingestor.documents) > 0)

if __name__ == "__main__":
    unittest.main()