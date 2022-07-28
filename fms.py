#!/usr/bin/env python3

import sys

from colorama import Fore, Style


def main():
    try:
        fname_out = input("What will the name of the output file be? ") 
        open(fname_out, 'x')
    except FileExistsError:
        print(f"[-] {Fore.RED}{fname_out} could not be created.{Style.RESET_ALL}")
        main()
    except KeyboardInterrupt:
        sys.exit()

    def merge(file):
        with open(file, "r+", encoding="utf8", errors="ignore") as file:
            fout = open(fname_out, "r+", encoding="utf8", errors="ignore")
            for line in file:
                if line not in fout:
                    fout.write(line)
            fout.close()
        return (f"[+] {Fore.GREEN}{file} merged successfully!{Style.RESET_ALL}")

    def iterate():
        n = list(x for x in range(1, len(sys.argv)))
        iteration = map(lambda x: merge(sys.argv[x]), n)
        return iteration

    iterate()


if __name__ == "__main__":
    if len(sys.argv) in range(3):
        print(f"[-] {sys.argv[0]} requires at least 2 two files!")
        print(f"[-] Usage: {sys.argv[0]} <file1> <file2> ...")
    else:
        main()