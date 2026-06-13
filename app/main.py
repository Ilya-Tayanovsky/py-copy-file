def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        return

    try:
        with open(src, "r") as file, open(dst, "w") as new_file:
            new_file.write(file.read())

    except FileNotFoundError:
        return
