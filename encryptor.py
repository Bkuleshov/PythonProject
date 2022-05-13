import sys
import argparse
import random


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', nargs='?', default='c')
    parser.add_argument('--shift', '-s', nargs='?', type=int, default=3)
    parser.add_argument('--input', '-i', nargs=1)
    parser.add_argument('--output', '-o', nargs=1)
    parser.add_argument('--key', '-k', nargs='?', default='cipher')
    return parser


def antipod(string):
    antipods = ''
    for i in range(0, len(string)):
        asciiCode = 91 - ord(string[i])
        antipods += chr(asciiCode + 65)
    return antipods


def cipherCaesar(namespace):
    fin = open(namespace.input[0], 'r')
    fout = open(namespace.output[0], 'a')
    for line in fin:
        cipher = ''
        for i in range(0, len(line)):
            asciiCode = ord(line[i])
            if asciiCode > 64 and asciiCode < 91:
                char = chr((asciiCode + namespace.shift - 65) % 26 + 65)
            elif asciiCode > 96 and asciiCode < 123:
                char = chr((asciiCode + namespace.shift - 97) % 26 + 97)
            else:
                char = line[i]
            cipher += char
        fout.write(cipher)
    return


def cipherVigenere(namespace):
    fin = open(namespace.input[0], 'r')
    fout = open(namespace.output[0], 'a')
    c = 0
    key = namespace.key.upper()
    if namespace.type == 'av' or namespace.type == 'antivigenere':
        key = antipod(key)
    for line in fin:
        cipher = ''
        for i in range(0, len(line)):
            asciiCode = ord(line[i])
            keyCode = ord(key[c])
            keyCode -= 65
            if asciiCode > 64 and asciiCode < 91:
                char = chr((asciiCode + keyCode - 65) % 26 + 65)
            elif asciiCode > 96 and asciiCode < 123:
                char = chr((asciiCode + keyCode - 97) % 26 + 97)
            else:
                char = line[i]
            cipher += char
            c = (c + 1) % len(key)
        fout.write(cipher)
    return


def cipherVernam(namespace):
    fin = open(namespace.input[0], 'r')
    fout = open(namespace.output[0], 'a')
    key = []
    for line in fin:
        cipher = ''
        for i in range(0, len(line)):
            asciiCode = ord(line[i])
            keyCode = random.randint(0, 26)
            if asciiCode > 64 and asciiCode < 91:
                char = chr((asciiCode + keyCode - 65) % 26 + 65)
            elif asciiCode > 96 and asciiCode < 123:
                char = chr((asciiCode + keyCode - 97) % 26 + 97)
            else:
                char = line[i]
                keyCode = 0
            cipher += char
            key.append(keyCode)
        fout.write(cipher)
    return


def main():
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.type == 'c' or namespace.type == 'caesar':
        cipherCaesar(namespace)
    elif namespace.type == 'v' or namespace.type == 'vigenere':
        cipherVigenere(namespace)
    elif namespace.type == 've' or namespace.type == 'vernam':
        cipherVernam(namespace)
    elif namespace.type == 'ac' or namespace.type == 'anticaesar':
        namespace.shift *= -1
        cipherCaesar(namespace)
    elif namespace.type == 'av' or namespace.type == 'antivigenere':
        cipherVigenere(namespace)
    else:
        print 'Incorrect option, finishing the program'
