def getLinesFor(day: str, sample: bool = False) -> list[str]:
    input = open(f"inputs/day{day}{'-sample' if sample else ''}.txt", "r")
    return input.readlines()
