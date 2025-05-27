from state import State
from langgraph.graph import StateGraph, END
from nodes import GraphNodes
import os
from IPython.display import Image


def run_langgraph_pipeline():
    graph = StateGraph(State)
    graph.add_node("filtering", GraphNodes().filtering_node)
    graph.add_node("extraction", GraphNodes().extraction_node)

    graph.set_entry_point("filtering")
    graph.add_edge("filtering", "extraction")
    graph.add_edge("filtering", END)

    app = graph.compile()
    image_bytes = app.get_graph().draw_mermaid_png()
    file_name = "langgraph_pipeline.png"
    if not os.path.exists(file_name):
        with open(file_name, "wb") as f:
            f.write(image_bytes)
        print(f"Saved image as {file_name}")
    else:
        print(f"{file_name} already exists. Skipping save.")

    final_state = app.invoke({})
    print("Pipeline completed. filtered ids:", final_state["filtered_ids"])
    
if __name__ == "__main__":
    run_langgraph_pipeline()