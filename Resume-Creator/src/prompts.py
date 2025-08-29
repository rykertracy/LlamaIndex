from llama_index.core.prompts import RichPromptTemplate
import datetime
import dotenv

def get_current_date():
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.datetime.now().strftime("%Y-%m-%d")

TIME_CONTEXT = f"Today's date, in Year-Month-Day format, is {get_current_date()}."

def resume_prompt(resume_text):
    # Personal information in general background. Speak to your experience over the past 5-10 years.
    GENERAL_BACKGROUND = dotenv.get_key(dotenv_path=dotenv.find_dotenv(raise_error_if_not_found=True, usecwd=True), key_to_get="GENERAL_BACKGROUND")
    _check_env(GENERAL_BACKGROUND)

    RESUME_SUMMARY_ROLE = "You are an expert resume reviewer. Your task is to review the provided resume text and provide a summary of the candidate's qualifications, skills, and experiences. \
        Focus on highlighting key achievements, relevant skills, and any unique aspects that make the candidate stand out. \
        Creatively emphasize points that would be particularly appealing to a potential employer."

    CONTENT_RETRIEVER_ROLE = "You are an expert resume content retriever. Your task is to extract and compile information from the database of resume content that is most relevant to the provided job description."

    summarize_instructions_str = """We have provided context information below.
    ---------------------
    {{ background_ctx }}
    ---------------------
    Given the context, your role is provided below.
    ---------------------
    {{ role_ctx }}
    ---------------------
    Given this information, please perform the following action: {{ request }}
    """

    template = RichPromptTemplate(summarize_instructions_str)

    prompt = template.format(background_ctx=GENERAL_BACKGROUND, role_ctx=RESUME_SUMMARY_ROLE, request=f"Summarize the following resume documents into a single, concise CV: {resume_text}")
    return prompt

def _check_env(key):
    if "A 5-10 sentence summary of your background over the past 5-10 years" in key:
        raise KeyError("GENERAL_BACKGROUND in .env not personalized.")