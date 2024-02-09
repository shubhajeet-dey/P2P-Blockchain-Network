#!/usr/bin/env python3
from initialize import init_nodes
from utils import parseArguments
from copy import deepcopy
import sys

if __name__ == "__main__":
	
	# Parse here 
	inputs = parseArguments(deepcopy(sys.argv)) #this parses the command line argument into the parseArgument function which returns the arguments in the form of dictionary

	# I and T_Tx are given in milliseconds
	nodes = int(inputs['nodes'])
	z0 = float(inputs['z0'])
	z1 = float(inputs['z1'])
	T_tx = int(inputs['T_Tx'])
	I  = int(inputs['I'])

	# Initializing nodes and creating a P2P network
	nodeArray = init_nodes(nodes, z0, z1, I, T_Tx)