#!/usr/bin/env python

import argparse
import glob
import json
import logging
import os
from pathlib import Path
import re

# set up logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def scrub_path(filepath):
    return re.sub(r'([ _?\#]+)', '_', filepath)


def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")
    
    dir_wiki = str(args.wiki)
    logging.info("wiki folder %s: ", dir_wiki)

    mdfiles = [f for f in glob.glob(f"{dir_wiki}/**/*.md", recursive=True)]

    idx_data=[]
    for i, f in enumerate(mdfiles):
#        idx_data.append({"id": i, "title": Path(f).relative_to(dir_wiki).with_suffix('').as_posix(), "body": Path(f).read_text()})
        idx_data.append({"id": i, "link": "/"+scrub_path(Path(f).relative_to(dir_wiki).with_suffix('.html').as_posix()), "title": Path(f).stem, "body": Path(f).read_text()})

    logging.info("index length %s: ",len(idx_data))

    # TODO: add wikilink to index: idx.append({"id": i, "link": scrub_path(Path(f).relative_to(dir_wiki).with_suffix('.html').as_posix()), "title": Path(f).stem, "body": Path(f).read_text()})

    idx_fpath= f"{dir_wiki}/.massivewikibuilder/massive-wiki-themes/basso-thiswiki/mwb-static/scripts"

    # TODO: (re)create a new javascript index file with every MWB build
    # shutil.os.chdir(idx_path)
    # shutil.copy('wiki_index.js, 'wiki_index_last.js')
    # shutil.os.remove('wiki_index.js')
    # shutil.copy('wiki_index_head.js', 'wiki_index.js')
    # shutil.so.chdir(dir_wiki)

    fname = f"{idx_fpath}/wiki_index.js"
    with open(fname,"a") as file:
        file.write("\n")
        for datum in enumerate(idx_data):
            file.write(f"var doc{datum[1].get('id')} = {datum[1]}\nindex.addDoc(doc{datum[1].get('id')});\n")

if __name__ == "__main__":
    exit(main())
