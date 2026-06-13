import os


def copy_file(command: str) -> None:
    file_name = command.split()

    if not file_name:
        return

    elif len(file_name) != 3:
        return

    elif not (os.path.exists(file_name[1])):
        return

    elif file_name[1] == file_name[2]:
        return

    elif file_name[0] == "cp":
        with (
            open(file_name[1], "r") as file,
            open(file_name[2], "w") as new_file
        ):
            content = file.read()
            new_file.write(content)
    return
