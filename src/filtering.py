import os
import json
import re
from sentence_transformers import SentenceTransformer, util

class Filtering:
    def __init__(self, input_dir, output_file):
        self.input_dir = input_dir
        self.output_file = output_file
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.cancer_embedding = self.model.encode("cancer research", convert_to_tensor=True)
        self.immunology_embedding = self.model.encode("immunology research", convert_to_tensor=True)
        self.cancer_terms = ["cancer", "tumor", "neoplasm", "oncogene"]
        self.immuno_terms = ["immuno", "antibody", "t-cell", "cytokine"]

    def is_relevant(self, text: str) -> bool:
        all_terms = self.cancer_terms + self.immuno_terms
        text_lower = text.lower()
        keyword_match = any(term in text_lower for term in all_terms)
        embedding = self.model.encode(text, convert_to_tensor=True)
        sim_cancer = util.cos_sim(embedding, self.cancer_embedding).item()
        sim_immuno = util.cos_sim(embedding, self.immunology_embedding).item()
        return keyword_match or sim_cancer > 0.5 or sim_immuno > 0.5

    def filter_articles(self):
        filtered_ids = []
        for filename in os.listdir(self.input_dir):
            if not filename.endswith(".md"):
                continue
            path = os.path.join(self.input_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                if self.is_relevant(content):
                    pubmed_id = re.findall(r"\*\*PMID:\*\*\s*(\d+)", content)
                    if pubmed_id:
                        filtered_ids.append(pubmed_id[0])

        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, "w") as f:
            json.dump({"filtered_articles": filtered_ids}, f, indent=2)

