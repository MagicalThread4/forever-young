for i in range(0,26):
    if i % 2 == 0:
        if i in range(0,14):
            print(str(i) + " AM")
        if i in range(12,26):
            print(str(i) + " PM")