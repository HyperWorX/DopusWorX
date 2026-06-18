# DopusWorX menus

Right-click anywhere in a DopusWorX pane and you get its own menu, built for what you clicked on. The toolbar at the top carries a Save button with its own drop-down for the export and print actions. This page covers both.

The viewer turns off the WebView2 browser menu on purpose, so the menu you see is always the DopusWorX one, never the generic browser entries. Everything below is what actually appears.

## The right-click menu

![The right-click menu in Reading mode, showing Copy, Print / Save as PDF, Select all and Zoom](images/context-menu.png)

The menu is built fresh on every right-click, so it only ever lists actions that apply to where you clicked. Two things decide what you get:

- The **mode** you are in: Reading, Live, or Source.
- The **file kind**: a Markdown document, a code or text file, or a CSV / TSV table.

Live, Source, and code Edit are editable surfaces. Reading and code View are read-only, so the editing items (Cut, Paste, Insert image, Find, Replace) are held back there.

### Markdown and document views

These are the items you can see, roughly top to bottom. Not all show at once.

- **Cut.** Only when you are on an editable surface and have text selected.
- **Copy.** Always present. Click it to copy straight away (the selection if you have one, otherwise the whole document source). Hover the arrow for the longer list:
  - **Selection**, when text is selected.
  - **Document as Markdown** copies the raw Markdown source.
  - **Document as HTML** copies the rendered HTML.
  - **Document as Rich text** copies it as formatted rich text, so it pastes with its styling into Word and the like.
  - **Document as Plain text** strips the markup and copies just the words.
- **Paste.** Editable surfaces only.
- **Insert image...** Editable Markdown only. It opens the same image dialog as the editing toolbar's image button. It is Markdown-only because it writes a Markdown image line `![alt](path)`, which is inert anywhere else. Code, HTML, CSV and even LaTeX / TeX source editors do not show it: LaTeX is prose-like for maths but uses `\includegraphics`, not Markdown image syntax.
- **Find...** and **Replace...** Editable surfaces only. They open the editor's find or find-and-replace bar.
- **Math.** A single submenu that changes with what is under your cursor. It only appears where maths makes sense (a prose-like file with maths switched on, or a rendered equation you have clicked):
  - On plain text or a selection, it offers **Inline math  $...$** and **Block math  $$...$$**, which wrap the selection (or drop an empty equation at the cursor).
  - With the cursor inside an existing `$...$` or `$$...$$` region, it offers the swaps instead: **Convert to inline** / **Convert to block**, and **Convert to LaTeX** / **Convert to AsciiMath** (labelled for whichever the equation is now). A fenced `am` block only offers the LaTeX / AsciiMath swap.
  - On a rendered equation, even in read-only Reading, you also get **Copy (LaTeX)** and **Copy (AsciiMath)**, which copy the equation in either notation regardless of how it was typed.
- **Copy link address** and **Open link in browser.** Only when you right-click a link. The first copies the raw `href`, the second opens it in your default browser.
- **Copy image address.** Only when you right-click an image. Copies its `src`.
- **Print / Save as PDF...** For Markdown documents (and CSV in the table view). Prints the whole document with the palette and styling intact, or saves it as a PDF through the print dialog.
- **Select all.** Always present. Selects the document text in the live surface.
- **Zoom.** Always present. A submenu of fixed steps (50, 75, 90, 100, 125, 150, 175, 200 percent) plus **Reset zoom**. This zooms the document or source content. The HTML View zooms itself inside its own frame, so this does not drive that.

#### How the menu shifts by mode

- **Reading** is read-only. No Cut, Paste, Insert image, Find or Replace. You still get Copy (with the document-as forms), Copy link / image address on a link or image, Copy equation on a rendered equation, Print / Save as PDF, Select all and Zoom.
- **Live** and **Source** are editable. The full editing set turns on: Cut (with a selection), Paste, Insert image (Markdown only), Find, Replace, and the Math insert / convert actions (prose-like files).

#### How it shifts by file kind

- **Markdown** gets the full Copy submenu (Markdown / HTML / Rich text / Plain text), Insert image, the Math actions, and Print / Save as PDF.
- **Code and text** files get a simpler Copy (**Selection** and **Entire document**), plus Find and Replace when editable. No Insert image and no Print entry. LaTeX / TeX source counts as prose-like for maths, so it gets the Math actions, but not Insert image (which writes Markdown image syntax).
- **CSV / TSV** in the table view gets its own grid actions, below.

### CSV and TSV table view

Open a CSV or TSV and Reading mode shows it as a sortable, editable grid. Right-click a cell and the grid first selects that cell (and its row and column), so the actions act on what you clicked.

- **Copy** here lists:
  - **Selected cells**, when you have a block of cells selected. Copies them as tab-separated text, laid out as they sit on screen.
  - **Cell**, the value of the clicked cell.
  - **Table as Markdown**, the current view (respecting any filter and sort) as a Markdown table.
  - **Document (CSV source)**, the raw file text.
- **Insert** submenu:
  - **Row above**, **Row below**, **Column left**, **Column right**, each relative to the clicked cell.
  - **Add rows...** and **Add columns...** open a small prompt to add several at once.
- **Delete row** and **Delete column**, on the clicked cell's row and column. The grid keeps at least one row and one column.
- **Sort by this column** submenu: **Ascending**, **Descending**, **Clear sort**. Sorting is view-only, so the saved file keeps its original row order.
- Below the grid actions you still get **Print / Save as PDF...**, **Select all** (which here selects every grid cell, ready to copy, rather than the page text), and **Zoom**.

The grid has more on board than the right-click menu shows. The bar above it has a live row filter, a delimiter override (auto, comma, semicolon, tab, pipe), and Header / Wrap / Freeze toggles. In the grid itself you can double-click a cell to edit it, drag column and row edges to resize, click a header to cycle its sort, and use the hover + / x controls in the gutter and above each column to add or remove rows and columns. To copy, use the Copy item on the right-click menu (the focused cell or the selected block). To insert a row, use the + control in the gutter or the right-click menu.

## The Save menu in the toolbar

The Save control at the top is a split button: the disk icon on the left is **Save**, and the small caret next to it opens the rest of the save and export actions.

- **Save.** The main button. Writes the current file in place. It is greyed out until you have unsaved changes and a real file path to write to.
- **Save As...** Writes the document to a new file you choose. Available whenever there is something loaded or edited.
- **Save a Copy...** Writes a copy to a new file without changing which file you are editing. Same availability as Save As.
- **Export as HTML...** Markdown only. Writes the rendered document out as an HTML file. Hidden for other kinds.
- **Export as Plain text...** Code and text files only (everything that is not Markdown). Hidden for Markdown.
- **Print / Save as PDF...** Offered for any kind that has content loaded. Prints the document or saves it as a PDF through the print dialog.

So the export entry you see depends on the file: a Markdown document shows **Export as HTML**, a code or text file shows **Export as Plain text**, and **Print / Save as PDF** is there for both. The two export entries never show together.
