#!/usr/bin/env python

# This file takes a folder containing genomic bam files and template.json as an input and after modifying template.json outputs the 
# file on the output folder.


import json
import argparse
import sys
import os
from collections import OrderedDict

FILE_EXT = '.json'

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template',
                        help='Template file path', required=True)
    parser.add_argument('-i', '--inputdir',
                        help='Bam file name', required=True)
    parser.add_argument('-o', '--outdir',
                        help='Output Location', required=True)

    args = parser.parse_args()

    if  os.path.isfile(args.inputdir):
        print "Input should be a folder"
        exit(1)
    if  os.path.isfile(args.outdir):
        print "Output should be a folder"
        exit(1)

    return args.template, args.inputdir, args.outdir

def update_template():
    template, input_dir, output_dir = parse_arguments()
    for element in os.listdir(input_dir):
      if element.endswith(".bam"):
         with open(template) as fp:
            data = json.load(fp, object_pairs_hook=OrderedDict)

         fname = os.path.splitext(os.path.basename(element))[0]
         fext = os.path.splitext(os.path.basename(element))[1]

         data['GenericPreProcessingToGVCFWorkflow.sample_name']  = fname

         ext = os.path.splitext(data['GenericPreProcessingToGVCFWorkflow.base_file_name'])[1]
         data['GenericPreProcessingToGVCFWorkflow.base_file_name'] = fname+ext

         del data['GenericPreProcessingToGVCFWorkflow.flowcell_unmapped_bams'][:]
         data['GenericPreProcessingToGVCFWorkflow.flowcell_unmapped_bams'].append(os.path.join(input_dir, element))

         s = data['GenericPreProcessingToGVCFWorkflow.final_gvcf_name'].split(".")
         s[0] = fname
         data['GenericPreProcessingToGVCFWorkflow.final_gvcf_name'] = ".".join(s)

         data['GenericPreProcessingToGVCFWorkflow.unmapped_bam_suffix'] = fext

         with open(os.path.join(output_dir, fname + FILE_EXT), 'w') as mod:
            json.dump(data, mod, indent=4, separators=(',',':'))

         fp.close()

if __name__ == '__main__':
    update_template()
