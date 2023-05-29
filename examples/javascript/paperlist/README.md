# paperlist

This JS script uses the Semantic Scholar API to query the publication list of an author (or a lab/group) using their Semantic Scholar ID(s) and offers multiple options to academics and labs to incorporate them into their websites.
Using the list and table options also provides easy-to-click buttons that can copy bib entries as well as report issues with the paper.

## Usage

Please add the following code snippet inside the head tag of the webpage.
```
<link href="https://niket.tandon.info/assets/papers/style.css" rel="stylesheet">
<script src="https://niket.tandon.info/assets/papers/get_papers.js" type="text/javascript">
```

To use it on your personal website, please add the following code snippet inside the body tag.
```
<papers_list> </papers_list>
<script> populate_papers("#123467"); </script>
```
`#1234567` corresponds to the Semantic Scholar ID of the person whose publication list is to be displayed.

To use it on an organization's website, please add the following code snippet inside the body tag.
```
<papers_list> </papers_list>
<script> populate_lab_papers(["#123467", "#456789"]); </script>
```
`#1234567` and `#456789` correspond to the Semantic Scholar IDs of people in the organization whose publication list is to be displayed.

## Advanced Usage

`paperlist` serves publications through two functions, whose signatures are listed below:
1. `populate_papers(scholar_id_str, format, exclude_paper_ids, report_mode)`
2. `populate_lab_papers(scholar_ids, format, exclude_paper_ids, report_mode)`

`scholar_id_str` is the Semantic Scholar ID of the author, `scholar_ids` is a list of IDs (of authors in an organization) to retrieve papers for. `format` can be `list` (which populates an HTML list), `table` (which populates an HTML table) and `json` which returns all the data in a JSON format (make sure to have a variable to store data). `exclude_paper_ids` can optionally take a list of Semantic Scholar paper IDs that should not be displayed (in case of errors). Setting `report_mode` to `true` adds a Report button for each paper, which is linked to an error reporting application.

### JSON objects

Below is an example JSON object that is returned when `populate_papers` is called with `json` format.

```
{
	"author_meta": {
		"author_name": str,
		"author_id": int,
		"citation_count": int,
		"h_index": int,
		"paper_count": int
	},
	"json_paper_list": [ {
			"paper_title": str,
			"paper_id": str,
			"author_list": str,
			"highlighted_author_list": str,
			"bib": str,
			"citation_count": int,
			"publicationVenue": str,
			"venue": str,
			"abbreviated_venue": str,
			"year": int
		},
	]
}
```

Below is an example JSON object that is returned when `populate_lab_papers` is called with `json` format.

```
{
	"author_meta": [ {
			"author_name": str,
			"author_id": int,
			"citation_count": int,
			"h_index": int,
			"paper_count": int
		},
	]
	"json_paper_list": [ {
			"paper_title": str,
			"paper_id": str,
			"author_list": str,
			"highlighted_author_list": str,
			"bib": str,
			"citation_count": int,
			"publicationVenue": str,
			"venue": str,
			"abbreviated_venue": str,
			"year": int
		},
	]
}
```