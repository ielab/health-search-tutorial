#!/usr/bin/env python3

import argparse
import logging
import json
import requests
import os
import multiprocessing
import threading

from tqdm import tqdm
from glob import glob

from umls_lookup import UMLSLookup

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.INFO)

def annotate_doc(filename, annotation_service='http://localhost:5000/match'):
    with open(filename) as fd:
        lines = fd.readlines()
        doc = {'text': '', 'cuis': '', 'concepts':''}
        for line in tqdm(lines, desc=filename):
            if len(line.strip()) == 0:
                continue
            doc['text'] = doc['text'] + line
            concepts = annotate_text(line.strip(), annotation_service)
            if len(concepts) > 0:
                doc['cuis'] = doc['cuis'] + ' '.join(concepts.keys()) + ' '
                doc['concepts'] = doc['concepts'] + ', '.join(concepts.values()) + ' '
    with open('annotated_'+filename+'.json', 'w') as outfile:
        json.dump(doc, outfile)
        #add trailing newline for POSIX compatibility
        outfile.write('\n')

def annotate_text(text, annotation_service):
    #print({'text': text})
    resp = requests.post(annotation_service, json={'text': text})
    if resp.status_code != 200:
         raise Exception('POST / {}: {}'.format(resp.status_code, resp.text))
    #for concept in resp.json():
    #    print('\t', {concept['cui']: concept['term']})
    return {concept['cui']: concept['term'] for concept in resp.json()}

if __name__ == '__main__':
    '''
    Annotate free-text documents with UMLS and format in JSON.
    '''

    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="Annotate free-text documents with UMLS and format in JSON.")
    parser.add_argument('-d', '--doc_dir', help='Directory to process.')
    parser.add_argument('-f', '--file', help='File to process.')
    parser.add_argument('--annotation_service', default='http://localhost:5000/match')
    parser.add_argument('text', help='Text to annotation.', nargs='?')
    args = parser.parse_args()

    if args.doc_dir:
        if not os.path.exists('annotated_'+args.doc_dir):
            os.makedirs('annotated_'+args.doc_dir)

        docs = [filename for filename in glob('{}/*'.format(args.doc_dir)) if not filename.endswith('.json')]

        for filename in tqdm(docs, desc="Annotating files in '{}'".format(args.doc_dir) ):
            annotate_doc(filename)

    elif args.file:
        annotate_doc(args.file, args.annotation_service)
    elif args.text:
        mapper = UMLSLookup()
        for cui, term in annotate_text(args.text, args.annotation_service).items():
            print('{}:\t"{}" ({})'.format(cui, term, mapper.umls_lookup(cui)))
    else:
        parser.print_usage()
