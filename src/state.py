from typing import Dict, List, Optional, Union, TypedDict

class State(TypedDict):
    input_dir: str
    output_file: str
    filtered_article_file: str
    filtered_ids: Optional[List[str]]