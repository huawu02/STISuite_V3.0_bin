#!/usr/bin/env python

import os
import json

# Parse a config file
def parse_config(config_json_file):
    """
    Take a json file, read and return the contents
    """

    if not os.path.isfile(config_json_file):
        raise ValueError('No config file could be found!')

    # Read the config json file
    with open(config_json_file, 'r') as jsonfile:
        config = json.load(jsonfile)

    return config

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--config_file', type=str, dest="config_file", default='/flywheel/v0/config.json', help='Full path to the input json config file.')
    ap.add_argument('--debug', '-d', type=bool, dest="debug", default=False, help='show debug print statements')
    args = ap.parse_args()

    config = parse_config(args.config_file)
    flywheel_input = '/flywheel/v0/input/'
    flywheel_output = '/flywheel/v0/output'
    
    # Parameters from gear config  
    smv_size = config['config']['smv_size']
    pad_size = config['config']['pad_size']

    # Unzip dicom data 
    dicomfile = config['inputs']['dicom']['location']['path']
    print("dicomfile: %s\n" % dicomfile)
    os.system("unzip %s -d %s" % (dicomfile, flywheel_input))
    dicomdir = os.path.join(flywheel_input, os.path.splitext(os.path.basename(dicomfile))[0])
    print("dicomdir: %s\n" % dicomdir)
    
    # run STI from flywheel output dir
    cmd = ("cd %s; run_STI_pipeline_CNI.sh /opt/mcr/v95 %s %s %d %d" %(flywheel_output, dicomdir, flywheel_output, pad_size, smv_size))
    print(cmd)
    os.system(cmd)

