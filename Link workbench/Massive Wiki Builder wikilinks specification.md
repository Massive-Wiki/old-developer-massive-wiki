# MWB wikilinks specification?

(question mark missing from filename because Netlify doesn't like `?` or `#` in deployed filenames.)

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

#### 2022-05-12
wikilink edge cases (from Pete)
```
-   [[wiki page]]
-   [[Wiki Page]]
-   [[wikI pagE]]
-   [[WikiPage]]
-   [[../wiki page]]
-   [[../../wiki page]]
-   [[../subdir/wiki page]]
-   [[/wiki page]]
-   [[/subdir/wiki page]]
-   [[/subdir/../subdir2/../wiki page]]
-   [[wiki page.md]]
-   [[wiki page.jpg]]
-   [[wiki page.jpeg]]
-   [[wiki page.bmp]]
-   [[wiki page/]]
-   [[wiki page.exe]]
-   [[wiki page.txt]]
-   [[Page: Wiki]]
-   [[Punctuation Is !@#$%^&*()_+-={}[]|\:";'<>,.?/~` Fun]]

```

build first tests for a small set of ordinary cases that
1. do not have identical wiki page basenames in links to different pages
2. can have "/" in the links
3. have case-sensitive basenames

```
-   [[wiki page1]]
-   [[../wiki page2]]
-   [[../../wiki page3]]
-   [[../subdir/wiki page4]]
-   [[/wiki page5]]
-   [[/subdir/wiki page6]]
-   [[/subdir/../subdir2/../wiki page7]]
-
```


#### 2022-05-22
- need to handle ".txt" files (also other media and document files) explicitly, perhaps the same way as image files; or
- perhaps build a way to create wikilinks for any file that is *not* a Markdown files with ".md" extension?

