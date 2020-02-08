#! python3

# alignTable.py - It takes a table and print it right aligned.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

lensTable= []
for sublist in tableData:
    for item in sublist:
        lensTable.append(len(item))

maxLen = max(lensTable)
print('max len is ' + str(maxLen))
for sublist in tableData:
    for item in sublist:
        item.rjust(maxLen)
        print(item.rjust(maxLen), end=' ')
    print()
