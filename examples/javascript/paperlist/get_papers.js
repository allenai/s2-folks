
async function populate_lab_papers(scholar_ids, format="list", exclude_paper_ids=[], report_mode=false) {

    const url = 'https://api.semanticscholar.org/graph/v1/author/batch';
    const papers_fields = ['title', 'year', 'paperId', 'venue', 'citationStyles', 'citationCount', 'authors', 'externalIds', 'url', 'publicationVenue', 'isOpenAccess', 'openAccessPdf'];
    const author_fields = ['name', 'citationCount', 'hIndex', 'paperCount'];
    const sep = 'papers.';
    const requestParam = "?fields=" + sep + papers_fields.join( "," + sep) + "," + author_fields.join(",");
    var requestURL = url + requestParam;
    const request = new Request(requestURL, {
        method: 'POST',
        headers: {
           'Accept': 'application/json',
           'Content-Type': 'application/json'
        },
        body: JSON.stringify({"ids":scholar_ids})
    });
    const response = await fetch(request);
    const papersText = await response.text();
    const papersjson = JSON.parse(papersText);
    const allPaperData = parseBatchPapers(papersjson, exclude_paper_ids);
    // turn off highlighting author names for lab (current design decision)
    if (format == "list") {
      populateList(allPaperData, report_mode, false);
    }
    else if (format == "table") {
      populateTable(allPaperData, report_mode, false);
    }
    else if (format == "json") {
      return allPaperData;
    }
}


function render_papers(jsonPaperList, report_mode, format, highlight=true) {
    if (format == "list") {
      populateList(jsonPaperList, report_mode, highlight);
    }
    else if (format == "table") {
      populateTable(jsonPaperList, report_mode, highlight);
    }
    else if (format == "json") {
      return jsonPaperList;
    }
}

async function populate_papers(scholar_id_str, cache_url="", format="list", exclude_paper_ids=[], report_mode=false) {

    // Start loading the page with cache.
    var cache_dict = {};
    if (cache_url !== "") {
        console.log("Loading cached content first...");
        const cache_data = await loadJsonFile(cache_url);
        render_papers(cache_data, report_mode, format);
        for (const p of cache_data["json_paper_list"]) {
            cache_dict[p["paper_id"]] = p;
        }
    }

    const url = 'https://api.semanticscholar.org/graph/v1/author/';
    const papers_fields = ['title', 'year', 'paperId', 'venue', 'citationStyles', 'citationCount', 'authors', 'externalIds', 'url', 'publicationVenue', 'isOpenAccess', 'openAccessPdf'];
    const author_fields = ['name', 'citationCount', 'hIndex', 'paperCount'];
    const sep = 'papers.';
    const requestParam = "?fields=" + sep + papers_fields.join( "," + sep) + "," + author_fields.join(","); 
    var requestURL = url + scholar_id_str + requestParam;
    const request = new Request(requestURL);
    const response = await fetch(request);
    const papersText = await response.text();
    const papersjson = JSON.parse(papersText);
    jsonPaperList = paperListToJSON(papersjson, exclude_paper_ids);

    paperIds = get_paper_ids(jsonPaperList);
    paper_ids_str = String(paperIds);

    var papers_dict = {};
    for (const p of jsonPaperList["json_paper_list"]) 
        papers_dict[p["paper_id"]] = p;
    
    updated_json = await fetch_figure(paper_ids_str, papers_dict, cache_dict);
    var updatedJsonPaperList = {'author_meta': jsonPaperList['author_meta'], 'json_paper_list': Object.values(updated_json)};

    render_papers(updatedJsonPaperList, report_mode, format);
}

async function loadJsonFile(url) {
    try {
      const response = await fetch(url);
      const data = await response.json();
      return data;
    } catch (error) {
      console.log('Error fetching data:', error);
    }
  }
  
  function openImageThumbnail(figure, figureUrl) {
      figure.onclick = function() {
          const img_window = window.open(figureUrl, '_blank');
          img_window.document.write(`
              <html>
              <head>
              </head>
              <body>
              <img src=${figureUrl}></img>
              </body>
              </html>`
              );
      }
  }


function download_as_file(path, filename){
    // Create a new link
    const anchor = document.createElement('a');
    anchor.href = path;
    anchor.download = filename;

    // Append to the DOM
    document.body.appendChild(anchor);

    // Trigger `click` event
    anchor.click();

    // Remove element from DOM
    document.body.removeChild(anchor);
}
  
  function downloadImageThumbnail(figure, figureUrl) {
      figure.onclick = function() {
      // this starts downloading the image
          window.open(figureUrl, '_blank');
      }
  }
  

async function fetch_figure(all_paper_ids, papers_json_dict, cache_json_dict) {

    figure_urls_json = {};
    alternate_figure_url = "https://pbs.twimg.com/profile_images/1138107711923544064/qDsIE-Xl_400x400.png";

    // currently, this API endpoint supports loading upto 9 figures; when a 10th ID is added, it returns 502 Bad Gateway error
    // var endpoint = "https://qzi4sdg7tilsfj4dnt2pmrnadm0xaedr.lambda-url.us-west-2.on.aws/?id=" + paper_ids;

    // slice 4 paper ids at a time and use
    const all_paper_ids_arr = all_paper_ids.split(',');
    for (j=0; j<all_paper_ids_arr.length; j=j+4) {
        // get elements from array from j to j+4
        // perform API call there
        // for the last call, make sure that j+x to length(all_paper_ids) is only used for API call
        const paper_ids_arr = all_paper_ids_arr.slice(j, j+4);
        const paper_ids = paper_ids_arr.join(',');
        // below string is for testing purpose
        // paper_ids = "63cd10c4ca6733a8894d55cf1343636fa816cf7c,7bb907e754942b832bacf7889ba1d6bd72945ca0,8c108052266ef5d530c4adf19629e23a989c83ac,b71c245e093568d8c95aa889f968ce72b18e3d8b"
        var endpoint = "https://qzi4sdg7tilsfj4dnt2pmrnadm0xaedr.lambda-url.us-west-2.on.aws/?id=" + paper_ids;
        await fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                console.log(paper_ids_arr);

                // till now, if there have been errors in API response, it returns a dict, not an array
                // the below condition handles that
                if (data.success == false) {
                    // for failures, open local JSON which should be paper id -> figure url and populate using those
                    console.log("Figures not available for some paper IDs at url:"+endpoint);

                    for (i=0; i< paper_ids_arr.length; i++) {
                        figure_urls_json[paper_ids_arr[i]] = alternate_figure_url;
                    }
                }
                else {
                    data.forEach(item => {

                        // Get the figure URL from the JSON response
                        var figureUrl = item.main;
                        // there are cases where item.main is null, so that needs to be handled
                        if (figureUrl == null) {
                            return;
                        }
                        var api_paper_id_arr = figureUrl.split('/');
                        var api_paper_id = api_paper_id_arr[api_paper_id_arr.length-2];

                        // I'm using the S2 figure url and parsing that as the paper id; maybe this is not fully correct
                        // For one case, it gives me a paper id that is not in the original paper_ids sent to the API
                        // It does not work with paper id 481c25f4bf5daa01c6f39172d211e076533b388e and instead returns aa9972d02863a5da866d18244134105fb0f83651
                        let paper_id_exists = paper_ids_arr.includes(api_paper_id);
                        if (paper_id_exists) {

                            figure_urls_json[api_paper_id] = figureUrl;

                            // openImageThumbnail(figure, figureUrl);
                            // downloadImageThumbnail(figure, figureUrl);
                        }
                        else {
                            console.log("Unknown paper id in response "+api_paper_id);
                        }
                    });
                }
            })
            .catch(error => {
                console.error("Error fetching figure:", error);
            });
    }
    return reconcile_paper_json(figure_urls_json, papers_json_dict, cache_json_dict, alternate_figure_url)
}

function reconcile_paper_json(figure_urls_json, papers_json_dict, cache_json_dict, alternate_figure_url) {

    for (let key in figure_urls_json) {
        if (figure_urls_json[key] == alternate_figure_url) {
        	if (Object.keys(cache_json_dict).length === 0) {
        		papers_json_dict[key]["figure_url"] = alternate_figure_url;
        	}
        	else {
        		papers_json_dict[key]["figure_url"] = cache_json_dict[key]["figure_url"];
        	}
        }
        else {
            papers_json_dict[key]["figure_url"] = figure_urls_json[key];
        }
    }
    return papers_json_dict;
}

function get_shortest_str(arr) {
    if (arr == null || arr.length ==0)
      return "";
    
    return arr.reduce(function(a, b) { 
        return a.length <= b.length ? a : b
    });
}

function get_abbreviated_venue(v, v_detailed) {
    if(v_detailed == null)
        return "Preprint";
    return get_shortest_str(v_detailed.alternate_names) || v ;
}
  
function highlight_author_list(authors, highlighted_author) {
    return authors.map(x => x.name == highlighted_author? "<b>" + x.name + "</b>": x.name).join(', ');
}

function raw_author_list(authors) {
    return authors.map(x => x.name).join(', ');
}

function copyBib(bib, bib_id){
    console.log(`Copying ${bib} to ${bib_id}`);
    navigator.clipboard.writeText(bib);
    document.getElementById(bib_id).textContent = "Copied!";
}

function reportError(paper_id, author_id, paper_title) {
    alert("You will be redirected to an error reporting form.");
    base_url = 'https://nikett-paperlist-app-dazi7u.streamlit.app/'
    redirect_url = base_url + '?paper_id='+paper_id+'&author_id='+author_id+'&paper_title='+paper_title;
    location.href = redirect_url;
}

function parseAuthorMetadata(obj) {
    var data = {};

    data["author_name"] = obj.name;
    data["author_id"] = obj.authorId;
    data["paper_count"] = obj.paperCount;
    data["citation_count"] = obj.citationCount;
    data["h_index"] = obj.hIndex;

    return data;
}


function get_paper_ids(papersjson) {
    var paper_ids = [];
    for (const p of papersjson["json_paper_list"]) {
        paper_ids.push(p["paper_id"]);
    }
    return paper_ids;
}

function parsePaperList(obj, exclude_paper_ids) {
    const papers = obj.papers;
    const highlighted_author = obj.name;

    var paperList = [];

    for (const p of papers) {
      var paperData = {};
      if (exclude_paper_ids.includes(p.paperId) == false) {
          paperData["paper_title"] = p.title;
          paperData["paper_id"] = p.paperId;
          paperData["author_list"] = raw_author_list(p.authors);
          paperData["highlighted_author_list"] = highlight_author_list(p.authors, highlighted_author);
          paperData["num_citations"] = p.citationCount;
          paperData["venue"] = p.venue;
          paperData["publicationVenue"] = p.publicationVenue;
          paperData["abbreviated_venue"] = get_abbreviated_venue(p.venue, p.publicationVenue);
          paperData["year"] = p.year;
          paperData["bib"] = p.citationStyles.bibtex.replace("@None", "@article");
          if (p.isOpenAccess) {
            paperData["pdf_url"] = p.openAccessPdf.url;
          }
          else {
            paperData["pdf_url"] = p.url;
          }

          paperList.push(paperData);
        }
    }
    return paperList;
}

function paperListToJSON(obj, exclude_paper_ids) {

    var data = {};
    data["author_meta"] = parseAuthorMetadata(obj);
    data["json_paper_list"] = parsePaperList(obj, exclude_paper_ids);

    return data;
}

function deduplicateLabPapers(papers) {
    var dedupLabPapers = [];
    var paperIds = {};
    for (var i=0; i < papers.length; i++) {
        if (papers[i]["paper_id"] in paperIds) {
            continue;
        }
        else {
            paperIds[papers[i]["paper_id"]] = 1;
            dedupLabPapers.push(papers[i]);
        }
    }
    return dedupLabPapers;
}

function parseBatchPapers(obj, exclude_paper_ids) {
    var labAuthorsMeta = [];
    var labPapers = [];
    for (const authorData of obj) {
        authorMeta = parseAuthorMetadata(authorData);
        labAuthorsMeta.push(authorMeta);

        authorPapers = parsePaperList(authorData, exclude_paper_ids);
        labPapers.push.apply(labPapers, authorPapers);
    }
    var data = {};
    data["authors"] = labAuthorsMeta;
    dedupLabPapers = deduplicateLabPapers(labPapers);
    data["json_paper_list"] = dedupLabPapers;

    return data;
}

function createTableRow(p, report_mode, highlight) {
    paper_title = p["paper_title"]
    t = "";
    t += `<tr class="tableRow">`;

    t += "<td>"+p["paper_title"]+".<br>";
    if (highlight == true) {
        t += p["highlighted_author_list"] + "<br>";
    }
    else {
        t += p["author_list"] + "<br>";
    }
    ven = p["abbreviated_venue"];
    t += "<i>" + ven + " " + p["year"] + " </i><br>";
    t += ` <a href="${p["pdf_url"]}"><span class="tableBtn">[PDF]</span></a>`;
    bib = p["bib"];
    bib_id  = `bibtocopy${pnum}`;
    t += '<button id="' + bib_id + '" class="tableBtn" onclick="copyBib(`' + bib +'`, `' + bib_id + '`)">Cite</button>'
    if (report_mode == true) {
        paper_id = p["paper_id"];
        t += '<button id="' + paper_id + '" class="tableBtn" onclick="reportError(`' + paper_id +'`, `' + author_id + '`, `' + paper_title + '`)">Report</button>';
    }
    t += " <br><br></td>";
    t += "</tr>";
    return t;
}

function populateTable(author_data, report_mode, highlight) {
    const section = document.querySelector('papers_list');
  
    const tbl = document.createElement('table');
    var t = "" ; // table content.

    papers = author_data["json_paper_list"]
    
    pnum = 1;
    for (const p of papers) {
      tr_item = createTableRow(p, report_mode, highlight);
      t += tr_item;
      pnum += 1;
    }

    tbl.innerHTML = t;
    section.appendChild(tbl);
}

function createListItem(p, report_mode, highlight) {
    paper_title = p["paper_title"];
    highlighted_author_list = p["highlighted_author_list"];
    author_list = p["author_list"];
    pdf_url = p["pdf_url"];
    year = p["year"];
    the_abbreviated_venue = p["abbreviated_venue"];

    li = '';
    li += '<div class="s2-list__paper-shell">' // Start
    // li += '<a href="' + pdf_url + '/figure/0" class="s2-list__image-holder" target="_blank"><img src="https://picsum.photos/id/' + Math.floor(Math.random() * 640) + '/300/169" alt="First figure in '+ paper_title +'" class="s2-list__image" /></a>'; // Image, TODO: get image source, correct url, make sure alt text is correct & descriptive
    li += '<a href="' + pdf_url + '/figure/0" class="s2-list__image-holder" target="_blank">';
    li += '<img src="'+ p["figure_url"] + '" alt="First figure in '+ paper_title +'" class="s2-list__image" /></a>';

    li += '<div class="s2-list__paper-content"><h6 class="s2-list__title"><a href="' + pdf_url + '" class="s2-list__link" target="_blank">' + paper_title +'</a></h6>'; // Title
    li += '<p class="s2-list__meta-list"><span class="s2-list__meta s2-list__meta--authors">'; // Start Meta, Start Authors
    if (highlight == true) {
        li += highlighted_author_list;
    }
    else {
        li += author_list;
    }
    li += '</span>'; // End Authors
    li += '<span class="s2-list__meta s2-list__meta--venue">' + the_abbreviated_venue + '</span>, <span class="s2-list__meta s2-list__meta--year">' + year + '</span>' // Venue & Year
    li += '</p>'; // End Meta
    li += '<div class="s2-list__button-list">'; // Start Controls
    bib = p["bib"];
    bib_id  = `bibtocopy${pnum}`;
    li += '<button id="' + bib_id + '" class="s2-list__button s2-list__button--secondary" onclick="copyBib(`' + bib +'`, `' + bib_id + '`)">bibtex</button>'; //Cite Button
    if (report_mode == true) {
        paper_id = p["paper_id"];
        li += '<button id="' + paper_id + '" class="s2-list__button s2-list__button--secondary" onclick="reportError(`' + paper_id +'`, `' + author_id + '`, `' + paper_title + '`)">Report</button>';
    }
    li += '</div></div></div>'; // End Controls
    return li;
}

function populateList(author_data, report_mode, highlight) {
    const section = document.querySelector('papers_list');
  
    const ul = document.createElement('ul');
    var t = "" ; // list content.

    papers = author_data["json_paper_list"];
    ul.className = "s2-list";
    
    pnum = 1;
    for (const p of papers) {
      let item = document.createElement("li");
      li = createListItem(p, report_mode, highlight);
      item.innerHTML = li;
      item.className = "s2-list__paper";
      pnum += 1;
      ul.appendChild(item)
    }

    section.appendChild(ul);

    const copied_json_btn = document.createElement('button');
    copied_json_btn.innerHTML = "Download publications json";
    copied_json_btn.addEventListener("click", function(){
        // Convert JSON to string
        const data = JSON.stringify(author_data, null, 2);
        console.log("copying paper json to clipboard ... " + data); 
        // Create a Blob object
        const blob = new Blob([data], { type: 'application/json' });
        // Create an object URL
        const url = URL.createObjectURL(blob);
        // Download file
        download_as_file(url, 's2_list_my_papers.json');
        // Release the object URL
        URL.revokeObjectURL(url);
    });
    section.appendChild(copied_json_btn);
}
