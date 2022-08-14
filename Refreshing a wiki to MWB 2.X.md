# Refreshing a wiki to MWB 2.x

### Get a clean version for a new repo

This process re-instantiates the submodules, which is good for keeping MWB and MWT files out of the repo (there's a reference pointer to the repos, but the files themselves don't get added to the repo), and also good for local testing.

Assumption 0: shell commands are written for macOS and `zsh`  
Assumption 1: the existing wiki is named `wiki.vault.name` .  
Assumption 2: all commands in the scripts below are relative to the parent directory of this existing wiki.  

``` shell
git clone git@github.com:Massive-Wiki/massive-wiki-starter.git temp-wiki.vault.name
cd temp-wiki.vault.name
rm -rf .git
git init
cd .massivewikibuilder
more ../.gitmodules # get addresses for MWB and MWT
rmdir massivewikibuilder massive-wiki-themes
git submodule add https://github.com/peterkaminski/massivewikibuilder.git
git submodule add https://github.com/peterkaminski/massive-wiki-themes.git
cd ..
git add .
git commit -m "start with Massive Wiki Starter"
```

### Push this new repo to GitHub

```Shell
gh repo create temp-wiki.vault.name --public --source=. --remote=upstream
git branch -M main
git remote add origin https://github.com/GH-UserID/temp-wiki.vault.name.git
git push -u origin main
```


### Copy content over from previous version

- copy over all the MD files, ``.obsidian/`` , and `.massivewikibuilder/mwb.yaml`  (but don't overwrite `netlify.toml`)

Assumption 3: commands in the scripts below are relative to the parent directory of this existing wiki.

```Shell
cd wiki.vault.name # change directory into the old vault folder
cp -av * ../temp-wiki.vault.name # does not copy dotfiles/dotdirectories
cp -av .obsidian ../temp-wiki.vault.name # copy over .obsidian directory
cp .massivewikibuilder/mwb.yaml ../temp-wiki.vault.name/.massivewikibuilder/ # copy over mwb.yaml
cd ../temp-wiki.vault.name
git checkout netlify.toml # restore netlify.toml we just copied over

```

### Add the old wiki content to the new repository
```Shell
git add --all ':!netlify.toml'
git commit -m "old wiki content transfer"
git push
```

### set new repository name to old name on Github

### Local Testing

Assumption 4: `python3` and `node` are installed and available

```Shell
cd temp-wiki.vault.name
cd .massivewikibuilder/massivewikibuilder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm ci  # install the node_modules used by lunr search | ONLY NEEDED ONCE
# run mwb using command from netlify.toml
./mwb.py -c ../mwb.yaml -w ../.. -o ../output -t ../this-wiki-themes/basso --lunr
# if successful
cd ../output
python3 -m http.server # open browser to localhost:8000 to view mwb output
```

