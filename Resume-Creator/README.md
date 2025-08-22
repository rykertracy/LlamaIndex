# Resume Creator
Being at a position where I have skills that span multiple industries, I would like to allow an LLM to create a resume from a master list that adhere's to the text of the job description. Therefore, here I will create a RAG pipeline that ingests my resumes over the past three years and uses contextual retrieval to grab only data relevant to the job description.

## Steps
1. Store all resumes into a Milvus vector database.
2. Summarize the job description. Draft a prompt that will reduce that summary down to a list of questions and key words.
3. Compile a list of answers that address the keywords and questions from the job description. With a hybrid search (https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo)