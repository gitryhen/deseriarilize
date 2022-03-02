import sys
import csv

def hello(a, b):
    print('Filename is: ', str(a))
    print(f'Columns are split on: {b}')

if __name__ == "__main__":
    fn = sys.argv[1]
    split_string = sys.argv[2]
    hello(fn, split_string)
    with open(fn) as file:
        lines = [line.rstrip() for line in file]
    x = []
    s = []
    for i,l in enumerate(lines):
        if l == '--':
            if x != []: s.append(x)
            x = []
        else:
            x.append(float(l))
    # for i,my_row in enumerate(s):
    #     if i<5:
    #         print(my_row)
    #     else:
    #         break

    # balance row length
    row_lengths = []
    for r in s:
        row_lengths.append(len(r))

    max_length = max(row_lengths)
    # print(max_length)

    for r in s:
        while len(r) < max_length:
            r.append(0)

    #transpose
    t = list(map(list, zip(*s)))

    with open(sys.argv[3], 'w', newline='') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(t) # weird to go back to list is this needed?
