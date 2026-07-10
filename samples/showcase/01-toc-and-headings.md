# TOC and Headings showcase

This file shows the Table of Contents and heading fixes. Open it in Reading to
see the finished page, and in Live to edit. To regenerate the list below,
right-click and choose Insert Table of Contents (it also keeps itself in sync as
you add or rename headings).

<!-- toc -->
<div class="dwx-toc-title">Table of Contents</div>

1. [Real section](#real-section)
2. [Centred title](#centred-title)
3. [Div-wrapped title](#div-wrapped-title)
4. [Indented heading](#indented-heading)
5. [Images](#images)
6. [Location](#location)
7. [Title](#title)

<hr class="dwx-toc-rule">
<!-- /toc -->

## Real section

A normal heading. It appears in the list above, folds in Live (click the arrow
in the gutter), and its link scrolls here.

> ## Quoted heading (should NOT be listed)
>
> This heading lives inside a blockquote, so it is quoted content, not document
> structure. It must NOT appear in the Table of Contents and must NOT get a fold
> arrow in Live. It still renders as a heading.

| Heading | Notes |
|---------|-------|
| # Not a title | A "#" inside a table cell is just text, never a TOC entry. |

<center>

## Centred title

</center>

A heading on the line right after a lone `<center>` opener (no blank line needed)
is still a real heading: it is listed above and its anchor resolves.

<div align="center">

### Div-wrapped title

</div>

Same for `<div align="center">`.

   # Indented heading

An ATX heading indented up to three spaces is still a heading. The list entry
reads "Indented heading" with no leading "#".

## Images

Headings whose text matches a browser/document property (Images, Location,
Title, ...) used to lose their anchor and the TOC link went dead. They resolve
now.

## Location

Body under Location.

## Title

Body under Title. All three links above jump to the right heading.
