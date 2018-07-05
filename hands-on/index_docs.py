#!/usr/bin/env python3



import argparse
import json

from glob import glob
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch()


def index_doc(filename):
    with open(filename) as fd:
        print("Indexing {}.".format(filename))
        json_content = json.load(fd)

        doc_id = filename[filename.rfind('/')+1:].replace('.json', '')

        res = es.index(index='sigir-health-search', doc_type='clinical_trial', id=doc_id, body=json_content)
        if res['result'] != 'created':
            print(res)

if __name__ == '__main__':
    '''
    Index json documents to Elastic.
    '''

    parser = argparse.ArgumentParser(description="Index json documents to Elastic.")
    parser.add_argument('-rm', '--remove_index', action='store_true', help='Delete the index.')
    parser.add_argument('-d', '--doc_dir', help='Index a whole directory of documents.')
    parser.add_argument('-f', '--file', help='Index a single file.')
    args = parser.parse_args()

    if args.remove_index:
        if es.indices.exists(index='sigir-health-search'):
            resp = es.indices.delete(index='sigir-health-search')
            print("Deleting index 'sigir-health-search'. Response is {}.".format(resp))

    if not es.indices.exists(index='sigir-health-search'):

        mapping = '''{
            "mapping": {
                "user": {
                    "_all": {
                        "enabled": true
                    }
                }
            }
        }'''


        settings = {
          "mappings": {
            "clinical_trial": {
              "properties": {
                "text": {
                  "type":    "text",
                  "copy_to": "all"
                },
                "cuis": {
                  "type":    "text",
                  "copy_to": "all"
                },
              "concepts": {
                  "type": "text",
                  "copy_to": "all"
              },
                "all": {
                  "type":    "text"
                }
              }
            }
          }
        }
        # create index
        es.indices.create(body=settings, index='sigir-health-search')

    if args.doc_dir:
        print("Indexing all docs in {}.".format(args.doc_dir))
        for filename in glob('{}/*.json'.format(args.doc_dir)):
            index_doc(filename)
    elif args.file:
        index_doc(args.file)

