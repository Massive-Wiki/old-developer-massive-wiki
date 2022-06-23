#!/usr/bin/env python

import argparse
import glob
import json
import logging
import os
from pathlib import Path

# set up logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser


# (re)create an new javascript index file

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_wiki = str(args.wiki)
    logging.info("wiki folder %s: ", dir_wiki)

#    mdfiles = [f for f in glob.glob(f"{dir_wiki}/**/*.md", recursive=True)]
    mdfiles = ['/Users/band/documents/myWikis/conversations/URIs URLs and URNs.md', '/Users/band/documents/myWikis/conversations/Wikis and knowledge structures.md', '/Users/band/documents/myWikis/conversations/Sandbox.md']

    idx_data=[]
    for i, f in enumerate(mdfiles):
        idx_data.append({"id": i, "title": f, "body": Path(f).read_text()})

    logging.info("index length %s: ",len(idx_data))

    fname = f"{dir_wiki}/.massivewikibuilder/massive-wiki-themes/basso-thiswiki/mwb-static/scripts/wiki_index.js"
    with open(fname,"a") as file:
        file.write("\n")
        for datum in enumerate(idx_data):
            file.write(f"var doc{datum[1].get('id')} = {{{json.dumps(datum[1])}}}\nindex.addDoc(doc{datum[1].get('id')});\n")

if __name__ == "__main__":
    exit(main())
