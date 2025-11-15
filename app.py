from src.preprocess import load_data, preprocess_items
from src.embed import embed_texts
from src.cluster import cluster_embeddings

backlog_tickets = load_data("data/mock_jira_response.json")
backlog_tickets = preprocess_items(backlog_tickets)

ticket_embeddings = []
for ticket in backlog_tickets:
    # Embed each ticket's clean text
    ticket_embeddings.append(embed_texts(ticket['clean_text']))

classified_labels = cluster_embeddings(ticket_embeddings)

for item, label in zip(backlog_tickets, classified_labels):
    print(f"Category {label}: " + item["clean_text"])