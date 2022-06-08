#!/usr/bin/env python

import argparse
import os
import re

from pathlib import Path

# set up logging
import logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='find recently changed files in wiki.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
#    print(f"args: {args}")
    
    dir_wiki = Path(args.wiki).resolve().as_posix()
    print(dir_wiki)
    logging.info("wiki directory: %s", dir_wiki)

    wikifiles = []
    
    for root,dirs,files in os.walk(dir_wiki):
        dirs[:]=[d for d in dirs if not d.startswith('.')]
        files=[f for f in files if not f.startswith('.')]
        readable_path = root[len(dir_wiki):]
        logging.debug("absolute wiki directory path: %s", f"{dir_wiki}{readable_path}")
        path = re.sub(r'([ _]+_)', '_', readable_path)
        for file in files:
            if file == 'netlify.toml' or file == 'YAML.md' or file == 'README.md':
                continue
            clean_name = re.sub(r'([ _]+_)', '_', file)
            wikipath = f"{dir_wiki}{path}/{clean_name}"
            logging.debug("filename: %s  | wikipath: %s: ", f"{file}", wikipath)
            if file.lower().endswith('.md') and os.path.exists(wikipath):
                wikifiles.append(wikipath)

    print(max(wikifiles, key=os.path.getctime))
    print(min(wikifiles, key=os.path.getctime))
    
if __name__ == "__main__":
    exit(main())
