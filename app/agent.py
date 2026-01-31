def solve_task(task: dict) -> dict:
    """
    Deterministic baseline logic.
    No learning, no memory, no external tools.
    """

    task_type = task.get("type", "unknown")

    if task_type == "classification":
        return {
            "answer": task.get("labels", ["default"])[0],
            "confidence": 0.5,
            "explanation": "Baseline rule: choose first label"
        }

    if task_type == "ranking":
        items = task.get("items", [])
        return {
            "ranking": sorted(items),
            "explanation": "Baseline rule: lexicographic sort"
        }

    if task_type == "planning":
        steps = task.get("steps", [])
        return {
            "plan": steps,
            "explanation": "Baseline rule: return provided order"
        }

    return {
        "answer": "unsupported_task",
        "explanation": "Baseline fallback behavior"
    }
