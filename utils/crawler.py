import requests
import xml.etree.ElementTree as ET

def get_latest_arxiv_paper(category="cs.AI"):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"cat:{category}",
        "start": 0,
        "max_results": 10,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Failed to fetch data from arXiv.")
        return []

    # Parse XML
    root = ET.fromstring(response.text)
    entries = root.findall('{http://www.w3.org/2005/Atom}entry')
    if entries is None:
        print("No entry found.")
        return []
    
    data=[]
    for entry in entries: 
        data.append({
            "title" : entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
            "summary" : entry.find('{http://www.w3.org/2005/Atom}summary').text.strip(),
            "link" : entry.find('{http://www.w3.org/2005/Atom}id').text.strip(),
            "authors" : [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
        })

    return data
