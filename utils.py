def getLinesFor(day: str, sample: bool = False) -> list[str]:
    input = open(f"day{day}-input{'-sample' if sample else ''}.txt", "r")
    return input.readlines()
