# Installing lunr search capability

### 2022-07-06/07/10  including lunr search

Steps to incorporate lunr search from developer-massive-wiki to  another massive-wiki (running MWB v1.9.0):  
0. merge `README.md` (done manually)  
1. install node modules:  
    1.1. install node (e.g., macOS: `$ brew install node`) 
    1.2. copy package.json, package-lock.json  to `.massivewikibuilder`  
    1.3. `$ npm ci`  (this installs the node modules into folder `node_modules`)  
2. install build-index.js  in `.massivewikibuilder`  
3. in `this-wiki-themes/basso`: update `page.html`, `_navbar.html`, `search.html`  
5. merge `mwb.py` (done manually - a simple copy may do it)  
6. update `netlify.toml` (add `--lunr` to the mwb build line)  



