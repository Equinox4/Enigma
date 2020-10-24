#!/usr/bin/python3

from string import ascii_uppercase
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

# /!\ implémenter le réflecteur /!\

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
    initialized_rotor = rotor
    while initialized_rotor[0] != rotor_position:
        initialized_rotor = rotate(initialized_rotor)

    return initialized_rotor

def encrypt(text):
    input_list = list(text)
    output_list = list()
    if not verify(input_list):
        print('Your input text contain a letter that is not supported.') # afficher l'alphabet
        exit(1)
    for letter in input_list:
        output_list.append(process(letter))

    return ''.join(output_list)

def decrypt():
    pass

def process(letter_in):
    letter_out = ''
    alphabet = ALPHABET
    for rotor in ROTORS:
        letter_out = rotor[alphabet.index(letter_in)]
        alphabet = rotor
#       add reflector here
    rotate_rotors()

    return letter_out
        

def verify(text):
    for letter in text:
        if letter not in ALPHABET:
            return False

    return True

def rotate_rotors():
    ROTORS[0] = rotate(ROTORS[0])
    for rotor_num in range(len(ROTORS)):
        if ROTORS[rotor_num][0] == ROTORS_CONF[rotor_num]['position']:
            ROTORS[rotor_num + 1] = rotate(ROTORS[rotor_num + 1])

def rotate(my_list):
    return my_list[1:] + my_list[:1]

ROTORS = get_initialized_rotors()
print(encrypt('AABB'))
