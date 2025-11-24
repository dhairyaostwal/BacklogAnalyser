# Donna
Your partner in planning

## Personal Story
As my project at work grew, I found tickets in the backlog EPIC increasing some even leading to 1.5 years old. Such large time delay also causes context loss and forces the PM/BA to open individual ticket and note priority. 

Here comes BacklogAnalyser that analyses the tickets and classifies them into similar categories for effective decision making.

> For Presentation slides visit [here](https://app.chroniclehq.com/share/1e19de00-66b3-4210-8406-c32eca0229c0/16141e12-3320-4504-af1a-bbfe11acc8d7/intro)

## Tech Stack
- Python
- scikit-learn
- sentence-transformers

## Main Files
1. app.py: Main application script orchestrating the workflow.
2. preprocess.py: Loads and cleans ticket data.
3. embed.py: Generates text embeddings using SentenceTransformer.
4. cluster.py: Clusters ticket embeddings using KMeans.
5. mock_jira_response.json: Sample JIRA ticket data.

## Data Flow
1. Load Data: load_data() in preprocess.py reads tickets from mock_jira_response.json.

2. Preprocess Tickets: preprocess_items() combines title and description, cleans the text, and adds a clean_text field to each ticket.

3. Generate Embeddings: embed_texts() in embed.py converts each ticket’s clean text into a vector embedding using a pre-trained model.

4. Cluster Tickets: cluster_embeddings() in cluster.py applies KMeans clustering to group similar tickets.

5. Output Results: The script prints each ticket’s clean text with its assigned cluster/category.

## Example Usage
```python
python app.py
```

## How It Works
- The tool reads JIRA tickets from a JSON file(JIRA API integration as part of future enhancement)
- It cleans and preprocesses the text data.
- Each ticket is embedded into a vector space.
- Tickets are clustered into categories using KMeans.
- The output shows which tickets belong to which category.