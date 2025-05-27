from typing import TypedDict


class State(TypedDict):
    filtered_ids: list[str]
    insights: dict