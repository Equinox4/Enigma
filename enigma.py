#!/usr/bin/python3

from string import ascii_uppercase
from collections import deque
from random import seed
from random import sample
from sys import exit


ALPHABET = list(ascii_uppercase)
SEED = 5 # change seed equals to change rotors
ROTORS = list()

ROTORS_POSITIONS = 'UHG' # initial rotors position
PERMUTATIONS = 'JKVC' # two pairs of letter that will be permuted

#temp
nb_rotations_rotor1 = 0
nb_rotations_rotor2 = 0



def initRotors(nb_rotors = 3):

	for num_rotor in range(nb_rotors):

		rotor = shuffle(num_rotor + SEED)
		rotor = setRotorPosition(rotor, ROTORS_POSITIONS[num_rotor])
		ROTORS.append(rotor)


def setRotorPosition(rotor, rotor_position):

	rotor = deque(rotor)
	while rotor[0] != rotor_position:
		rotor.rotate(1)

	return list(rotor)

def shuffle(my_seed):

	seed(my_seed)
	return sample(ALPHABET, len(ALPHABET))


def encrypt(text):

	text_list = list(text)
	if not verify(text_list):
		exit(1)
	for letter in text:
		

		
#############################
#temporary functions
def verify(text):

	for letter in text:
	
		if letter not in ALPHABET:
			return False
		
	return True

def setPermutation(letter_couple):

	pass
	
def rotate(rotor1, rotor2, rotor3):

	pass	

def substitute(letter, rotor):

	pass
	
def process(msg_in):

	msg_out = list()
	for letter in list(msg_in):
		index_rotor1 = ROTORS[0].index(letter)
		permut = ROTORS[1]
		
	return msg_out

##########

initRotors()
text_in = input("Hello World !")
text_out = encrypt(text_in)
print(text_out)

