from functools import reduce
import csv
import sys

def parse(file):
    return list(filter(lambda s: s != '', [line.strip() for line in file.readlines()]))

def read_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return parse(f)

def chunks(lines):
    chunk = []
    while len(lines) > 0:
        chunk.append(lines[:5])
        lines = lines[5:]

    return chunk

def find_unique(chunk):
    return {' '.join(i[2].split()[:-2]) for i in chunk}

def to_words(transaction_chunks):
    return [j.split(': ') if len(j.split()) > 2 else j.split() for i in transaction_chunks for j in i]

def to_dict(d):
    xs = []

    while len(d) > 0:
        xs.append(reduce(lambda x, y: {**x, **y}, d[:5]))
        d = d[5:]

    return xs

def write_csv(data):
    file_names = data.keys()

    for i in file_names:
        header = data[i][0].keys()
        with open(i+'.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data[i])

def main():
    if len(sys.argv) > 1:
        transaction_chunks = chunks(read_file(sys.argv[1]))
    else:
        transaction_chunks = chunks(parse(sys.stdin))

    output_files = {j:[] for j in [i[:-1] for i in find_unique(transaction_chunks)]}

    xs = to_dict([{i[0]:i[1]} for i in to_words(transaction_chunks)]) # converts words to dict. Ex: ['Transaction', '0xc0ffee'] -> {'Transaction': '0xc0ffee'}


    for i in output_files.keys():
        for j in xs:
            if i in j.keys():
                output_files[i].append(j)
    
    write_csv(output_files)

if __name__ == '__main__':
    main()
