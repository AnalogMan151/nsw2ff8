#!/usr/bin/env python3
# Author: AnalogMan
# Modified Date: 2019-09-08
# Purpose: Injects or extracts FF8 save data to Switch save

import os, argparse

def main():
    print('\n======== FF8 NSW Save Tool ========\n\n')
    
    if sys.version_info <= (3,1,0):
        print('Python version 3.1.x+ needed to run this script.\n\n')
        return 1

    # Arg parser for program options
    p = argparse.ArgumentParser(description='Inject or extract FF8 save data to Nintendo Switch save')
    g = p.add_mutually_exclusive_group(required=True)
    p.add_argument('nsw_file', help='Path to Switch save')
    p.add_argument('ff8_file', help='Path to FF8 save')
    g.add_argument('-i', '--inject', action='store_true', help='Inject FF8 save into Switch save')
    g.add_argument('-e', '--extract', action='store_true', help='Extract FF8 save from Switch save')
    # Check passed arguments
    args = p.parse_args()

    # Check if required files exist
    if os.path.isfile(args.nsw_file) == False:
        print('Switch save cannot be found\n\n')
        return 1

    if args.extract == True:
        try: 
            with open(args.nsw_file, 'rb') as nsw:
                save_len = int.from_bytes(nsw.read(4), byteorder='little')
                ff8_data = nsw.read(save_len)
            with open(args.ff8_file, 'wb') as ff8:
                ff8.write(ff8_data)
            print('FF8 save file extracted successfully.\n\n')
        except:
            print('Save could not be extracted.\n\n')
    
    if args.inject == True:
        if os.path.isfile(args.ff8_file) == False:
            print('FF8 save cannot be found\n\n')
            return 1
        try:
            with open(args.ff8_file, 'rb') as ff8:
                ff8_data = ff8.read()
            with open(args.nsw_file, 'rb+') as nsw:
                nsw.write((len(ff8_data)).to_bytes(4, byteorder='little'))
                nsw.write(ff8_data)
            print('FF8 save file injected successfully.\n\n')
        except:
            print('Save could not be injected.\n\n')
    
if __name__ == "__main__":
    main()
