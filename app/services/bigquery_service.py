from google.cloud import bigquery
from datetime import datetime

client = bigquery.Client()
TABLE_ID = "your_project.your_dataset.text_analysis"

def save_to_bigquery(file_name: str, analysis_type: str, key: str, value):
    row = {
        "file_name": file_name,
        "analysis_type": analysis_type,
        "key": key,
        "value": str(value),
        "timestamp": datetime.utcnow()
    }

    errors = client.insert_rows_json(TABLE_ID, [row])
    if errors:
        print("BigQuery insert error:", errors)
