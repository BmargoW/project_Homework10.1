from typing import Any, Dict, List


def filter_by_state(roster: list[dict], status: str = "EXECUTED") -> list[dict]:
    """функция, которая фильтрует список по заданному значению и возвращает
    список словарей, имеющих заданное значение
    :rtype: list[dict]"""

    approved = []
    for element in roster:
        if status == element.get("state"):
            approved.append(element)
    return approved


def sort_by_date(roster: List[Dict[str, Any]], decreasing: bool = True) -> List[Dict[str, Any]]:
    """функция, сортирующая заданный список словарей по дате, в порядке убывания
    :rtype: list[Dict[str, Any]]
    """
    if decreasing:
        sorted_date: List[Dict[str, Any]] = sorted(roster, key=lambda rost: rost.get("date"), reverse=True)
        return sorted_date
    else:
        sorted_date: List[Dict[str, Any]] = sorted(roster, key=lambda rost: rost.get("date"))
        return sorted_date
