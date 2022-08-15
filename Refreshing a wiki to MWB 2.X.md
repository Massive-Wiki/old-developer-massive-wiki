# Refreshing a wiki to MWB 2.x

### Get a clean version for a new repo

This process re-instantiates the submodules, which is good for keeping MWB and MWT files out of the repo (there's a reference pointer to the repos, but the files themselves don't get added to the repo), and also good for local testing.

Assumption 0: shell commands are written for macOS and `zsh`  
Assumption 1: the existing wiki is named `wiki-vault-name` .  
Assumption 2: all commands in the scripts below are relative to the parent directory of this existing wiki.  
Assumption 3: the repo in GitHub belongs to `GH-UserID`, and isn't in a different organization (if it is, `gh` command needs to be changed)

``` shell
git clone git@github.com:Massive-Wiki/massive-wiki-starter.git temp-wiki-vault-name
cd temp-wiki-vault-name
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
gh repo create temp-wiki-vault-name --public --source=. --remote=upstream
git branch -M main

# use either HTTPS or SSH line
# git remote add origin https://github.com/GH-UserID/temp-wiki-vault-name.git
# git remote add origin git@github.com:GH-UserID/wiki-vault-name.git

git remote add origin https://github.com/GH-UserID/temp-wiki-vault-name.git
git push -u origin main
```

### Copy content over from previous version

Copy over all the MD files, ``.obsidian/`` , and `.massivewikibuilder/mwb.yaml`  (but don't overwrite `netlify.toml`)

Assumption 4: commands in the scripts below are relative to the parent directory of this existing wiki.

```Shell
cd wiki-vault-name # change directory into the old vault folder
cp -av * ../temp-wiki-vault-name # does not copy dotfiles/dotdirectories
rm ../temp-wiki-vault-name/.obsidian # ensure we don't copy _into_ .obsidian
cp -av .obsidian ../temp-wiki-vault-name # copy over .obsidian directory
cp .massivewikibuilder/mwb.yaml ../temp-wiki-vault-name/.massivewikibuilder/ # copy over mwb.yaml
cd ../temp-wiki-vault-name
git checkout netlify.toml # restore netlify.toml we just copied over

```

### Add the old wiki content to the new repository
```Shell
git add --all ':!netlify.toml'
git commit -m "old wiki content transfer"
git push
```


### set old repository name to old-wiki-vault-name on Github

In the GitHub interface, go to Settings in the repo, and rename.

_(need `gh` command if available)_

### set new repository name to old name on Github

In the GitHub interface, go to Settings in the repo, and rename.

_(need `gh` command if available)_

### Local Testing

Assumption 4: `python3` and `node` are installed and available

```Shell
cd temp-wiki-vault-name
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

### Locally, move old wiki out of the way, clone new wiki

```Shell
cd ~/Documents/GitHub/ # or wherever wikis are
mv wiki-vault-name old-wiki-vault-name

# use either HTTPS or SSH line
# git clone https://github.com/GH-UserID/wiki-vault-name.git
# git clone git@github.com:GH-UserID/wiki-vault-name.git

cd wiki-vault-name
rm -rf .obsidian
cp -a ../old-wiki-vault-name/.obsidian .
```

### Invite people with access to the old repo to the new repo

In the new repo on GitHub, go to Settings > Collaborators and teams.