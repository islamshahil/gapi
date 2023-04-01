import os
import sys
import argparse
from controller import *

from importlib_metadata import version
import warnings

warnings.filterwarnings("ignore")
v = version('gapi')

def main():

	program_descripton = f'''
                    _ 
                   (_)
   __ _  __ _ _ __  _ 
  / _` |/ _` | '_ \| |
 | (_| | (_| | |_) | |
  \__, |\__,_| .__/|_|
   __/ |     | |      
  |___/      |_|      
          
GSheet Applications Programming Interface - v{v}
Created by Shahil
Copyright 2023. All rights reserved.
    '''