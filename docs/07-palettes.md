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
the Appearance tab overrides individual colours, fonts, headings, rules and page
layout on top of the active palette; an empty field falls back to the palette
default.

A few related controls sit alongside the palette picker:

- **Syntax palette** colours fenced code blocks independently of the page.
  Match palette (the default) derives code colours from the active palette;
  picking a named entry locks the code colouring regardless of the page. A
  separate toggle, **Use syntax palette in source mode**, extends it to the
  Source editor.
- **DOpus theme counts as** tells the viewer whether to treat your Directory
  Opus theme as light or dark when the automatic guess gets it wrong.
- The **Themes** menu at the bottom of Settings saves your current tweaks as a
  reusable palette, style or theme of your own, and **Import...** / **Export...**
  move your whole settings file between machines.

