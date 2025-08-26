

# Resume Creator

This project uses a Retrieval-Augmented Generation (RAG) pipeline to generate tailored resumes from a master list, leveraging LlamaIndex, PostgreSQL, and LLMs.

## Workflow
1. **Ingest resumes**: Load PDF resumes and store them as vector nodes in PostgreSQL.
2. **Summarize or query**: Use job descriptions or queries to generate prompts for the LLM.
3. **Contextual retrieval**: Retrieve relevant resume content and summarize into a concise CV or answers.

## Folder Structure
- `data/`: Resume PDFs and related documents.
- `src/`: Source code for prompts, utilities, and database management.
	- `prompts.py`: Generates prompts for LLM summarization.
	- `utils.py`: Fetches, aggregates, and summarizes resume nodes.
	- `postgresDB/pgstore.py`: Manages PostgreSQL vector store.
	- `summarize.py`: Script for summarizing resumes.
- `Store_data.ipynb`: Ingests resume PDFs into the vector store.
- `summarize_all_resumes.ipynb`: Summarizes all resumes in the database.

## Usage
1. Set up PostgreSQL and update connection strings.
2. Install dependencies (`pip install -r requirements.txt`).
3. Ingest resumes with `Store_data.ipynb`.
4. Summarize resumes with `summarize_all_resumes.ipynb` or run `python src/summarize.py`.

## Technologies
- Python, Jupyter Notebook
- LlamaIndex
- PostgreSQL
- HuggingFace Embeddings
- OpenAI LLM

## References
- [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/)