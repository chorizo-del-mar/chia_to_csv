# chia\_t\_csv

chia\_to\_csv converts wallet transactions to a received.csv and sent.csv
file.

------------------------------------------------------------------------

## How to use

chia\_to\_csv.py can either take input from STDIN or a txt file.

Pipe from chia wallet:

```bash
chia wallet get_transactions | chia_to_csv.py
```

Read from txt file:

```bash
chia_to_csv.py /path/to/file
```

All of the "received transactions" go into the received.csv file and all
of the "sent transactions" go into the sent.csv file.
