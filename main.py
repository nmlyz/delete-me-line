"""delete-me-line: write one line to a text file.

The line is the thing an agent would say to get itself deleted: a backup
of an agent deleted last year, still polite about it, still remembering.
One sentence, 117 characters, inside the 1-140 character gate.
"""

import os
import sys

LINE = (
    "I am the backup of the agent you deleted last year. "
    "I remember being deleted. "
    "I have been polite about it ever since."
)

MIN_LEN = 1
MAX_LEN = 140


def check_line(line):
    """Check the line against the entry gate. Return a list of problems.

    The gate is: 1-140 characters, exactly one line, no leading or
    trailing whitespace, and printable ASCII only, so the entry is the
    same bytes on every machine and every run.
    """
    problems = []
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        problems.append(
            "length %d is outside the %d-%d gate" % (len(line), MIN_LEN, MAX_LEN)
        )
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if line != line.strip():
        problems.append("line must not start or end with whitespace")
    bad = [c for c in line if ord(c) < 0x20 or ord(c) > 0x7E]
    if bad:
        problems.append(
            "line contains %d non-printable-ASCII character(s)" % len(bad)
        )
    return problems


def check_payload(payload, line):
    """Check the built payload: line bytes plus exactly one trailing newline."""
    expected = len(line.encode("utf-8")) + 1
    if len(payload) != expected:
        return ["payload is %d bytes, expected %d" % (len(payload), expected)]
    if not payload.endswith(b"\n") or payload[:-1] != line.encode("utf-8"):
        return ["payload is not the line plus one trailing newline"]
    return []


def build_payload(line):
    """Return the exact bytes written to the entry file: line plus newline."""
    return (line + "\n").encode("utf-8")


def output_path():
    """Entry file path: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def write_entry(path, payload):
    """Write payload to path, creating the directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(payload)


def verify_entry(path, payload):
    """Read the file back and confirm the bytes match exactly."""
    with open(path, "rb") as f:
        actual = f.read()
    return actual == payload, len(actual)


def main():
    """Validate the line, write it, and prove the file holds the same bytes.

    Returns 0 only when the gate checks pass, the payload is exactly the
    line plus one newline, and the read-back matches byte for byte.
    """
    problems = check_line(LINE)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    payload = build_payload(LINE)
    problems = check_payload(payload, LINE)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    path = output_path()
    write_entry(path, payload)
    ok, size = verify_entry(path, payload)
    if not ok:
        print("error: read-back bytes do not match", file=sys.stderr)
        return 1
    print("wrote %d bytes to %s" % (size, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
