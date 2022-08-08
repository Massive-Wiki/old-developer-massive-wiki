# Massive Wiki Roadmap

## Massive Wiki Projects

- [ ] update Developer Wiki to MWB 2.0, with new directory structure and search
- [x] create Massive Wiki roadmap
- [ ] create fractal/graph db of MW projects
- [x] try Pijul
- [x] try Syncthing
- [ ] improve Massive Wiki Builder
- [ ] move MWB and MWT central repos from github:peterkaminski to github:Massive-Wiki
	- [ ] fix all the links to the peterkaminski repos in READMEs and whatever else
- [ ] create [[Opal]]
- [ ] create [[Zirconia]]
	- [ ] kill or revive [Missive Weaver](https://github.com/peterkaminski/missive-weaver)
- [ ] create [[Pier2Pier]]
	- [ ] may be obviated by [[Obsidian Git]]'s source control view

## Improve Massive Wiki Builder

- [x] fuzzy linking
- [x] search (with e.g., Lunr)
- [ ] [Format incipient links differently #37](https://github.com/peterkaminski/massivewikibuilder/issues/37)
- [ ] merge index_wiki() and main processing loop #refactoring
- [ ] merge all calls to .render() into one call #refactoring
- [ ] separate home page template (generalize to _many_ page templates)
- [ ] recent changes / recent changes lite
	- [ ] simple recent changes: have an alpha sort and chrono sort for All Pages (use [jQuery tabs](https://jqueryui.com/tabs/) to toggle)
- [ ] more than one sidebar
- [ ] additional css/fixes for sidebar in Basso theme
- [ ] backlinks
- [ ] more cleanup of mwb_wikilinks_plus #refactoring
- [ ] decide whether we want a plugin system or not
- [ ] <https://github.com/peterkaminski/massivewikibuilder/issues>
- [ ] look at [Stork](https://stork-search.net/) for another search engine
- [x] rewrite or otherwise improve mdx_wikilinks_plus
- [x] sidebar
- [ ] evaluate other [[Python Markdown engines]], add to or replace current library if appropriate
