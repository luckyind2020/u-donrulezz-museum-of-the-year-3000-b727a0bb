import pathlib


def load_line():
    path = pathlib.Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8").strip()


def validate_line(line):
    if not line:
        raise ValueError("entry.txt must not be empty")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters, got %d" % len(line))
    return line


def format_output(line):
    return validate_line(line)


def main():
    print(format_output(load_line()))


if __name__ == "__main__":
    main()
