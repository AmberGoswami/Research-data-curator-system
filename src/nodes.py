from state import State
from filtering import Filtering
from extraction import Extraction
import json

class GraphNodes:
    
    @classmethod
    def filtering_node(cls, state: State) -> State:
        filtering_obj = Filtering(
            input_dir=state["input_dir"],
            output_file=state["filtered_article_file"]
        )
        filtering_obj.filter_articles()
        with open(state["filtered_article_file"]) as f:
            state["filtered_ids"] = json.load(f)["filtered_articles"]
        return state
    
    @classmethod
    def extraction_node(cls, state: State) -> State:
        extraction_obj = Extraction(
            input_dir=state["input_dir"],
            output_file=state["output_file"],
            filtered_article_file=state["filtered_article_file"]
        )
        extraction_obj.process_filtered_articles()
        return state