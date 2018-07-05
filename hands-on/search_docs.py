#!/usr/bin/env python3



import argparse
import sys
import json
import random

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()


def search_file(query_file):
    with open(query_file) as fh:
        query_json = json.load(fh)
        for topic in query_json:
            qid = topic['qId'].replace('trec', '').replace('-', '')
            keyword = random.choice(topic['keywords'])['keywords']
            search(keyword, qid)


def search(query, qid=''):
    query_payload = '{"query": {"match": {"all": "{'+query+'}"}}}'
    results = helpers.scan(es, query=query_payload, index='sigir-health-search', doc_type='clinical_trial', preserve_order=True)

    if qid=='':
        print('{}\t{}\t\t{}\t{}\n--'.format("query", "doc", "score", "rank"), file=sys.stderr)

    qid = qid if len(qid) > 0 else query.replace(' ', '_')

    count = 0
    for count, hit in enumerate(results):
        print('{}\t0\t{}\t{}\t{}\tRunId'.format(qid, hit['_id'], count+1, round(hit['_score'],4)))
    print("{}: {} results".format(qid, count), file=sys.stderr)

if __name__ == '__main__':
    '''
    Searches in an Elastic index.
    '''

    parser = argparse.ArgumentParser(description="Annotate free-text documents with UMLS and format in JSON.")
    parser.add_argument('-f', '--query_file', help='Search using a query file contain a number of queries.')
    parser.add_argument('-q', '--query', help='Search given the input text.')
    args = parser.parse_args()

    if args.query_file:
        print("Searching using {}.".format(args.query_file), file=sys.stderr)
        search_file(args.query_file)
    elif args.query:
        search(args.query.strip())
    else:
        parser.print_usage()

