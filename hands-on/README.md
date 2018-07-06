# SIGIR Health Search Tutorial - Hands on session instructions

**Author**: Bevan Koopman, Guido Zuccon

This file is versioned at:

[https://github.com/ielab/health-search-tutorial/tree/master/hands-on](https://github.com/ielab/health-search-tutorial/tree/master/hands-on)

---


The following are instructions on the SIGIR Health Search Tutorial hands-on session.

This tutorial demostrates using a number of different tools to implement a search system in the health domain. These tools require some setup and configuration. To use the burden in this we have distributed them pre-build via a docker image. 

## Setup

1) First, **download and install docker** for your operating system.

Now we need two docker images: one for elastic and the other for this tutorial.

2) For elastic:

`docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.1`

3) For this tutorial:

`docker pull ielabgroup/health-search-tutorial`

**Alternative**: 

If the docker image was saved to file (not obtained via docker hub) then it can be loaded via: 

1. `gunzip health-search-tutorial-docker.tar.gz`
2. `docker load -i health-search-tutorial-docker.tar`.)

---

### Details of the task

In the task you will:

1. Take a collection of clinical trials, annotate them with medical concepts, producing documents with both term and concept representation.
2. Index these documenmts in Elastic with multi term/concepts fields.
3. Search Elatic with either term or concept, demonstrating semantic search capabilities.



## Tutorial tasks

### Step 0 - Fire up the tutorial docker image

`docker run --net="host" -it ielabgroup/health-search-tutorial`

This will run the start the docker image and you will be presented with a bash shell on a Ubuntu virtual machine. By default you will start off in the `/health-search-tutorial` directory. This contains all the scripts and documents for this tutorial.

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

### Step 1 - View some documents

Have a look at the clinical trials documents in the `docs` directory:

`less docs/NCT02631304`

### Step 2 - Annotating with UMLS concepts

We will now identify medical concepts from free-text. 

First start the QuickUMLS service in the background:

`python /QuickUMLS-master/server.py /quickumls-data &`

Then lets do a test to identify some medical concepts from the phases "Family history of lung cancer". Run:

`python annotate_docs.py "Family history of lung cancer"`

You should see some JSON returns with concepts identified; e.g.:

```{'C0260515': 'Family history of cancer', 'C0728711': 'Family history of lung cancer'}```

Now we will use the same script to annotated all the documents in `docs`:

`python annotate_docs.py -d docs`

This will annotated each document and write the output to `annotated_docs` as individual JSON file. 

**Note**: this process can be very slow on docker. You can Ctrl C to cancel it if its taking too long. We have already run this and the output is all in `annotated_docs`.

Now, take a look in some files (e.g., `less annotated_docs/NCT02631304.json`) and you will see the document now has three fields:

* `text` containing the original test;
* `cuis` contained the UMLS concept ids for concepts found in the text; and 
* `concepts` containing the umls concepts names.


### Step 3 - Indexing with Elastic Search

#### Starting Elastic

First, start Elastic. We will use the standard docker images provided by elastic to do this. 

Open a new terminal window and make sure you run this not in the tutorial docker but on your host machine:

`docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.1`

Ensure that the docker service is up and running by visiting: [http://localhost:9200/](http://localhost:9200/)

#### Indexing

Return to your tutorial docker shell.

Now we want to index all the annotated documents to Elastic:

`python index_docs.py -d annotated_docs`

This process will take each JSON document in `annoted_docs` and submit to Elatic search.

You can check the indexed docs by searching for all docs in your browser as:

[http://localhost:9200/sigir-health-search/_search?pretty](http://localhost:9200/sigir-health-search/_search?pretty)

You'll see the documents have been indexed with the three fields.

### Step 4 - Searching

Have a play with various searching by setting `q=queryterm`; e.g., to search for "cancer"

[http://localhost:9200/sigir-health-search/_search?q=cancer&pretty](http://localhost:9200/sigir-health-search/_search?q=lung&pretty)

To run a search and get a results in TREC format run:

`python search_docs.py -q "lung cancer"` (remember the quotes for query term)

This will produce a ranked list in trec_eval format.

We have also provided a set of query topics to use in `adhoc-queries.json`. Note that this is a special test collection we developed of clinical trials; it has multiple query variations, provided by different doctors, for a single query topic. To do a search using these topics run:

`python search_docs.py -f adhoc-queries.json`

Note, because there are multiple query variations for a topic, the script will choose a variation from a random person and run that - this highlights some of issues in query variation in health search.

### Step 5 - Evaluation

Run the script again but this time pipe the output to a results file:

`python search_docs.py -f adhoc-queries.json > trec_results.txt`

We can now use the qrels to evaluate our system using trec_eval:

`trec_eval qrels-clinical_trials.txt trec_results.txt`

### Step 6 - Time to play

Now we want to understand a bit about how different search can be done. Let us look at some concept-based searches. First, lets run some annotation to understand different medical concepts:

**Case 1**: `python annotate_docs.py "metastatic breast cancer"` gives us:

`{'C0278488': 'metastatic breast cancer'}`

But

**Case 2**: `python annotate_docs.py "breast cancer"` gives us

`{'C0006142': 'Breast cancer', 'C0678222': 'Breast cancer'}`

Notice the different medical concepts.

Now let's look at how this affects search:

* Searching for case 1 `python search_docs.py -q "C0278488"` yields 5 results.
* Searching for case 2 `python search_docs.py -q "C0006142 C0006142"` yields 8 different results.
* Searching for the original text of case 1 `python search_docs.py -q "metastatic breast cancer"` yields 107 different results.
* Searching for the original text of case 2 `python search_docs.py -q "breast cancer"` yields 103 different results.

We leave you now to experiment and discuss different search options and what impact they may have.