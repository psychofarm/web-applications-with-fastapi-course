def try_int(text) -> int:
    try:
        return int(text)
    except (NameError, ValueError):
        return 0
