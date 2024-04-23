with open("Text1.txt", "r") as file:
    with open("Text2.txt", "r") as file2:
        count = 1
        handle = file.readlines()
        handle2 = file2.readlines()
        for i in range(len(handle)):
            for j in range(len(handle2)):
                if i == j:
                    if handle[i] == handle2[j]:
                        print(f"Line {count} are the SAME\n")
                    else:
                        print(f"Line {count} are NOT SAME")
                        print(f"File1 is {handle[i].strip()}")
                        print(f"File2 is {handle2[j].strip()}\n")
            count +=1