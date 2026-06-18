line_count = 0
word_count = 0

with open("poem.txt", "r") as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")

with open("summary.txt", "w") as summary_file:
    summary_file.write(f"The poem has {line_count} lines and {word_count} words.\n")
