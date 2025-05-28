import os
import json
import time
from chains import Chains

class Extraction:
    def __init__(self, input_dir: str, output_file: str, filtered_article_file: str):
        self.input_dir = input_dir
        self.output_file = output_file
        self.filtered_article_file = filtered_article_file
    
    def process_filtered_articles(self):
        with open(self.filtered_article_file, "r") as f:
            filtered_ids = json.load(f)["filtered_articles"]
        insights = {}
        processed_count = 0 
        for file in os.listdir(self.input_dir):
            if not file.endswith(".md"):
                continue

            article_id = file.replace(".md", "")
            if article_id not in filtered_ids:
                continue

            with open(os.path.join(self.input_dir, file), "r", encoding="utf-8") as f:
                text = f.read()
                try:
                    result = Chains().extraction_chain().invoke({"article": text})
                    insights[article_id] = result.dict()
                    print(f"{processed_count} article processed")
                    processed_count += 1
                    # Pause after every 14 requests to avoid hitting Gemini free-tier rate limits
                    if processed_count % 14 == 0:
                        print("Pausing for 120 seconds...")
                        time.sleep(120)  
                except Exception as e:
                    print(f"Error processing {article_id}: {e}")

        with open(self.output_file, "w") as f:
            json.dump(insights, f, indent=2)

