def filter_by_state(roster: list[dict], status: str = "EXECUTED") -> list[dict]:
    """функция, которая фильтрует список по заданному значению и возвращает
    список словарей, имеющих заданное значение
    :rtype: list[dict]"""

    approved = []
    for element in roster:
        if status == element.get("state"):
            approved.append(element)
    return approved


def sort_by_date(roster: list[dict], decreasing: bool = True) -> list[dict]:
    """функция, сортирующая заданный список словарей по дате, в порядке убывания"""
    if decreasing:
        sorted_date: list[dict] = sorted(roster, key=lambda rost: rost.get("date"), reverse=True)
        return sorted_date
    else:
        sorted_date: list[dict] = sorted(roster, key=lambda rost: rost.get("date"))
        return sorted_date
