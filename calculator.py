def Add(numbers: str) -> int:
    if not numbers:
        return 0
    normal = numbers.replace('\n', ',')
    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Invalid input with separators")
    try:
        nums_str_to_int = [int(x) for x in normal.split(',')]
        return sum(nums_str_to_int)
    except ValueError:
        raise ValueError("Invalid input")

