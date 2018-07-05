#!/usr/bin/env python3



import argparse
import logging
import json

from tqdm import tqdm
from glob import glob
from client import get_quickumls_client
import os

logger = logging.getLogger(__file__)

matcher = get_quickumls_client()


def annotate_doc(filename):
    with open(filename) as fd:
        doc = {'text': '', 'cuis': '', 'concepts':''}
        for line in fd:
            doc['text'] = doc['text'] + line
            concepts = annotate_text(line.strip())
            if len(concepts) > 0:
                doc['cuis'] = doc['cuis'] + ' '.join(concepts.keys()) + ' '
                doc['concepts'] = doc['concepts'] + ', '.join(concepts.values()) + ' '
    with open('annotated_'+filename+'.json', 'w') as outfile:
        json.dump(doc, outfile)
        #add trailing newline for POSIX compatibility
        outfile.write('\n')

def annotate_text(text):
    cuis = {}
    for phrase in matcher.match(text, best_match=True, ignore_syntax=False):
        for annotation in phrase:
            cuis[annotation['cui']] = annotation['term']
    return cuis


if __name__ == '__main__':
    '''
    Annotate free-text documents with UMLS and format in JSON.
    '''

    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="Annotate free-text documents with UMLS and format in JSON.")
    parser.add_argument('-d', '--doc_dir', help='Directory to process.')
    parser.add_argument('-f', '--file', help='File to process.')
    parser.add_argument('text', help='Text to annotation.', nargs='?')
    args = parser.parse_args()

    if args.doc_dir:
        if not os.path.exists('annotated_'+args.doc_dir):
            os.makedirs('annotated_'+args.doc_dir)
        for filename in tqdm(glob('{}/*'.format(args.doc_dir))):
            if filename.endswith('.json'):
                continue
            annotate_doc(filename)
    elif args.file:
        annotate_doc(args.file)
    elif args.text:
        print(annotate_text(args.text))
    else:
        parser.print_usage()
