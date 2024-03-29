#!/usr/bin/env python

import argparse
import os
import glob

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_wiki = str(args.wiki)
    print(dir_wiki)

    mdfiles = [f for f in glob.glob(f"{dir_wiki}/**/*.md", recursive=True)]
    Print("newest file: ", max(mdfiles, key=os.path.getctime))
    print("oldest file: ", min(mdfiles, key=os.path.getctime))

    for f in sorted(mdfiles,key=os.path.getmtime,reverse=True)[:5]:
        print(f)
    
if __name__ == "__main__":
    exit(main())
