# SIGIR Health Search Tutorial - Hands on session instruction

The following are instructions on the SIGIR Health Search Tutorial hands-on session.

## Setup

`docker pull`

Start the quickumls server

`docker run -P Y:Y xx python3 server.py`

### Details of the task

In the task you will:

1. Take a collection of clinical trials, annotate them with medical concepts, producing documents with both term and concept representation.
2. Index these documenmts in Elastic with multi term/concepts fields.
3. Search Elatic with either term or concept, demonstrating semantic search capabilities.

### Files provided

In this direction are the following files:

File | Description
--- | ---
`README.md` | This file
`adhoc-queries.json` | Test query topics
`annotate_docs.py` | Script to take plain text docs and annotated with UMLS concepts; see `annotate_docs.py -h` for info.
`docs` | 500 sample clinical trial documents in plain text
`index_docs.py` | Script to take annotated documents and index in Elastic; see `index_docs.py -h` for details
`qrels-clinical_trials.txt` | Qrels for the test query topics and docs.
`requirements.txt` | List of python dependecies.
`search_docs.py` | Script for searching with Elastic; see `search_docs.py -h` for details.

## Tutorial tasks

### Step 1 - View documents

Have a look at the clinical trials documents in the `docs` directory.

#### Step 2 - Annotating with UMLS concepts

We will now identify medical concepts from free-text. 

First start the QuickUMLS service in the background:

`python /QuickUMLS-master/server.py /quickumls-data &`

Then lets do a test to identify some medical concepts from the phases "Family history of lung cancer". Run:

`python annotate_docs.py "Family history of lung cancer"`

You should see some JSON returns with concepts identified; e.g.:

```{'C0260515': 'Family history of cancer', 'C0728711': 'Family history of lung cancer'}```

Now we will use the same script to annotated all the documents in `docs`:

`python annotate_docs.py -d docs`

This will annotated each document and write the output to `annotated_docs` as individual JSON file. Take a look in some files and you will see the document now has three fields:

* `text` containing the original test;
* `cuis` contained the UMLS concept ids for concepts found in the text; and 
* `concepts` containing the umls concepts names.

### Step 3 - Indexing with Elastic Search

First, start Elastic with:

`/elasticsearch-6.3.0/bin/elasticsearch &`

Now we want to index all the annotated documents to Elastic:

`python index_docs.py -d annotated_docs`

You can check the indexed docs by searching for all docs in your browser as:

[http://localhost:9200/sigir-health-search/_search?pretty](http://localhost:9200/sigir-health-search/_search?pretty)

You'll see the documents have been indexed with the three fields.

### Step 3 - Searching

Have a play with various searching by setting `q=queryterm`; e.g., to search for "cancer"

[http://localhost:9200/sigir-health-search/_search?q=cancer&pretty](http://localhost:9200/sigir-health-search/_search?q=lung&pretty)

To run a search and get a results in TREC format run:

`python search_docs.py -q "lung cancer"` (remember the quotes for query term)

This will produce a ranked list in trec_eval format.

We have also provided a set of query topics to use in `adhoc-queries.json`. Note that this is a special test collection we developed of clinical trials; it has multiple query variations, provided by different doctors, for a single query topic. To do a search using these topics run:

`python search_docs.py -f adhoc-queries.json`

Note, because there are multiple query variations for a topic, the script will choose a variation from a random person and run that - this highlights some of issues in query variation in health search.

Run the script again but this time pipe the output to a results file:

`python search_docs.py -f adhoc-queries.json > trec_results.txt`

We can now use the qrels to evaluate our system using trec_eval:

`trec_eval qrels-clinical_trials.txt trec_results.txt`

## Todo

add trec_eval

staring quickumls

starting elastic