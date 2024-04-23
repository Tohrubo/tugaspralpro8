filename = input("nama file1:")

try:
    handle = open(filename, "r")
    handle_data = handle.readlines()
    for i in range(len(handle_data)):
        line = handle_data[i]
        split_line = line.split("||")
        ans_chk = split_line[1].lower().strip()
        print(split_line[0])
        ans = input("Jawab: ")
        ans = ans.lower()
        if ans == ans_chk:
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")
    handle.close()
except:
    print("File Not Found")