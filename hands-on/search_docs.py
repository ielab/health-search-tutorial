#!/usr/bin/env python3



import argparse
import sys
import json
import random

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

INDEX_NAME = 'wsdm-health-search'

def search_file(query_file, variation=0):
    with open(query_file) as fh:
        query_json = json.load(fh)
        for topic in query_json:
            qid = topic['qId'].replace('trec', '').replace('-', '')
            variation = min(variation, len(topic['keywords'])-1)
            keyword = topic['keywords'][variation]['keywords'] # choose the first keyword
            search(keyword, qid)


def search(query, qid=''):
    query_payload = '{"query": {"match": {"all": "{'+query+'}"}}}'
    results = helpers.scan(es, query=query_payload, index=INDEX_NAME, doc_type='clinical_trial', preserve_order=True)

    if qid=='':
        print('{}\t{}\t\t{}\t{}\n--'.format("query", "doc", "score", "rank"), file=sys.stderr)

    qid = qid if len(qid) > 0 else query.replace(' ', '_')

    count = 0
    for count, hit in enumerate(results):
        print('{}\t0\t{}\t{}\t{}\tRunId'.format(qid, hit['_id'], count+1, round(hit['_score'],4)))
    print("{}: {} results".format(qid, count+1), file=sys.stderr)

if __name__ == '__main__':
    '''
    Searches in an Elastic index.
    '''

    parser = argparse.ArgumentParser(description="Annotate free-text documents with UMLS and format in JSON.")
    parser.add_argument('-f', '--query_file', help='Search using a query file contain a number of queries.')
    parser.add_argument('-v', '--variation', help='Which query variation to select.', default=0, type=int)
    parser.add_argument('query', help='Search given the input text.', nargs='?')
    args = parser.parse_args()

    if args.query_file:
        print("Searching using {}.".format(args.query_file), file=sys.stderr)
        search_file(args.query_file, args.variation)
    elif args.query:
        search(args.query.strip())
    else:
        parser.print_usage()

