handle = open("example.txt", "r")
# handle = open("none.txt", "r")

# count = 0
# for line in handle:
#     count += 1
# print("Line count = ", count)

# handle_read = handle.read()
# print(f"Ukuran: {len(handle_read)} bytes")

count = 0
for line in handle:
    if line.startswith("Hello"):
        count += 1
        print(line)
print(count)

# print(handle)
# handle.write("Hello, this text is written with python")

handle.close()