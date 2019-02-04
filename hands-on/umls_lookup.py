#!/usr/bin/env python3

import argparse

class UMLSLookup:

    def __init__(self, mapping_file="etc/MRCONSO.RRF.idx"):
        self.mapping = {}
        with open(mapping_file) as fh:
            for line in fh:
                cui, desc = line.strip().split("\t")
                self.mapping[cui] = desc

    def umls_lookup(self, cui):
        return self.mapping.get(cui, "")

if __name__ == '__main__':
    '''
    Lookup UMLS concepts
    '''

    parser = argparse.ArgumentParser(description="Given a UMLS CUI, display the description.")
    parser.add_argument('cuis', nargs="*", help='Search using a query file contain a number of queries.')
    args = parser.parse_args()

    lookup = UMLSLookup()
    
    for cui in args.cuis:
        print('{}\t{}'.format(cui, lookup.umls_lookup(cui)))
