#!/usr/bin/env python3



import argparse
import json

from glob import glob
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch()


INDEX_NAME = 'wsdm-health-search'

def index_doc(filename):
    with open(filename) as fd:
        print("Indexing {}.".format(filename))
        json_content = json.load(fd)

        doc_id = filename[filename.rfind('/')+1:].replace('.json', '')

        res = es.index(index=INDEX_NAME, doc_type='clinical_trial', id=doc_id, body=json_content)
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
        if es.indices.exists(index=INDEX_NAME):
            resp = es.indices.delete(index=INDEX_NAME)
            print("Deleting index '{}'. Response is {}.".format(INDEX_NAME, resp))

    if not es.indices.exists(index=INDEX_NAME):

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
        es.indices.create(body=settings, index=INDEX_NAME)

    if args.doc_dir:
        print("Indexing all docs in {}.".format(args.doc_dir))
        docs = glob('{}/*.json'.format(args.doc_dir))
        for filename in docs:
            index_doc(filename)
        print("Completed indexing {} documents in {} to {}.".format(len(docs), args.doc_dir, INDEX_NAME))
    elif args.file:
        index_doc(args.file)

