from src.gpt_usage import classify_tickets, prioritize_tickets
from src.preprocess import load_data, preprocess_items

backlog_tickets = load_data("data/mock_jira_response.json")
backlog_tickets = preprocess_items(backlog_tickets)

classified_tickets = classify_tickets(backlog_tickets)
print(f"Classified Tickets = {classified_tickets}")

priority_request = "I'd want to resolve all performance and reliability issues before the next release."

prioritized_tickets = prioritize_tickets(classified_tickets, priority_request)
print(f"Priority Order = {prioritized_tickets}")