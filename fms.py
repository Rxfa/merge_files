#!/usr/bin/python3

import sys

app_name = sys.argv[0]

def main():
    fname_out = input("What will the name of the output file be?")
    try: 
        open(fname_out, 'x')
    except:
        print(f'{fname_out}')

    def merge(file):
        with open(file, 'r+', encoding='utf8', errors='ignore') as file:
            fout = open(fname_out, 'r+', encoding='utf8', errors='ignore')
            for line in file:
                if line not in fout:
                    fout.write(line)
            fout.close()
        return (f"[+]{file} merged successfully!")

    n = 1
    while n <= (len(sys.argv)-1):
        merge(sys.argv[n])
        n += 1


if __name__ == '__main__':
    if (len(sys.argv)-1) <= 1:
        print(f'[-] {app_name} requires at least 2 two files!')
        print(f'[-] Usage: {app_name} <file1> <file2> ...')
    else:
        main()
