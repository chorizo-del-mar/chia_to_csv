# Jose Munoz
# chia_to_csv.py
# 2023-02-02


import itertools
import csv
import sys

def get_file():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            return f.read()

    else:
        return sys.stdin.read()

def flatten(xs):
    return itertools.chain.from_iterable(xs)

def into_blocks(raw_string):
    return raw_string.split('\n\n')

def into_dict(xs):
    return {xs[i]: xs[i+1] for i in range(0, len(xs), 2)}

def trim_newline(string):
    return string.split('\n')

def half_string(string):
    if ': ' in string:
        return string.split(': ')
    else:
        return string.split()

def get_keys_and_index(transactions_dict):
    return [(transactions_dict[i].keys(), i) for i in range(len(transactions_dict))]

def get_received(keys_and_index):
    return filter(lambda s: 'Amount received' in s[0], keys_and_index)

def get_sent(keys_and_index):
    return filter(lambda s: 'Amount sent' in s[0], keys_and_index)

def seperate_received_sent(transactions_dict):
    return (get_received(get_keys_and_index(transactions_dict)), get_sent(get_keys_and_index(transactions_dict)))

def recombine(rs_tuple, transactions_list):
    return ([transactions_list[i[1]] for i in rs_tuple[0]], [transactions_list[i[1]] for i in rs_tuple[1]])

def to_csv(filename, header, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        [writer.writerow(i) for i in data]

def main():
    processed = [into_dict(list(flatten(map(half_string, i)))) for i in map(trim_newline, into_blocks(get_file()))]
    rs_tuple = recombine(seperate_received_sent(processed), processed)
    to_csv('received.csv', rs_tuple[0][0].keys(), rs_tuple[0])
    to_csv('sent.csv', rs_tuple[1][0].keys(), rs_tuple[1])

if __name__ == '__main__':
    main()
