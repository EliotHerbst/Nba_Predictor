def reverse_file(read, write):
    File_Object = open(read, "r")
    File_To_Write = open(write, "a")
    lines = File_Object.readlines()
    File_To_Write.writelines(lines[::-1])


reverse_file("AdvancedDataByDate.txt", "AdvancedDataByDataReversed.txt")

