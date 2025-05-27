from state import State
from langgraph.graph import StateGraph, END
from nodes import GraphNodes


def run_langgraph_pipeline():
    graph = StateGraph(State)
    graph.add_node("filtering", GraphNodes().filtering_node)
    graph.add_node("extraction", GraphNodes().extraction_node)

    graph.set_entry_point("filtering")
    graph.add_edge("filtering", "extraction")
    graph.add_edge("filtering", END)

    app = graph.compile()
    final_state = app.invoke({})
    print("Pipeline completed. filtered ids:", final_state["filtered_ids"])
    
if __name__ == "__main__":
    run_langgraph_pipeline()