# Installing lunr search capability

### 2022-07-06/07 including lunr search

Steps to incorporate lunr search from developer-massive-wiki to  another massive-wiki (running MWB v1.9.0):  
0. merge README.md (done manually)  
1. install node modules  
    1.1. install node  
    1.2. copy package.json, package-lock.json (is lock file required?)  
	(needed to git add -f package.json to the repo)  
    1.3. `$ npm ci`  (this installs the node modules)  
2. verify package.json  
3. install build-index.js  
4. in this-wiki-themes/basso: update page.html, _navbar.html, search.html  
5. merge mwb.py (done manually - yikes!)  
6. update netlify.toml (add --lunr to the mwb build line)  


