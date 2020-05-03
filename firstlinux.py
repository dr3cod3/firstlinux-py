#!/usr/bin/python3
def main(msg):
    print(msg)

main("Hello ubuntu 20.1")



def add(num1, num2):
    for num in range(num1):
        if num % 2 == 0:
            num+=num2
            print(num)

add(22, 5)