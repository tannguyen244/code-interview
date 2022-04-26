
# # fetch image tag
# # secscan
# /api/v1/repository/{repository}/manifest/{manifestref}/security
# Using python3
# command test code python3 main.py --file image_list.json > abcd.txt
import argparse
import requests
import sys
import json
import os
from collections import defaultdict

def scan(tags):
    reports = []
    for tag in tags:
        repo = "{}/{}".format(tag["Organisation"], tag["Repository"])
        image_tag = tag["Tag"]
        reports.append(find_vulns(repo, image_tag))
    #print(reports)
    dump_result(reports)

def dump_result(reports):
    print(json.dumps(reports, indent = 4, sort_keys = True))

def fetch_image_by_tag(repo, tag):
    url = "https://quay.io/api/v1/repository/{}".format(repo)
    response = requests.get(url).json()
    found_tag = None
    for key, response_tag in response["tags"].items():
        if key == tag:
            found_tag = response_tag
    return found_tag

def secscan(repo, image_id):
    url = "https://quay.io/api/v1/repository/{}/manifest/{}/security?vulnerabilities=true".format(repo, image_id)
    response = requests.get(url)
    #print(response.json()["data"]["Layer"]["Features"])
    return response.json()["data"]["Layer"]["Features"]

def find_vulns(repo, tag):
    found_tag = fetch_image_by_tag(repo, tag)
    image_id = found_tag["manifest_digest"]
    pkgs = secscan(repo, image_id)
    sec_map = defaultdict(str)
    for pkg in pkgs:
        if "Vulnerabilities" not in pkg.keys():
            continue
        for vuln in pkg["Vulnerabilities"]:
            vuln['PackageName'] = pkg['Name']
            sec_map[vuln["Name"]] = vuln
    #print(sec_map)
    vulns = list(sec_map.values())
    #print(vulns)
    #vulns = dict(zip(Name, sec_map.values()))
    org, repo = repo.split("/")
    return {
        "Organisation": org,
        "Repository": repo,
        "Tag": found_tag["name"],
        "Manifest": found_tag["manifest_digest"],
        "Vulnerabilities": vulns
    }

#endpoint = os.getenv("QUAY_API_ENDPOINT", "https://quay.io/api/v1")
parser = argparse.ArgumentParser(
    description = "Find vulnerabilities for a given file or read from stdin. File must be in the correct format"
)
parser.add_argument("--file", help = "file containing the image tag to look up")
parser.add_argument("data", nargs="?", help = "json stream of lookup tags from stdin")


lookup_file = parser.parse_args().file
if lookup_file:
    with open(lookup_file, "r") as lookup_file:
        data = lookup_file.read()
        tags = json.loads(data)
        scan(tags)
else:
    tags = json.load(sys.stdin)
    scan(tags)