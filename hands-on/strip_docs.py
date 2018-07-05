#!/usr/bin/env python3

import fileinput
import xmltodict
import argparse

from tqdm import tqdm
from glob import glob

def process_doc(filename):
    with open(filename) as fd:
        try:
            doc = xmltodict.parse(fd.read())
        except:
            print('Unable to parse XML for {}'.format(filename))
            raise

        brief_title = doc['clinical_study']['brief_title']
        brief_summary = doc['clinical_study']['brief_summary']['textblock']

        with open(filename.replace('xml', 'txt'), 'w') as outfile:

            outfile.write('TITLE:\n')
            outfile.write('      ' + brief_title + '\n')
            outfile.write('SUMMARY:\n')
            outfile.write('      ' + brief_summary + '\n')

            try:

                if 'detailed_description' in doc['clinical_study']:
                    detailed_description = doc['clinical_study']['detailed_description']['textblock']
                    outfile.write('DETAILED DESCRIPTION:\n')
                    outfile.write('      ' + detailed_description + '\n')

                if 'eligibility' in doc['clinical_study'] and 'criteria' in doc['clinical_study']['eligibility']:
                    eligibility_criteria = doc['clinical_study']['eligibility']['criteria']['textblock']
                    outfile.write('ELIGIBILITY CRITERIA:\n')
                    outfile.write('      ' + eligibility_criteria + '\n')

            except:
                print("Unable to find the right content in {}".format(filename))
                raise

if __name__ == '__main__':
    '''
    Converts clinical trial XML files to plain text.
    '''

    parser = argparse.ArgumentParser(description="Converts clinical trial XML files to plain text..")
    parser.add_argument("xml_dir")
    # parser.add_argument("-summary", action="store_true", help="Extract the summary section.")
    # parser.add_argument("-tsv", action="store_true", help="outfile.write the results in tab separated format instead of TREC format. (For importing elsewhere; e.g., relevation!")
    args = parser.parse_args()

    for filename in tqdm(glob('{}/*.xml'.format(args.xml_dir))):
        process_doc(filename)

