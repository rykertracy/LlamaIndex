from llama_index.core.vector_stores import VectorStoreQuery
import src.prompts as prompts
import pymupdf4llm
import os
import re

def fetch_all_resume_nodes(vector_store):
    """
    Query all resume nodes from the vector store.
    """
    query = VectorStoreQuery(query_embedding=None, mode="default", similarity_top_k=101)
    result = vector_store.query(query)
    return result.nodes

def aggregate_resume_text(nodes):
    """
    Combine all resume node contents into a single string.
    """
    return "\n\n".join(node.get_content(metadata_mode="all") for node in nodes)

def summarize_resumes(llm, resume_text):
    """
    Use LLM to summarize resume text using the prompt from prompts.py.
    """
    prompt = prompts.resume_prompt(resume_text)
    return llm.complete(prompt)

def denoise_text(text):
    text = re.sub(r"[^\w*\s]", " ", text)
    return text

def remove_whitespace(text):
    text = text.strip()
    return text

def remove_underscores(text):
# This will remove patterns like **___** (any number of underscores between two pairs of asterisks)
    text = re.sub(r"\*\*_{1,}\*\*", "", text)
    return text

def pdf_to_llama_markdown(dir, test_on_one_page: bool = False) -> dict:
    raw_markdowns = {}
    loader = pymupdf4llm.LlamaMarkdownReader()
    if test_on_one_page:
        file = os.listdir(dir)[0]
        file_path = os.path.join(dir, file)
        print(file_path)
        doc = loader.load_data(file_path=file_path)

        # Combine all page texts into one string
        combined_text = ''.join([page.text for page in doc])
        return combined_text
    
    else:
        print("Transforming PDF to Markdown...")
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            doc = loader.load_data(file_path=file_path)
            key = file.strip('.pdf')

            # Combine all page texts into one string
            combined_text = ''.join([page.text for page in doc])
            raw_markdowns[key] = {
                'text': combined_text,
                'metadata': [page.metadata for page in doc]
            }
        return raw_markdowns