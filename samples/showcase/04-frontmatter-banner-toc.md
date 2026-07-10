---
banner: https://upload.wikimedia.org/wikipedia/commons/2/27/Salvador_Dali_NYWTS.jpg
title: Frontmatter, banner and TOC
tags: [showcase, frontmatter, banner, toc]
date: 2026-07-10
description: How a banner, a frontmatter block and the Table of Contents share the top of a page without fighting.
---

# Frontmatter, banner and TOC

Three things share the top of this page and stay out of each other's way:

- the **banner** image strip, pinned flush against the very top of the card;
- the **frontmatter** block (the `---` key/values above), which in Live renders
  as one dim, ordinary-editable block with no stray gap above it - click anywhere
  in it and the caret lands exactly where you clicked;
- the **Table of Contents** below, which lists only real document headings.

Open this in Reading to see the finished page, then switch to Live to edit. To
regenerate the list below, right-click and choose Insert Table of Contents; it
keeps itself in sync as you add or rename headings.

<!-- toc -->
<div class="dwx-toc-title">Table of Contents</div>

1. [Frontmatter, banner and TOC](#frontmatter-banner-and-toc)
   1. [Real section](#real-section)
   2. [Another real section](#another-real-section)
   3. [What the TOC leaves out](#what-the-toc-leaves-out)
   4. [Banner and frontmatter together](#banner-and-frontmatter-together)

<hr class="dwx-toc-rule">
<!-- /toc -->

## Real section

A normal heading. It is listed in the Table of Contents above, folds in Live
(click the arrow in the gutter), and its link scrolls here.

## Another real section

Also listed. Rename it and the Table of Contents stays in step.

## What the TOC leaves out

The two headings below look like structure but are not: one is quoted, one is a
table cell. The Table of Contents skips both, and Live gives neither a fold arrow.

> ## Quoted heading (not in the TOC)
>
> This heading lives inside a blockquote, so it is quoted content, not document
> structure. It still renders as a heading, but it never becomes a Table of
> Contents entry and never leaves a dead link behind.

| Heading | Notes |
|---------|-------|
| # Not a title | A "#" inside a table cell is just text, never a TOC entry. |

## Banner and frontmatter together

Switch between Reading and Live. In both modes:

- the banner stays pinned at the top of the card, its left and right edges fading
  softly into the page colour instead of ending on a hard line;
- the frontmatter sits directly under it - in Live as a single dim, editable
  block with no gap above it, in Reading tucked away so the banner leads;
- the Table of Contents above lists these four real sections only.

A paragraph of ordinary body text, so there is content under the fold to scroll
through while the banner stays put.
