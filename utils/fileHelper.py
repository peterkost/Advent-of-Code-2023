def getLinesFor(day: str, sample: bool = False) -> list[str]:
    input = open(f"inputs/day{day}{'-sample' if sample else ''}.txt", "r")
    return [line.strip() for line in input.readlines()]

def writeListToFile(input: list, name: str):
    file = open(f"tmp/{name}.txt", "w")
    for e in input:
        file.write("".join(e) + "\n")
    file.close()

