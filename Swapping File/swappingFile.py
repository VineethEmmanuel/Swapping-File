def SwapFileData():
    takePath1 = input('Give the First Path: ')
    takePath2 = input('Give the Second Path: ')

    with open(takePath1, 'r') as file1:
        data_a = file1.read()
        
    with open(takePath2, 'r') as file2:
        data_b = file2.read()
        

    # using with statement
    with open(takePath1, 'w') as file1:
        file1.write(data_b)
    # using with statement
    with open(takePath2, 'w') as file2:
        file2.write(data_a)

SwapFileData()