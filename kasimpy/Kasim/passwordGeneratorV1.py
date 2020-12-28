#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-()%'
length = input('Password length:')
length = int(length)
noPwd = input('Number of passwords:')
noPwd = int(noPwd)

for p in range(noPwd):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)


