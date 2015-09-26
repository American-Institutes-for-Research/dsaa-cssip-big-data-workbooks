PyALM Docs
==========

Contents
--------
1. Basic usage
	1. Summary level information
	2. More detailed source information
2. Working with data
	1. Working with history
	2. Working with events

Basic usage
-----------

###Summary Level Information###

After installation (see the README) import the library and call the API give a doi and 
the information level required (summary, event, history, detail). We are starting with 
the API call which just gives summary level information.
{{ d['examples/example.py|idio|pycon|pyg']['import-the-library'] }}
{{ d['examples/example.py|idio|pycon|pyg']['get-single-doi'] }}

The returned object provides some basic information:
{{  d['examples/example.py|idio|pycon|pyg']['print-article'] }}

We can then start getting some summary information about the returned object. With the
summary API call you obtain the basic bibliographic information (`title`, `doi`,
`url`, `publication_date`), the most recent `update_date`, the identifiers for the paper 
(`doi`, `pmid`, `pmcid`) alongside summary metrics information (`views`, `shares`, 
`bookmarks`, `citations`). In each case the relevant information can be obtained as an 
attribute of the response:	

{{  d['examples/example.py|idio|pycon|pyg']['print-biblio'] }}
{{  d['examples/example.py|idio|pycon|pyg']['print-ids'] }}
{{  d['examples/example.py|idio|pycon|pyg']['print-stats'] }}

The returned object is always a list of ArticleALM objects. If a single DOI is passed
the list will be of length one. Multiple DOIs should be passed to the `get` method as a
list of strings of the form `10.1371/journal.pgen.1004001`.

{{  d['examples/example.py|idio|pycon|pyg']['multiple-dois'] }}

###More Detailed Source Information###

To obtain more detailed information on each ALM source from the ALM API a request should 
be made for from detailed information. The options available are `event`, `history`, and 
`detail`. More information on the different levels can be found below. For all the info 
levels a specific set of sources can be specified from one to a list,
to all (by omitting the `source` option). Specific sources are then available via the 
`sources` attribute of the returned object.

{{  d['examples/example.py|idio|pycon|pyg']['get-event-level-cites'] }}

Quantitative information is available for the requested sources divided into the same
categories provided by summary level info (`views`, `shares`, `bookmarks`, `citations`).
If a category is not populated, eg `shares` for the twitter source then it will return
`None`.

{{  d['examples/example.py|idio|pycon|pyg']['print-cites-metrics'] }}

Further information about the source itself and the last time the ALM App instance
updated its records are also available from attributes of the source object.

{{  d['examples/example.py|idio|pycon|pyg']['source-cites-attributes'] }}

Working with data
-------------------
When requesting more detailed data there are two options `event` and `history`. 
The `history` option provides information on the ALM over a series of timepoints. These
timepoints are those when the ALM App polled the data source rather than the date or time
of specific events. Finally the `detail` level provides both event and history data.

Event level data provides information on the specific events contributing to an ALM 
count. For instance, this will provide information on the individual tweets contributing 
to the overall count or individual citation events to the article of interest. 

###Working with histories###

History data is parsed from the original JSON to an ordered list of duples where the
first element is a `datetime.datetime` object and the second is the integer total count 
for that metric. It is obtained from the `histories` attribute of the source object. The 
list is ordered from oldest to newest record. 

{{  d['examples/example.py|idio|pycon|pyg']['get-history-level-cites'] }}

The number of elements in the `histories` list reflects the frequency with which the 
App instance updates the record and is not sensitive to the actual events which cause
the count.
  
###Working with events###

The event information is available via the `events` attribute on the source. Event data 
is not parsed direct from the return JSON object and needs to be handled by the user
depending on their needs.

{{  d['examples/example.py|idio|pycon|pyg']['get-event-level-cites'] }}
{{  d['examples/example.py|idio|pycon|pyg']['print-cites-events'] }}

The `events` module provides a set of classes for handling specific types of events.