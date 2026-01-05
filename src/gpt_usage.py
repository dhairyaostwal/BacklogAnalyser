from openai import OpenAI
from src.prompts.prompt import CLASSIFY_PROMPT, PRIORITIZE_PROMPT
from src.secrets.secrets import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
OPENAI_MODEL = "gpt-4o"


def classify_tickets(backlog_tickets):
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=CLASSIFY_PROMPT.format(backlog_tickets),
    )
    return response.output_text


def prioritize_tickets(classified_tickets, priority_request):
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=PRIORITIZE_PROMPT.format(classified_tickets, priority_request),
    )
    return response.output_text
