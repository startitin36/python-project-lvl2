from gendiff import generate_diff


file1 = input("input first file name:")
file2 = input("input second file name:")
diff = generate_diff(file1, file2)
print(diff)
