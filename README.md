# ENS-Checker
Script that takes in a list of words and checks whether they are available to be claimed on ethereum name service or not

## Installation

clone repo then

```bash
pip install -r requirements.txt
```

## How to use:

add a wordlist to list.txt (each username to be checked on a seperate line, the script automatically adds .eth to them)

put your infura api link in the file

run main.py 

available usernames will be stored in available.txt you can also make it print which usernames are available by uncommenting it in main.py
