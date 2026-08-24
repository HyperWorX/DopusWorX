# Palettes

30 built-in palettes &middot; 18 dark &middot; 12 light, plus the **Default** dark
and light themes the viewer falls back to when no palette is pinned.

Out of the box no palette is fixed: the page follows the Opus pane background
(light or dark), which is what the **Default Dark** and **Default Light** cards
below show. Pick any of the named palettes to pin it instead.

Each card shows two states of the live editor:

- **Cursor elsewhere** - markers hidden / replaced (the rendered look).
- **Cursor on line** - raw markdown source revealed.

Every marker token is coloured via the palette accent; bold / italic / strike / inline-code each get their own palette-derived colour.

## Dark palettes

<table>
<tr>
<td width="50%"><b>Default Dark</b><br><img src="palette-images/default-dark.png" alt="Default Dark"></td>
<td width="50%"><b>ProWorX</b><br><img src="palette-images/proworx.png" alt="ProWorX"></td>
</tr>
<tr>
<td width="50%"><b>GloWorX</b><br><img src="palette-images/gloworx.png" alt="GloWorX"></td>
<td width="50%"><b>Dracula</b><br><img src="palette-images/dracula.png" alt="Dracula"></td>
</tr>
<tr>
<td width="50%"><b>Solarized Dark</b><br><img src="palette-images/solarized-dark.png" alt="Solarized Dark"></td>
<td width="50%"><b>Nord</b><br><img src="palette-images/nord.png" alt="Nord"></td>
</tr>
<tr>
<td width="50%"><b>Gruvbox Dark</b><br><img src="palette-images/gruvbox-dark.png" alt="Gruvbox Dark"></td>
<td width="50%"><b>One Dark</b><br><img src="palette-images/one-dark.png" alt="One Dark"></td>
</tr>
<tr>
<td width="50%"><b>Tokyo Night</b><br><img src="palette-images/tokyo-night.png" alt="Tokyo Night"></td>
<td width="50%"><b>Ayu Dark</b><br><img src="palette-images/ayu-dark.png" alt="Ayu Dark"></td>
</tr>
<tr>
<td width="50%"><b>Catppuccin Mocha</b><br><img src="palette-images/catppuccin-mocha.png" alt="Catppuccin Mocha"></td>
<td width="50%"><b>GitHub Dark</b><br><img src="palette-images/github-dark.png" alt="GitHub Dark"></td>
</tr>
<tr>
<td width="50%"><b>Obsidianite</b><br><img src="palette-images/obsidianite.png" alt="Obsidianite"></td>
<td width="50%"><b>PLN Dark</b><br><img src="palette-images/pln-dark.png" alt="PLN Dark"></td>
</tr>
<tr>
<td width="50%"><b>AnuPpuccin Frappé</b><br><img src="palette-images/anuppuccin-frappe.png" alt="AnuPpuccin Frappé"></td>
<td width="50%"><b>Everforest</b><br><img src="palette-images/everforest.png" alt="Everforest"></td>
</tr>
<tr>
<td width="50%"><b>Rosé Pine</b><br><img src="palette-images/rose-pine.png" alt="Rosé Pine"></td>
<td width="50%"><b>Vesper</b><br><img src="palette-images/vesper.png" alt="Vesper"></td>
</tr>
<tr>
<td width="50%"><b>Red Rascal</b><br><img src="palette-images/red-rascal.png" alt="Red Rascal"></td>
<td width="50%"></td>
</tr>
</table>

## Light palettes

<table>
<tr>
<td width="50%"><b>Default Light</b><br><img src="palette-images/default-light.png" alt="Default Light"></td>
<td width="50%"><b>ProWorX Light</b><br><img src="palette-images/proworx-light.png" alt="ProWorX Light"></td>
</tr>
<tr>
<td width="50%"><b>PLN Light</b><br><img src="palette-images/pln-light.png" alt="PLN Light"></td>
<td width="50%"><b>Solarized Light</b><br><img src="palette-images/solarized-light.png" alt="Solarized Light"></td>
</tr>
<tr>
<td width="50%"><b>GitHub Light</b><br><img src="palette-images/github-light.png" alt="GitHub Light"></td>
<td width="50%"><b>Ayu Light</b><br><img src="palette-images/ayu-light.png" alt="Ayu Light"></td>
</tr>
<tr>
<td width="50%"><b>Gruvbox Light</b><br><img src="palette-images/gruvbox-light.png" alt="Gruvbox Light"></td>
<td width="50%"><b>Catppuccin Latte</b><br><img src="palette-images/catppuccin-latte.png" alt="Catppuccin Latte"></td>
</tr>
<tr>
<td width="50%"><b>One Light</b><br><img src="palette-images/one-light.png" alt="One Light"></td>
<td width="50%"><b>Tokyo Night Day</b><br><img src="palette-images/tokyo-night-day.png" alt="Tokyo Night Day"></td>
</tr>
<tr>
<td width="50%"><b>Nord Light</b><br><img src="palette-images/nord-light.png" alt="Nord Light"></td>
<td width="50%"><b>Alucard</b><br><img src="palette-images/alucard.png" alt="Alucard"></td>
</tr>
<tr>
<td width="50%"><b>Obsidianite Light</b><br><img src="palette-images/obsidianite-light.png" alt="Obsidianite Light"></td>
<td width="50%"></td>
</tr>
</table>

## Appearance settings

The palettes above set a whole look at once. You pick them from the **Global
palette** dropdown in Settings &rsaquo; Appearance, with dark and light palettes
grouped and Default Auto following the Opus pane. For finer control, the rest of
the Appearance tab overrides individual colours, fonts, headings, list spacing, rules
and page layout on top of the active palette; an empty field falls back to the palette
default. GloWorX is the exception: its neon look is pinned in the stylesheet, so its
colour fields appear greyed out when it is the active palette.

<div align="center"><img src="images/settings-appearance.png" width="560" alt="The Appearance tab: the Global palette dropdown open with Default Auto and the grouped dark palettes, above the Code block palette picker"></div>

Every colour field carries an alpha slider between the text input and the reset link.
Drag it to set transparency on any colour: it reads the alpha from whatever notation
is already in the field (hex, rgba(), hsla(), or eight-digit #RRGGBBAA) and writes
it back in the same notation, so a live-preview fires on every drag exactly as if you
had typed. The slider hides when the field holds a CSS gradient, which has no single
alpha.

The background fields (Page background, Code block, Blockquote, Table header,
Table cell, and Highlight) also accept a CSS gradient typed directly into the field.
Any valid gradient value (linear-gradient(), radial-gradient(),
repeating-linear-gradient(), and so on) is applied as a background-image layer in
both Reading and Live view; the solid colour override is cleared so the palette's
colour-mix consumers (highlight opacity, table-header hover tints) keep a real colour
to work from.

A few related controls sit alongside the palette picker:

- **Code block palette** colours fenced code blocks in a rendered document,
  independently of the page. Match palette (the default) derives the code
  colours from the active palette; picking a named entry locks the code
  colouring regardless of the page, and inline `code` takes the same entry's
  background and text colour so it matches the blocks. Choosing a named entry
  clears any **Code background** colour you have set, because the entry now owns
  the code-block background; equally, setting a Code background colour resets
  this back to Match palette.
- **Source editor palette** does the same job for the raw file in Source view.
  Match global palette (the default) keeps the editor in the palette's own
  colours, Same as code in documents follows the row above, and any named entry
  gives the editor a scheme of its own, which is what you want if you like a dark
  editor over a light document.
- **DOpus theme** tells the viewer whether to treat your Directory Opus theme as
  light or dark when the automatic guess gets it wrong.
- **Viewer background** colours the area behind the page card; leave it empty
  to match your Opus pane automatically (identical in the pane and the standalone
  window). It travels with your custom palettes and themes and is left alone by
  the built-in presets.
- **Page width**, in the Page layout section, controls how the page card fills
  the viewer: **Fixed width** keeps a centred column (Page max width applies),
  **Flexible** fills the viewer width and puts a drag grip on each page edge so
  you can set your own (double-click a grip to reset), and **Fill** goes edge to
  edge with the background carried up behind the toolbar. A flexible width is
  stored as a proportion of the pane rather than a pixel count, so a width set in
  a narrow pane comes out sensibly in a wide standalone window, and it is damped
  above about 900px so a big screen keeps widening the page but slowly.
- **Padding and margins**, in the same section, are six text fields: padding on
  all four sides of the page, and a top and bottom margin. The padding is the gap
  inside the page, between its edge and the text; the margin is the gap outside
  it, between the page and the pane. The top margin is what holds the first line
  clear of the floating toolbar, so that is the one to reduce if you want the
  document to start higher. Each field takes a bare number as pixels or any CSS
  length, and an empty field keeps the default.
- **Quotes**, **Tables** and **Lines**, further down the Appearance tab, hold the
  blockquote and table colours and the horizontal rule: its colour, its thickness
  and its **style** - solid, a gradient fade, a centre fade, dotted, dashed, a
  double line, or three centred diamonds. (The banner height is on the Markdown
  tab, under Images.)

<div align="center"><img src="images/hr-styles.png" width="640" alt="The seven horizontal rule styles stacked and labelled: solid, gradient fade, centre fade, dotted, dashed, double line and the three-diamond ornament"></div>

- **Save...**, beside the Global palette picker, keeps your current tweaks as
  something you can come back to. Name it, then choose how much of the current
  look to keep: a **Theme** is the colours and the layout together, a **Palette**
  is the colours only, and a **Style** is the fonts, spacing and toolbar. Your
  saved entries appear in the picker grouped under those three headings. Select
  one and a **Delete** button appears next to Save. **Import...** / **Export...**
  in the footer move your whole settings file between machines.

