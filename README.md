# chia\_to\_csv.py

chia\_to\_csv.py takes the output of the CLI Chia Wallet and seperates it into different CSV files(Amount sent.csv, Amount received.csv, Amount rewarded.csv, etc.).

------------------------------------------------------------------------

## How to use

chia\_to\_csv.py can either take input from STDIN or a txt file.

Pipe from Chia Wallet:

```bash
chia wallet get_transactions | python3 chia_to_csv.py
```

Read from txt file:

```bash
python3 chia_to_csv.py /path/to/file
```

## Update 2 :smile:

Update 2 fixes some issues with the first version. The first version would ignor rewards and "sent in trade" transactions. Also the entire source code is refactored, so hopefully it is easier to understand.

## Donations

Not required, but much appreciated.

xch17mqudjld8c97jamgpz3vvfnrqtuc4pyuhyvjlk6rnzsd5ejvc30sfdqp0g
