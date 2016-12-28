#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | linker                            
# Last Modified: 15/09/2016
#
#########################################################HEAD#


from core.Internal import (GetRootModules)

import importlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--module", help=" Script module to run.")
args = parser.parse_args()


if __name__=="__main__":
	for modules in GetRootModules().findall('module'):
		if args.module == modules.get('name'):
			category = modules.find('category').text
			filename = modules.find('filename').text
			ModuleToStart = importlib.import_module("modules."+category+"."+filename) 
			init=ModuleToStart.init()
			output = ""
			for VAR in init.options:
				output += VAR+":_:"+str(init.options[VAR][0])+":_:"+str(init.options[VAR][1])+":_:"+str(init.options[VAR][2])+":_:_:"
	 		
			print output[:-5]
	






