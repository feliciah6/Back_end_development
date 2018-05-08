names =input("names:")

result=names.split(',')
print(','.join(sorted(list(set(result)))))
