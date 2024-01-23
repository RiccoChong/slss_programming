with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    for line in f:
        line_list = line.split(",")