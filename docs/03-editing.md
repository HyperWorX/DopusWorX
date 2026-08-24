# Editing

DopusWorX is more than a previewer. You can read a file, write in it, and format it without leaving the pane. This page covers the three view modes, the formatting toolbar, the code-editing toolbar, inserting images and tables, wikilinks and embeds, find and replace, saving, the smaller comforts like undo, the live word count and zoom, and the keyboard shortcuts.

## The three modes

A file opens in one of three modes, picked from the buttons at the left of the top toolbar. You choose which view markdown opens in, and whether DopusWorX remembers the view you last used for each file; see [Which view a file opens in](#which-view-a-file-opens-in) below.

| Mode | What it is for |
|---|---|
| **Reading** | A clean, rendered, read-only view. This is what the document looks like finished. Task checkboxes are still clickable here, and ticking one writes `[ ]` to `[x]` back to the source line - including checkboxes inside table cells and inside blockquotes. **Alt+double-click** any text to drop into Live with the cursor on that word; a plain double-click still just selects. |
| **Live** | An editor that looks like the rendered output as you type, the way Obsidian's Live Preview works. Click into a line and the raw markdown markers for that line appear so you can change them; click away and the line renders again. Clicking a word inside a rendered block, such as a table cell, a quote or a code line, puts the cursor on that exact word when the block opens for editing, not at the start of the block. Typographic ("curly") apostrophes render in Live exactly as they do in Reading - click into the word and the straight source character comes back under the caret for editing. Task checkboxes are live here too: clicking one toggles the `[ ]` / `[x]` in the source line, including checkboxes in table cells. |
| **Source** | A plain-text editor showing the raw markdown (or raw code) with syntax highlighting and nothing hidden. The power-user surface. |

Click **Reading**, **Live** or **Source** in the toolbar to switch between the modes. Not every file kind offers all three. Code and text files always open as an editable Source view; markdown gives you all three. Switching modes keeps your place: the view stays where you were, and your cursor position and any active selection survive the round trip, even through Reading. If you scroll around while in Reading, your new scroll position is what you come back to, and the cursor restores without jumping the view to it.

### Which view a file opens in

Two settings decide the mode a markdown file lands in. Both live in Settings, on the Markdown tab under Document.

- **Open markdown in** sets the default view: Reading (the default), Live or Source. A file opens in this view whenever its remembered view is not used.
- **Remember each file's view** decides whether a file reopens in the view you last used for it, and for how long: a duration from five minutes up to a year (4 hours is the default), Always so the last view sticks however long ago it was, or Off so every file opens in the default view. With a duration the last view comes back only if you reopen the file within that window, counted from the last time you opened it; once the window lapses the file falls back to the default view.

### Raw HTML and aligned blocks in Live

Live shows raw HTML blocks the way Reading does, rather than leaving them as visible tags. A self-contained block such as a `<details>` box, a `<mark>` or an `<img>` renders in place. Put the cursor on it and the raw source comes back so you can edit it; click away and it renders again. Wrapper tags on their own line, like a bare `<div>` or `</div>`, simply disappear.

Alignment carries across too. A block centred with a `<div align="center">`, a `<center>` element or a `text-align` style centres its content, including whole tables, in Live as well as Reading. Left, right and justify alignment work the same way. In Source mode the HTML stays exactly as you wrote it.

### The Source split preview

The Source button has a small pane icon on it. Click Source once to enter Source mode; click it again to toggle a **split preview**: the raw source on the left, the rendered document on the right, side by side. Click once more to drop back to a single pane. The split state is remembered per file for the session.

<div align="center"><img src="images/source-split.png" width="640" alt="The Source split: raw Markdown on the left, the rendered document on the right, with a draggable divider between them"></div>

While the split is open:

- **Drag the divider** between the two panes to resize them. The split holds between 15% and 85% so neither pane can be squeezed to nothing.
- **Linked scrolling** is on by default. Scroll either pane and the other follows in step (a ratio match, not line-for-line, since prose and monospace source do not line up exactly). The link button sits on the divider; the chain icon shows whether scrolling is linked.
- **Click the chain button to unlink.** The icon switches to a broken chain and the two panes scroll independently. Click it again to relink.

### Folding heading sections

In Live and Source you can fold a markdown heading's whole section down to the next heading of the same or a higher level, so you can collapse the parts you are not working on.

- **Source** marks a foldable line on the line itself, next to the code, the way Notepad++ does, rather than in a column of its own. The marker is three short rules with an arrow beside them, faint until you move the pointer onto the line and brighter still on the marker. Click it to fold or unfold; the arrow turns over as it goes. A folded marker stays visible whether you are pointing at it or not, since it is the only thing telling you the lines below are collapsed.
- **Live** has no gutter at all, so it folds from the heading itself. Hover an H1, H2 or H3 and a small accent chevron appears in the left margin beside it. Click the chevron to fold or unfold; it rotates to show the state and stays clickable while folded, so you can open the section back up. A folded section collapses to accent-coloured **...** dots after the heading - click the dots to unfold.

The Source marker sits at its line's indent, so it steps in with the code rather than lining up in one column. Where it lands on the indentation it hides the whitespace dots underneath it, and the rest of that line's indentation fades back as the marker comes up, so the two never fight for the same space.

Folding is a view convenience only. It never changes the document.

## The formatting toolbar

The formatting toolbar runs along the bottom of the pane in Live and Source mode for markdown files. Each button either wraps your selection in markdown or adds a prefix to the lines you have selected. With nothing selected, the wrapping buttons drop the markers in and park the cursor between them so you can start typing.

You can rearrange the toolbar to suit you: **Edit toolbar layout** in Settings, on the General tab under Toolbars, lets you drag buttons sideways to reorder them, click one to hide or show it, and Reset to put the default set back.

<div align="center"><img src="images/editing-toolbar.png" width="640" alt="The formatting toolbar: bold, italic, strikethrough, highlight, inline code, link, footnote and clear-formatting, then the heading and maths buttons, the list buttons, indent, blockquote, code block, and image and table insert"></div>

### Inline formatting

| Button | Produces | Notes |
|---|---|---|
| **Bold** | `**text**` | |
| **Italic** | `*text*` | |
| **Strikethrough** | `~~text~~` | |
| **Highlight** | `==text==` | |
| **Inline code** | `` `text` `` | |
| **Link** | `[text](url)` | Asks for the URL. If your selection already looks like a link it is used as the label; otherwise `link text` is dropped in and selected for you. |
| **Footnote** | `[^N]` at the cursor, plus a matching `[^N]: ` definition at the end of the document | `N` is the lowest free number, so deleting a footnote frees its number for reuse. The cursor lands in the new definition so you can type the note straight in. See [Footnotes](#footnotes) below for editing them. |
| **Clear formatting** | strips everything back to plain text | Works on the selection, or the current line if nothing is selected. It removes line prefixes (heading `#`, blockquote `>`, list and task markers, indentation, stacked or nested), inline markers (`**`, `*`, `~~`, `==`, `` ` ``), link and image syntax (keeping the visible text), and any stray inline HTML pasted from another app. Single underscores are left alone so `snake_case` survives. One undo reverses it. |

The common inline wraps also have keyboard shortcuts in markdown Live and Source: **Ctrl+B** bold, **Ctrl+I** italic, **Ctrl+Shift+C** inline code and **Ctrl+Shift+X** strikethrough. They do exactly what the matching buttons do.

### Headings and maths

| Button | What it does |
|---|---|
| **Heading (H)** | Cycles the heading level of the current line. The number on the button shows what the next click will apply. A plain line becomes H1; an existing heading steps up one level, wrapping H6 back to H1. Moving the cursor to another line re-reads that line's level. The button always sets a level rather than removing it; to drop a heading, delete the `#` or undo. |
| **Sigma (Σ)** | Opens the maths symbol panel. The button is present whenever maths rendering is on, which it is by default, and disappears only if you turn maths off in settings. See the maths page for what the panel does. |

### Lists

| Button | Produces |
|---|---|
| **Bulleted list** | `- ` on each selected line (click again to remove) |
| **Numbered list** | `1. `, `2. `, `3. ` down the selected lines, renumbered in sequence (click again to remove) |
| **Task list** | `- [ ] ` on each selected line, preserving any indent so it works inside nested lists (click again to remove) |

**Tab** indents the current line and **Shift+Tab** outdents it, two spaces at a time. This works on any line in the editor, not just list lines - the same two-space step as the indent buttons below.

The vertical gap between list items is adjustable: **List item spacing** in
Settings, under Body text, one value that Reading and Live follow identically.

### Indent

| Button | What it does |
|---|---|
| **Increase indent** | adds two spaces to the front of each selected line |
| **Decrease indent (outdent)** | removes up to two leading spaces from each selected line |

### Blocks

| Button | Produces |
|---|---|
| **Blockquote** | `> ` on each selected line (click again to remove) |
| **Fenced code block** | a ```` ``` ```` fence around the selection, or an empty fence with the cursor on the body line. The fence always starts and ends on its own line so it parses cleanly. |
| **Insert image** | opens the image popup (below) |
| **Insert table** | opens the table size grid (below) |

A `---` on its own line renders as a horizontal rule divider. Its appearance - solid, gradient fade, centre fade, dotted, dashed, double line, or three centred diamonds - is controlled by the **Horizontal rule style** setting in Settings > Appearance > Lines, along with separate colour and thickness controls. See [07-palettes.md](07-palettes.md) for the full Appearance tab.

## The code-editing toolbar

When you open a code or text file in Source mode, the formatting toolbar is replaced by a code-editing toolbar. These commands are language-agnostic and run CodeMirror's own editing commands, so they behave exactly like the editor itself.

<div align="center"><img src="images/code-toolbar.png" width="280" alt="The code-editing toolbar: toggle comment, outdent, indent, duplicate line, move line up, move line down, find, and the whitespace and indentation guide toggles"></div>

| Button | What it does |
|---|---|
| **Toggle comment (`//`)** | comments or uncomments the current line or selection, using the comment syntax of the file's language. A no-op on languages with no comment token. |
| **Outdent** / **Indent** | decrease or increase the indent of the selected lines |
| **Duplicate line** | copies the current line below itself |
| **Move line up** / **Move line down** | shifts the current line past its neighbour |
| **Find** | opens the editor's search panel |

After a separator sit two view toggles. They change how the source is displayed rather than editing it, and each one remembers your choice.

| Toggle | What it does |
|---|---|
| **Show whitespace marks** | the faint dots on spaces and arrows on tabs |
| **Show indent guides** | the vertical lines running down each level of indentation |

The comment toggle knows the comment syntax of every language DopusWorX highlights, including the forty-odd whose grammars never declared one themselves, so JSON, INI and VBScript comment properly instead of doing nothing at all. Where a format genuinely has no comment form, plain text, logs, CSV and diffs among them, the button does nothing rather than stamping a stray `<!-- -->` into the file, which is what it used to do.

The two view toggles are on this bar only. Markdown Source keeps the formatting toolbar, so for a markdown file set whitespace marks and indentation guides from Settings instead.

### Wrapping long lines

The wrap button lives in the **top** toolbar, beside Find, because it means something for every file rather than only for source.

- On a **markdown** file it wraps the rendered code blocks and inline code, in Reading and in Live. Your prose is unaffected either way, since prose wraps regardless.
- On a **code or text** file it wraps the Source editor and the read-only view.

With it off, a long line stays on one line and its block scrolls sideways instead, which is what you want when the alignment of the code matters more than seeing all of it at once.

## Inserting an image

The image button (in the formatting toolbar) opens a small popup so you can place an image without hand-writing the markdown.

<div align="center"><img src="images/image-insert.png" width="460" alt="The Insert image popup: Source with a Browse button, Alt text, Width and Height, an Alignment row, and a Storage choice of Embed a copy or Link in place"></div>

- **Source** can be a local file path or an `http(s)` URL. Type or paste it, or click **Browse** to pick a file from disk.
- **Alt text** is the description used by screen readers. Optional.
- **Width** and **Height** are optional pixel values. Leave either blank for automatic sizing; you can set just one.
- **Alignment** is None, Left, Center or Right. None inserts plain markdown with no wrapper.
- **Storage** is the choice that decides whether the image travels with your document. It has two options, and a line under it explains what the current choice will do:
  - **Embed a copy** (the default) brings the image in beside the document and links it by a relative path, so it stays self-contained. For a local file this copies it; for a URL it downloads it. This is the safe choice: a copied-in image always shows, including after you close and reopen the file.
  - **Link in place** points the document at the file where it already sits, without copying. This is an external reference, the same kind of thing as a web URL or a hand-written `<img>` tag: it does not travel with the document, and it only resolves while the original file stays put. Use it when you would rather not duplicate a shared image library.

  For a web URL, Link in place keeps the URL and needs **Allow remote images** turned on in settings; with that off, Link is disabled and the choice is forced to Embed (downloaded), because an unresolved external URL would just show as a placeholder.

Insert is enabled as soon as the Source field has text. The popup writes Obsidian-style image markdown, for example `![alt|400x300|center](path)`, which renders at the right size and alignment both here and in Obsidian. Click outside the popup, or its close control, to close it.

You can write the same syntax by hand anywhere: `![alt|420](path)` sets a width, `![alt|420x300](path)` width and height, `![alt|x300](path)` a height alone, and a trailing `|left`, `|center` or `|right` aligns the image. The Obsidian embed form takes the same sizes: `![[img.png|420]]` (see [Wikilinks and embeds](#wikilinks-and-embeds)).

### How local images are found

When a document references a local image, DopusWorX looks for it in this order:

1. **Beside the document**, by the relative path written in the markdown. This is where Embed a copy puts things, and it is the most portable: move the document and its folder together and the images come along.
2. **In your image search folders**, if it was not found beside the document. The **Also look for images in** setting (Settings, default `attachments`) names extra folders to check, separated by `;`. Each entry is relative to the document folder, such as `attachments` or `../assets`, and absolute paths such as `D:\vault\attachments` work too. Each folder is tried with the image's full relative path first, then with its bare filename, which is how Obsidian resolves its uniquely-named pasted images.
3. **At its absolute path**, for an image linked in place (or any document that already stores a `C:\...` path). These keep working across restarts: opening a document re-establishes which outside folders its own images live in, so a linked image does not go blank after you reopen the file or restart Directory Opus.

For safety, the viewer only ever serves images from folders your open document points at or that you pick yourself, and it never serves from the Windows system folder. A document cannot make it read files it does not reference.

## Inserting a table

The table button (in the formatting toolbar) opens a small popup. Move the pointer over the grid to pick a size, up to 10 columns by 10 rows, with the current choice shown as "N × M". The **Rows** stepper accepts 1-100 and the **Columns** stepper accepts 1-30, so you can build tables much larger than the grid. The **Position** control (Left / Centre / Right) sets where the table sits on the page; Centre and Right write a `dwx-table` directive above the table (see [Table options](#table-options) below). The **Headers** section has two toggles: **Row** is on by default and renders the first row as a shaded header - uncheck it to render that row as a plain data row instead; **Column** shades the first column like a row-label header. Both use the same `dwx-table` directive as Position. Click to drop a markdown table at the cursor: the cursor lands in the first cell ready to fill in. Click outside the popup, or press Escape, to close it without inserting.

<div align="center"><img src="images/table-insert.png" width="460" alt="The Insert table popup: a hover size grid on the left (a 3 by 3 selection lit), with Rows and Columns steppers, a Position control and Header row / column toggles on the right"></div>

### Images in table cells

You can put a sized, aligned image in a table cell. Two ways, and you can mix them
in one table:

- **Obsidian pipe syntax**, the same one [Inserting an image](#inserting-an-image)
  writes: `![alt|72](path)` for width, `![alt|72x48](path)` for width and height,
  and add an alignment to centre it in the cell, `![alt|72|center](path)`. Use the
  plain pipe; you do **not** need to escape it inside the cell.
- **HTML**, `<img src="path" width="72">`, which is handy if you prefer to set the
  height too or already have HTML to hand.

A column can also be centred the normal markdown way, with a `:---:` separator, so
its cells (image or text) centre as a column.

How it works: a bare `|` is normally the cell separator, so the viewer recognises
the `![ ... ]( ... )` image span and treats the pipes inside it as part of the
image, not as new columns. Your source file keeps the plain pipe exactly as you
typed it; the handling is only for rendering.

What breaks it: the image has to be a single, well-formed `![alt](path)` span on
the line. A stray `]` or `)` inside the alt text or the path, an unclosed bracket,
or a real line break in the middle will end the span early and the rest spills into
the next column. If a cell ever splits oddly, fall back to the HTML `<img>` form,
which has no pipes to confuse the table.

### Table options

A comment on the line directly above a table gives it options markdown cannot
express:

```
<!-- dwx-table: center, header-col -->
| Name | Value |
|---|---|
| one  | 1 |
```

The flags, in any combination separated by commas:

| Flag | Effect |
|---|---|
| `center` | centres the table on the page |
| `right` | pushes the table to the right edge |
| `header-col` | shades the first column like a header, for tables whose rows are labelled down the side |
| `no-header` | renders the header row as a plain data row, for tables that have no titles |

The directive works in Reading and Live alike, and the comment itself renders to
nothing. Other markdown apps simply show a normal table, so a file that uses it
stays portable.

Wrapping a table in an alignment container does the same job for position: a
table inside `<div align="center">` (or `<center>`) centres the table itself, not
just the text in its cells, exactly as the `center` flag does, and a right-aligned
wrapper matches `right`. This is what the right-click Alignment menu writes when
you use it on a table (see [06-context-menus.md](06-context-menus.md)).

## Table of contents

Right-click an editable markdown document and choose Insert &rsaquo; Table of Contents to drop a contents list at the top, under a leading H1 title if the document has one, otherwise below any frontmatter. Choose it again to refresh the list.

The block sits between a hidden `<!-- toc -->` marker and its `<!-- /toc -->` closing marker and keeps itself in step: add, remove, rename or reorder a heading and the list updates on its own, so it never drifts from the document. Each entry links to its heading.

Two settings on the Markdown tab, under Table of contents, set the look, and both update an existing TOC in place:

- **List style**: Numbered (1. 2. 3.) or Bulleted.
- **Title style**: No title, Classic (bold with a rule), Styled (small caps with a top rule), Accented (an accent bar) or Coloured (an accent banner).

Only real document headings appear in the list. A heading written inside a blockquote (`> ## Heading`), a table cell, or a fenced code block is not counted as document structure and stays out of the contents.

The list covers the whole file however long it is. A document too big to read through on the spot is finished in the background and the contents written once it covers the document, so a long file no longer gets the first handful of headings and nothing after them. In the rare case it still cannot finish, the block says the list is partial rather than looking complete.

## Frontmatter and the banner image

A markdown file can open with a YAML frontmatter block: a `---` fence, some `key: value` lines, then a closing `---`, before any content. DopusWorX recognises it and keeps it out of the rendered document, rather than showing the `---` as a horizontal rule and the keys as stray text.

- **Reading** hides the block.
- **Live** shows the block as faint, dimmed YAML you can click into and edit directly - unless the file has a `banner:` key, in which case the banner image stands in for the block until you click it (see below).
- **Source** shows the frontmatter as written.

One key is special: **`banner:`** takes an image path or URL and renders that image as a banner strip across the top of the document, above the first heading, in Reading and Live. It resolves local paths the same way inline images do (see [How local images are found](#how-local-images-are-found)).

The banner shows in Live from the moment the file opens; it stays up until you click it, when the raw frontmatter comes back so you can edit the `banner:` line. Move the cursor out of the frontmatter and the banner renders again. Its left and right edges fade evenly into the page so it melts into the document.

Set its height with **Banner height** in Settings, on the Markdown tab under Images. Leave it empty for the default, which scales with the pane width. Two further keys control geometry per file: `banner_y: N` (an integer from 0 to 100, where 0 anchors the crop to the top of the image and 100 to the bottom; bare integers and the `%` suffix both work) and `banner_height: Npx` (a pixel value from 24 to 2000 that overrides the global Settings height for this document only). Omit either key to get the defaults.

### Set banner image

You do not have to find a picture by hand. Right-click a markdown document and choose **Set banner image** to open a search box: type what you want, press Enter, and click a result to open a position preview: the image appears as a banner strip. Drag it up or down to choose the vertical crop, then click **Set banner** to write the frontmatter. Nothing is written until you click Set. If the document already has a banner, reopening the picker seeds the preview from its current position so you can adjust the crop without re-searching.

<div align="center"><img src="images/banner-picker.png" width="460" alt="The banner image picker showing a search result selected and the position preview strip, with the drag-to-reposition hint and per-file height field below it"></div>

By default it searches [Wikimedia Commons](https://commons.wikimedia.org), the largest free image library, so it works with no setup. If Commons is unreachable it falls back to [Openverse](https://openverse.org) automatically. [Openverse](https://openverse.org) is always available on its own tab and needs no key; a free Openverse API key in Settings only lifts its anonymous rate limit. To add Unsplash as well, paste your own free Unsplash Access Key into **Unsplash access key** in Settings, on the Markdown tab under Images (register a free application at unsplash.com/developers).

The picker shows a row of tabs above the results: Commons and Openverse always, plus Unsplash when its key is set. Click a tab to search that source; the search box keeps its text so you can compare the same word across sources. It opens on Unsplash when you have an Unsplash key, otherwise Commons. Repeated searches are remembered, so trying the same word again, or switching back to a source you already searched, is instant and does not count against any limit.

If the first page of results is not quite what you want, click **More results** to load the next page (20 results per page). The button hides itself once the provider is exhausted.

The preview also shows a **This file's banner height** field. Type a pixel value (24-2000) to override the global Settings height for this file only; leave it blank to use the global setting. Set writes it as `banner_height: Npx` frontmatter. Clearing the field and clicking Set removes the override, restoring the global height.

The picked image is a web URL, so it needs a connection to load the first time; if a search comes back empty, wait a moment and try again.

## Wikilinks and embeds

DopusWorX reads Obsidian's double-bracket references:

- **`[[note]]`** is a wikilink. `[[note|shown text]]` changes the display text, and `[[#Heading]]` links to a heading in the same document - click it to scroll there. A link into another document renders as a styled reference but is not followed.
- **`![[note]]`** embeds (transcludes) another note's content into the document in Reading mode, and `![[note#Section]]` embeds just that section. An embed that cannot be resolved says why in place - a file that cannot be read, a section not found, or a circular embed - rather than breaking the page.
- **`![[image.png]]`** embeds an image. Add a size after a pipe: `![[image.png|240]]` for a width, `![[image.png|240x180]]` for width and height.

In Live mode wikilinks render as styled references and note embeds show as compact chips; put the cursor on one and the raw source comes back for editing.

## Footnotes

Footnotes attach a note or citation to a point in the text. The **Footnote** button on the formatting toolbar adds both halves at once: a `[^N]` marker where the cursor is, and a matching `[^N]: ` definition at the end of the document. The number is the lowest free one, so if you delete a footnote its number comes free again and the next one you add reuses it instead of always climbing.

You edit a footnote in its real place in the document, the same way Live mode handles every other block. There is no separate pop-up box, so what you type is the markdown and Reading, Live and Source always agree.

- **In Live mode** the definitions sit at the bottom as a tidy footnotes section. Click a footnote (or arrow into it) and its raw source opens for editing; click away and it renders again. After inserting, the cursor is already in the new definition so you can type straight away.
- **Multi-line footnotes**: press Enter inside a footnote to continue it on a new line, indented so it stays part of the same note. Press Enter on a blank line to finish the footnote.
- **An empty footnote** shows a "click to add text" placeholder, so you can always reopen one you left blank and fill it in later.
- **To remove a footnote**, use the small delete control on it. That removes the definition and every `[^N]` reference to it in one go.
- **Jumping around**: click a footnote number in the text to go to its note, and the return arrow on the note to go back to the reference. Both centre the target in the view rather than pinning it to the top.
- **In Reading mode** footnotes render at the bottom with the same numbered links and return arrows, and those links work too.

In Source mode you write footnotes by hand as plain markdown: a `[^id]` marker in the text and a `[^id]: text` definition at the end, with any continuation lines indented four spaces. The id can be a number or a word like `[^note]`; either way it shows as a number in Reading and Live.

## Find and replace

The magnifier button on the top toolbar, or **Ctrl+F**, opens the find and replace panel. Find works in every mode: in Live and Source it searches the editor, and in Reading it searches the rendered page, with the count showing your position ("2 / 5"). Replace needs an editor, so the Replace row is available in Live and Source only. (In code Source mode, the code toolbar's Find button opens the editor's own search instead.)

<div align="center"><img src="images/find-replace-panel.png" width="478" alt="The find and replace panel: Find and Replace fields, a live match count, the case, whole-word and regex toggles, and the previous/next arrows"></div>

- Type in the **Find** field. The match count shows beside it live ("3 matches", "no matches", or "bad regex" if a regular expression will not compile). If you had a single line selected when you opened the panel, it seeds the Find field for you.
- **Enter** jumps to the next match and **Shift+Enter** to the previous, the same as the **‹** and **›** arrows. Each match is scrolled to the centre of the view so it is always in sight.
- Three toggles change how Find matches:
  - **Aa** - match case
  - **\b** - match whole word
  - **.\*** - treat the Find text as a regular expression
- The panel opens as find-only. The **⇅** toggle reveals the Replace row when you want it, so Enter always means "next match" and can never replace something by accident. (Opening the panel from the right-click menu's Find / Replace item reveals the row straight away.)
- With Replace open, **Replace** changes the current match; **All** replaces every match at once. Enter in the Replace field also replaces the current match. The count updates after each replace.

Click the close control (or press Esc) to dismiss the panel; the match highlights clear with it. On a narrow pane the panel's controls wrap onto a second line so it always fits.

## Spell check

Turn on **Spell check while editing** in Settings, on the General tab under Open & save (with the dictionary picker just below it), and misspelled words get a wavy red underline in the Live and Source editors of markdown documents. Reading mode is left clean. Code, inline code, links and URLs are skipped, so a filename or a URL is never flagged, and so are all-capitals words and camelCase identifiers.

Right-click an underlined word for a short list of suggestions at the top of the menu; click one to replace the word.

### Dictionaries

The **Dictionaries** picker (next to the spell-check toggle) chooses which languages to check against. English (US) is built in and works offline straight away. Open the dropdown to add more: English (UK), Australian and Canadian English, the German family including Austrian, Swiss and Low German (with compound words handled properly), and the major European languages plus Greek, Turkish, Hebrew, Korean and others - over fifty in all.

Each added dictionary downloads once, a few hundred kilobytes, and is then cached so it works offline from then on. A pill shows "downloading" while it fetches and turns into a plain chip when it is ready. Add as many as you like and they are all used together, so a note that mixes languages is checked against every one - a word is treated as correct if any of your dictionaries knows it. Remove one with the × on its chip.

## Go to line

Press **Ctrl+G** in any editor surface - markdown Live or Source, and code files in Source - to open the Go to line popup. It opens seeded with the current line; type a line number (within the document's length) and press Enter, or click Go, to jump to that line and centre it. The right-click menu also offers Go to line, in Source view only, where lines are the visible unit; Live renders blocks, so a line number means nothing there and the menu leaves it out. (In the [binary inspector](09-binary-inspector.md), Ctrl+G jumps to a byte offset instead.)

## Saving

The save button is the split control near the left of the top toolbar: the main half saves, the caret beside it opens the rest of the save options.

- **Save** (the main button) writes your changes back to the file. It does nothing if there is nothing to save.
- **Save As** (from the Save menu) writes to a new file and switches the pane to it. It works even with no unsaved changes, so you can duplicate a file under a new name.
- **Save a Copy** writes the current content to a path you pick without changing the file you are editing. It is an export: the pane stays on the original, the dirty marker is untouched.

The same menu also holds export options: **Export as HTML** for markdown, **Export as Plain text** for code, and **Print** for any file, which holds both sheets.

### Printing

Print and Save as PDF put the document on the page on its own, with no floating card, so the text
runs the full printable width and the page margin is the only inset.

There is nothing to set up. It prints in the palette you are reading, page colour and all, sitting
inside the page margin the way it sits in the viewer. A document read in a dark theme prints on that
dark page, with its headings, links and code the colours they are on screen.

Nothing else on the sheet is drawn with a background fill. The page colour is the only one: a
horizontal rule is a rule, a table is its grid, a code block sits inside a thin border, highlighted
text is underlined in the highlight colour, and a ticked task box has a tick drawn in it. Headings
stay headings by size and weight as well as colour, and syntax highlighting carries in bold and
italics alongside the hue. That is deliberate, and it is what makes the next paragraph work.

**There is a second sheet for plain paper: Black and white.** Print is one entry in both the Save
menu and the right-click menu, and the two sheets sit under it: click Print for the normal one, or
hover it and pick **Black and white** to print the document black on white with none of the palette
in it. Everything keeps its meaning: the rules, borders, ticks and underlines are all
still drawn, and a code listing carries its highlighting in weight and slope. Nothing is remembered
between prints, so the two commands can be used in any order and each one gives you its own sheet
every time.

That is a command rather than a tick box because the print dialog's own Black and white setting
cannot reach it. That setting greys out the finished page after we have handed it over, so on a dark
theme it gives you a grey sheet with pale text rather than a clean one. Use it if you want a
greyscale of what you see; use Black and white under Print if you want plain paper.

One kind is deliberately not printed in the palette: a rendered HTML file. That is somebody else's
document with its own styling, shown in a frame the palette never touches, and its colours were
chosen against the background its author set. It prints as it always has, dark on a plain white
sheet. An HTML file's Source is our own listing like any other, so that one does take the palette.

Every kind of file prints the whole of itself, not the part that happened to be on screen. A code or
text file prints its full syntax-highlighted source from either view. An HTML file prints the
rendered page from View and its markup from Source. A CSV prints the entire table, carrying whatever
filter and sort you have applied, with the column headings repeated at the top of each sheet, and
prints the raw text instead if you are in Source. A binary file prints a real hex dump; that one is
capped, and the sheet says so.

Printing never changes what is on screen. You can print from any view and come back to it as it was.

Three things in the print dialog itself are worth knowing, because they are the dialog's and not
ours:

- **Margins.** DopusWorX asks for a 12mm top and bottom and 10mm sides, with the coloured page
  carrying its own inset inside that. The paper margin only applies on *Default*; pick anything else
  and the dialog uses its own inset instead. *None* runs the coloured page to the edge of the paper.
- **Background graphics.** Off by default, and it decides whether background fills print. It makes no
  difference here. The page colour is asked for in a way that prints either way, and nothing else on
  the sheet is a fill at all, so ticking it adds nothing and leaving it off takes nothing away. It is
  listed because it is the setting people reach for when a printed page comes out missing something,
  and with DopusWorX it is not the one.
- **Headers and footers.** The date and URL some printers add along the top and bottom. Untick it
  for a clean sheet.

Your original file's encoding and line endings are preserved on save. A file with mixed line endings keeps them line by line; a uniform file keeps its convention.

### Auto-save

Auto-save is off by default and set in minutes in settings. When on, it saves on that interval but only if there are unsaved changes, and it never truncates a file to empty (only a deliberate manual save of an empty document can do that).

### Refresh (reload from disk)

Ctrl+R or F5 reloads the file from disk, in any mode, not just Reading. If you have unsaved edits it asks before discarding them, so a refresh never quietly throws away your work. This is the way to pick up a change another program made to the file while you had the viewer open. (HTML files also get a refresh button on the top toolbar, for reloading the rendered View; other kinds use the keys.)

### If the file changes underneath you

<div align="center"><img src="images/conflict-banner.png" width="640" alt="The frosted conflict banner overlaying the document, showing the 'Edits here and a change outside' message with Keep my edits and Discard and reload buttons"></div>

Your unsaved work is never silently dropped.

Switch away from a file you were editing and back again and the edits are simply there, with the bullet in the title and Save ready. Same after a restart or a crash: unsaved work is kept and comes back the next time you open the file. Nothing outside the viewer touched the file while you were away, so there are not two versions to choose between and you are not asked about it. The status bar says the edits were restored, and Ctrl+R still takes you to the disk version if that is what you want.

The banner is for when two versions really are in play. It appears and stays until you choose. The message and buttons fit the case:

- **Unsaved edits in another window.** If another DopusWorX window holds unsaved edits for the same file, the banner says so and offers **Use those edits here** (adopt them and carry on), **Save a copy & reload** (writes your edits to a timestamped copy beside the file, then loads the disk version) or **View disk version**. Viewing the disk version never touches the other window's edits; they stay safe in that window.
- **Edits here and a change outside.** If you have unsaved edits and the file also changed on disk or in another window, **Keep my edits** keeps your version and makes your next save win; **Discard and reload** takes the disk version.
- **A save lost the race.** If a save finds the disk copy changed first, **Keep my edits** saves your version over it; **Discard and reload** takes the disk version.
- **No local edits, new content elsewhere.** If your copy is clean and the file changed on disk or was saved by another window, the banner asks whether to **Reload** or **Keep current view**.

This prompt is controlled by **Ask before reloading** in Settings, on the General tab under Open & save (on by default). Turn it off and a clean file reloads straight away with a brief notice instead of a banner - useful for logs or generated files that update on their own. Unsaved edits plus a change outside always prompt regardless of this setting.

Every Keep or Discard shows a brief toast with an **Undo** button that brings the banner back so you can choose again.

If you would rather not have unsaved edits come back at all, turn on **Reload external changes** in Settings, on the General tab under Open & save: the disk version is then always used. Save before you close - with this on, unsaved edits from a previous session are gone.

## Smaller comforts

### Undo and redo

The undo and redo buttons on the top toolbar step through your edit history. **Hold** either button for about half a second to open a list of recent states. Each entry leads with what the step did and a quoted snippet of the text it touched - Cut "Some words…", Paste "the new paragraph…" - plus how much the document grew or shrank (+120, −45) and how long ago. Click an entry to jump straight back to that state instead of stepping one edit at a time. The list keeps up to 40 recent states per file.

<div align="center"><img src="images/undo-history.png" width="460" alt="Holding the undo button opens a history of checkpoints, each named with its action, a quoted snippet, a size delta and an age"></div>

### Live word count

A small pill under the top toolbar shows the document's word, character and line counts as you type. Select text and it switches to the selection's character and word count, with the full document figures in the tooltip. Turn **Document stats** off in Settings, on the General tab under Toolbars, to hide it.

### Auto-hiding toolbars

Each toolbar can either stay put or slide out of the way. The pushpin on the corner of a toolbar toggles it: pinned means always visible, unpinned means auto-hide. When a bar is hidden, move the pointer to the edge where it lives and it slides back in. The choice is saved and applies to every open pane. The same pair of choices lives in Settings, on the General tab under Toolbars, as **Top toolbar display** and **Edit toolbar display**.

### Toolbar colours

The **Toolbars** section of the General tab recolours both toolbar pills: background, text and icons, border, and the resting opacity (they always sharpen to fully opaque under the pointer). Leave a field empty to keep the active palette's own toolbar chrome. Whatever background you pick, the selected mode tab and hover feedback adjust automatically to stay readable - on a bright bar the active tab becomes a dark pill with the bar's colour for its label, and the reverse on a dark bar. A **Reset all** link under the four fields clears them back to the palette defaults in one click.

### Zoom

Hold **Ctrl and scroll the mouse wheel** to zoom the document in or out, from 50% to 300%. A small pill shows the level as you go. Each mode keeps its own zoom, and opening a different file resets to 100%. A trackpad pinch zooms too, with the toolbars staying pinned at their normal size while the document scales behind them.

### Wrapping long lines in code

Two settings control how long lines of code behave, separately for the two surfaces.

- **Wrap lines in code blocks** (Markdown tab, under Document; on by default) governs rendered code blocks in Reading and Live. On, a long line wraps to the pane width; off, each block scrolls horizontally on its own.
- **Wrap lines in source** (General tab, under Source; on by default) governs the Source editor. On, long lines reflow to the pane width; off, the editor scrolls horizontally and keeps column alignment.

Both of these are the same thing as the wrap button in the top toolbar, which picks whichever of the two applies to the file you have open. Change it in either place and the other follows.

### Magnifying the active row

In Source and code editing the line your cursor is on lifts slightly toward you, so it is easy to see where you are working. It is on by default; turn **Magnify active row** off in Settings, on the General tab under Source, for a flat view. It does not apply in Live mode. A related toggle in the same section, **Highlight active row** (also on by default), tints the current line and its line number together as one accent band.

### Keyboard shortcut guide

Press **F1** at any time to open a full reference of every keyboard shortcut, grouped by task with keycap styling. In Reading mode **?** also opens it. Close it with Escape, F1 again, or a click outside the panel. The guide lists only shortcuts that are actually bound, so every entry works. It is also reachable from the right-click menu under **Keyboard shortcuts**.

### Formatting characters and whitespace

Source view marks spaces with faint dots and tabs with arrows out of the box. The opacity of these marks is adjustable: **Whitespace marker opacity** (Settings, General tab, under Source, on the same row as the show/hide switch) lets you dial them from barely visible to fully solid, applied live. **Whitespace dots in Source** turns the marks off entirely, and is the same switch as the whitespace button in the code toolbar. **Formatting characters** (Settings, Markdown tab, under Document) goes further: it adds a line-ending badge (LF or CRLF) to each line and shows the whitespace marks in Live mode too, not just Source.

### Indentation guides

Source view also draws a faint vertical line down each level of indentation, so you can see which lines belong to which block without counting spaces. The line sits on the left edge of its column, the way Notepad++ and VS Code draw theirs, and the guide for the block your cursor is in is drawn a little stronger than the rest.

The spacing comes from the file itself rather than from a fixed setting: a file indented by two gets guides every two columns, a file indented by four gets them every four. The columns are measured from the code font you have chosen, so a guide lands on the tab stop rather than beside it, and a line whose indent is not an exact multiple of the step still shows the level it is nested inside instead of dropping back one. A guide never runs down the inside of a string or comment that wraps over several indented lines, since a continuation is not a new block. **Indentation guides** in Settings, on the General tab under Source, turns them off, and so does the guides button in the code toolbar.

One rough edge worth knowing: a markdown file uses one spacing for the whole document, so a fenced code block indented more deeply than the surrounding list can pick up a guide part-way through its indentation.

### Single newlines as line breaks

Standard markdown joins lines separated by a single newline into one paragraph, and both views honour that. With the setting **off** (the default), a hard-wrapped paragraph flows to the pane width in Reading *and* in Live - Live renders each interior newline as a space, so three short source lines read as one flowing paragraph, exactly as Reading shows them. Switch to Source to see (or edit) the raw line breaks.

If you want a newline in the source to be a visible line break instead (the way chat apps and some note tools treat it), turn on **Render single newlines as breaks** in Settings, on the Markdown tab under Document. Every line you type then stays on its own line in Reading and Live alike, and the caret, cut and paste all work line by line, matching the source exactly.

To force a line break within a paragraph while the setting is off, end the line with two spaces or a backslash (a markdown hard break), or leave a blank line to start a new paragraph.

### Selection match highlighting

Select two or more characters and every other occurrence of that text is softly tinted in all three modes - Reading, Live and Source - so you can see where a word or phrase appears without running a search. The highlight is capped at 100 matches so large documents are not washed out. Turn it on or off with **Highlight matching text** in Settings, on the Markdown tab under Document (on by default).

### Ctrl+click to open a URL

In a Source editor (markdown Source or code Source), hold **Ctrl** (Cmd on Mac) and click a web address to open it in your browser. A plain click still places the cursor. Only `http` and `https` addresses open; `file://` links stay blocked.

### Scroll position memory

Within a session, DopusWorX remembers where you were scrolled in each file and puts you back there when you return to it.

### Gutter line selection

Click a line number to select that whole line; drag or **Shift+click** to extend the selection; **Ctrl+click** (Cmd on Mac) to add or remove individual lines for simultaneous multi-line edits. **Delete** removes the selected lines. This works in every editor that shows line numbers.

### Code and source appearance settings

Several appearance options for Source editors and rendered code blocks live in Settings, on the General tab under Source and on the Appearance tab under Code blocks and Source editor.

- **Tab width (columns)** (General &rsaquo; Source): how many columns a tab character occupies in Source and code editors. Accepts 1-8, default 4.
- **Line-number gutter** (General &rsaquo; Source): Off (no line numbers), Plain (neutral gutter), Accent bar (coloured bar on the left edge over a light tint), or Filled accent (accent colour fills the gutter column with numbers on top). It is the only gutter Source has: folding is marked on the line itself, not in a column of its own.
- **Source editor** (Appearance): five optional overrides - Source font (falls back to the Code font if empty), Source font size in px (falls back to the Code font size if empty), Source line height as a multiplier (falls back to the Code line height if empty), Source text colour (follows the active palette if empty; syntax tokens keep their own colours), and Source line-highlight colour (follows the UI accent or the Source editor palette if empty). Setting any field overrides only that property.
- **Code blocks** (Appearance): four optional fields that govern rendered code blocks in markdown - Code font, Code font weight, Code font size, and Code line height. Empty fields follow the palette or body defaults.

## Keyboard shortcuts

| Keys | What they do |
|---|---|
| **Ctrl+E** | Cycle through the view modes |
| **Alt+Left / Alt+Right** | Step backward / forward through the view modes (markdown and HTML) |
| **Alt+Up** | Open the split preview, switching to Source first if needed |
| **Alt+Down** | Close the split |
| **Ctrl+S** | Save |
| **Ctrl+Shift+S** | Save As |
| **Ctrl+F** | Find (all modes) |
| **Ctrl+G** | Go to line (a byte offset in the binary inspector) |
| **Ctrl+R / F5** | Reload from disk |
| **Ctrl+P** | Print / Save as PDF |
| **Ctrl+B / Ctrl+I** | Bold / italic (markdown Live and Source) |
| **Ctrl+Shift+C / Ctrl+Shift+X** | Inline code / strikethrough (markdown Live and Source) |
| **Ctrl+Shift+I** | Insert image (markdown Live and Source) |
| **Ctrl+Shift+T** | Insert table (markdown Live and Source) |
| **Ctrl+Shift+M** | Math symbol panel (markdown Live and Source) |
| **Ctrl+Z** | Undo (all editor surfaces) |
| **Ctrl+Y / Ctrl+Shift+Z** | Redo (all editor surfaces) |
| **Tab / Shift+Tab** | Indent / outdent the current line (any editor line, not just list lines) |
| **Ctrl+Alt+Left / Ctrl+Alt+Right** | Back / forward through the files this viewer has shown (mouse back/forward buttons work too) |
| **F11** | Toggle full screen (standalone viewer window) |
| **F1** | Open the keyboard shortcut guide (any mode; `?` also works in Reading) |
| **Ctrl+mouse wheel** | Zoom |
