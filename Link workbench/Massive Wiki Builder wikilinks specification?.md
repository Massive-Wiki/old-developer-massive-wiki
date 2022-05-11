# MWB wikilinks specification?

(Or something like a specification? use RFC template?)

/ outline the syntax //
/ do not assume scheme when encountering ':' (Obsidian does not allow ':' in file names, so such links cannot create wiki pages) //
/ generate full path links from root of the wiki //
/ do not change case on the text in the link //

```

for each line
  find wikilink string
  (e.g., with this re: wikilink_pattern="\[\[(.*?)\]\]")

search wikifiles dictionary
  if found replace string with wikilink full pathname


```
