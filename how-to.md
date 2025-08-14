# How to Use LlamaIndex with PostgreSQL on Windows 11
## Context
I want to use PostgreSQL as a vector store for my R.A.G. Pipeline. I'm positive there are better options for storing vectors for my use-case. So why do I want to use PostgreSQL? A) In general I want to build Postgre skills. B) I want to store my RAG data locally.

I like to use Powershell's `winget` command to manage my packages if I can because it makes me feel like an epic hacker. Every time I use `winget` here, you can just as easily browser-search the packages/software and download/install. But if you like making things unnecessarily complicated as well, `winget` works all the same. 

I also use Visual Studio Code. If you don't already have it installed, read ahead for some helpful tips during VS Code installation that might alleviate some work. 

**Note**: this how-to assumes you know the foundations of LlamaIndex, Python, and Git

## Installation
1. Install PostgreSQL (link)
    
    **To-do**
    - Process for installing PostgreSQL properly.

2. Install pgvector.

    **To-do**
    - Explanation of why pgvector is necessary
    - Explain PostgreSQL extensions
    - In Powershell, use `winget search --name Visual Studio BuildTools 2022` to hunt down *x64 Native Command Prompt*.
        - I believe that if you're installing Visual Studio Code for the first time, the installer has a checkbox for this. But I already had VS Code, so I had to do it this way.
    - `psql` command line for creating the extension.

3. Use psycopg2

    `pip command`
4. Install PGVectorStore from LlamaIndex with pip

    `pip commmand`

## Using PGVectorStore
    To-Do: 
    - Check if this statment is true: You have to set up the vector store outside of the LlamaIndex framework, then connect to it within the LlamaIndex pipeline.
1. Check and enable `pgvector`

    Create a database and enable extensions. Open Powershell as administrator and run:

    `psql`

    then,
    ```
    CREATE DATABASE vector_db;
    \c vector_db
    CREATE EXTENSION IF NOT EXISTS vector;
    ```
    if this fails, the pgvector extension is not installed properly.
2. 