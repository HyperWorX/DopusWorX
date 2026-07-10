# Split view showcase

Open this file, click **Source**, then click **Source again** — the raw markdown sits on the
left while this rendered page tracks it on the right. Drag the divider to resize; the link
button on the divider toggles linked scrolling. This document is deliberately dense with
formatting so the two panes look properly different.

## Why split view earns its place

Seeing the source *and* the result at once is the fastest way to learn what a construct does.
The table below reads as pipes and dashes on the left, and as this on the right:

| Construct | Source shape | Rendered shape |
| --- | --- | --- |
| Emphasis | `*stars*` and `**double stars**` | *italics* and **bold** |
| Inline code | backticks | `like_this()` |
| Strikethrough | `~~tildes~~` | ~~gone~~ |
| Highlight | `==equals==` | ==marked== |

## Code keeps its shape

```python
def fibonacci(n: int) -> int:
    """The classic — watch the syntax colours appear only on the right."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

## Quotes nest

> A blockquote wraps this paragraph.
>
> > And a nested one sits inside it, which reads as two `>` characters on the left
> > and as this indented card on the right.

## Lists, tasks and maths

1. Ordered items renumber themselves when you reorder the source
2. A task list shows real checkboxes only when rendered:
   - [x] pick an icon
   - [ ] ship rc.2
3. Inline maths renders from dollar signs: $e^{i\pi} + 1 = 0$

$$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$$

---

A horizontal rule above, a footnote here[^1], and a final paragraph so the page ends with
ordinary prose. Edit anything on the left and watch the right keep up.

[^1]: Footnotes collect themselves at the bottom of the rendered pane.
