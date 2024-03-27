#!/usr/bin/python3
"""0-stats.py"""
import sys
import re

regex = r"""
^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s
(\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}\])\s
("GET\s\/projects\/260\sHTTP\/1\.1")\s
(200|301|400|401|403|404|405|500)\s(\d+)$"""

dataToPrint = {
    "totalSize": 0,
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def printResults():
    """_summary_"""

    statusDict = dataToPrint.copy()
    statusDict.pop("totalSize")

    print(f"File size: {dataToPrint['totalSize']}")
    for status, val in statusDict.items():
        if val == 0:
            continue
        print(f"{status}: {val}")


try:
    for i, line in enumerate(sys.stdin):
        line = line.strip()
        match = re.match(regex, line)
        if match is None:
            continue
        status = match.groups()[3]
        size = int(match.groups()[4])
        dataToPrint["totalSize"] += size
        dataToPrint[status] += 1

        if (i+1) % 10 == 0:
            printResults()

finally:
    printResults()
