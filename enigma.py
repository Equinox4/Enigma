#!/usr/bin/python3

from string import ascii_uppercase
from collections import deque
from random import seed, sample
from sys import exit


ALPHABET = list(ascii_uppercase)
ROTORS_CONF = [
    { 'seed': '7', 'position': 'U' },
    { 'seed': '4', 'position': 'H' },
    { 'seed': '9', 'position': 'G' },
]
PERMUTATIONS = {
    'J': 'K',
    'V': 'C'
} # two pairs of letters that will be permuted
ROTORS = list()

def get_initialized_rotors():
    rotors = list()
    for num_rotor in range(len(ROTORS_CONF)):
        rotor = make_rotor(ROTORS_CONF[num_rotor]['seed'])
        rotor = set_rotor_position(rotor, ROTORS_CONF[num_rotor]['position'])
        rotors.append(rotor)

    return rotors

def make_rotor(my_seed):
    seed(my_seed)

    return sample(ALPHABET, len(ALPHABET))

def set_rotor_position(rotor, rotor_position):
    rotor = deque(rotor)
    while rotor[0] != rotor_position:
        rotor.rotate(1)

    return list(rotor)

def encrypt(text):
    input_list = list(text)
    output_list = list()
    if not verify(text_list):
        print('Your input text contain a letter that is not supported.') # afficher l'alphabet
        exit(1)
    for letter in text:
        output_list.append(process(letter))

    return str(output_list)

def decrypt():
    pass

def process(letter):
        index_rotor1 = ROTORS[0].index(letter)
        permut = ROTORS[1]

def verify(text):
    for letter in text:
        if letter not in ALPHABET:
            return False

    return True

def rotate_rotors():
    pass


ROTORS = get_initialized_rotors()
