import os
import sys
import argparse

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
    parser = argparse.ArgumentParser(description=program_descripton,formatter_class=argparse.RawTextHelpFormatter, add_help=True, usage='python -m payall -c <crypto> -t <type>')parser = argparse.ArgumentParser(description=program_descripton,formatter_class=argparse.RawTextHelpFormatter, add_help=True, usage='python -m gapi -h')

if __name__=="__main__":
    main()