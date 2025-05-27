from state import State
from filtering import Filtering
from extraction import Extraction
import json

class GraphNodes:
    
    @classmethod
    def filtering_node(cls, state: State) -> State:
        input_dir='research_articles/papers'
        output_file='outputs/filtered_articles.json'
        filtering_obj: Filtering= Filtering(input_dir=input_dir, output_file=output_file)
        filtering_obj.filter_articles()
        with open(output_file) as f:
            state["filtered_ids"] = json.load(f)["filtered_articles"]
        return state
    
    @classmethod
    def extraction_node(cls, state: State) -> State:
        input_dir='research_articles/papers'
        output_file='outputs/extracted_insights.json'
        filtered_article_file='outputs/filtered_articles.json'
        extraction_obj: Extraction= Extraction(input_dir=input_dir, output_file=output_file, filtered_article_file=filtered_article_file)
        extraction_obj.process_filtered_articles()
        # with open(output_file) as f:
        #     state["extracted_insights"] = json.load(f)
        return state