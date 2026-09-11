def draw_pyramid(n):
    odds = []
    for i in range(1, n + 1):
        odds.append(2 * i - 1)

    rows = []
    for i in range(len(odds)):
        current_numbers = odds[: i + 1]
        line = ""
        for num in reversed(current_numbers):
            line = line + str(num) + " "
        line = line.strip()
        rows.append(line)

    max_len = len(rows[-1])

    for line in rows:
        spaces = (max_len - len(line)) // 2
        print(" " * spaces + line)

    for line in reversed(rows[:-1]):
        spaces = (max_len - len(line)) // 2
        print(" " * spaces + line)