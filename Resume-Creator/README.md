
# Resume Creator

This project uses a Retrieval-Augmented Generation (RAG) pipeline to create tailored resumes from a master list, leveraging LLMs and vector search. It ingests multiple resume documents, stores them in a PostgreSQL vector database, and generates concise CVs or answers relevant to job descriptions using contextual retrieval.

## Workflow Overview
1. **Ingest resumes**: PDF resumes are loaded and stored as vector nodes in a PostgreSQL database using LlamaIndex.
2. **Summarize or query**: The job description or query is summarized and converted into a prompt for the LLM.
3. **Contextual retrieval**: Relevant resume content is retrieved from the vector store and summarized into a concise CV or answers using the LLM.

## Folder Structure
- `data/` — Contains all resume PDFs and related documents.
- `src/` — Source code for prompts, utilities, and database management.
	- `prompts.py` — Generates rich prompts for the LLM.
	- `utils.py` — Utility functions for fetching, aggregating, and summarizing resume nodes.
	- `postgresDB/pgstore.py` — Manages PostgreSQL database and vector store integration.
- `summarize_all_resumes.ipynb` — Jupyter notebook for summarizing all resumes in the database.
- `Store_data.ipynb` — Notebook for ingesting and storing resume data.

## Usage
1. **Set up PostgreSQL**: Ensure a running PostgreSQL instance and update connection strings in the code.
2. **Install dependencies**: Install required Python packages (see project requirements).
3. **Ingest resumes**: Use `Store_data.ipynb` to load and store resume PDFs into the vector database.
4. **Summarize resumes**: Run `summarize_all_resumes.ipynb` to retrieve and summarize all resume content using the LLM.

## Example Notebooks
- `Store_data.ipynb`: Ingests resume PDFs into the vector store.
- `summarize_all_resumes.ipynb`: Retrieves all resume nodes and generates a summary CV using the LLM and prompt logic.

## Technologies Used
- Python, Jupyter Notebook
- LlamaIndex
- PostgreSQL
- HuggingFace Embeddings
- OpenAI LLM

## References
- [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/)