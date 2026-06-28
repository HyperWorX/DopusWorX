# Binary inspector

A file that is binary rather than text opens in the binary inspector: a hex view of its bytes, with a panel that reads the values under your cursor. DopusWorX decides a file is binary by looking at its content, not its name, so a binary with a text-like extension still opens here, and a text file with an unusual extension does not.

The inspector is on by default. Turn **Binary inspector** off in Settings to send binary files back to the plain not-text notice instead.

## The hex view

The view has the three classic columns: the byte offset down the left, the bytes as hex in the middle, and the same bytes as text on the right, with anything unprintable shown as a dot. It is virtualised, so a large file scrolls smoothly without loading all of it into the page at once.

## The data inspector

Down the side, the data inspector reads the bytes starting at the cursor as the common types at once: signed and unsigned integers, 32 and 64-bit floating point, and the character. Move the cursor and the readings update to match the new position.

## Selecting bytes

- Click a byte to put the cursor on it.
- Shift-click, or click and drag, to select a range.
- Ctrl+A selects the whole file.

The selection drives Copy (below).

## Going to an offset

Press Ctrl+G to jump to a byte offset. It takes a hex offset, with or without a `0x` prefix (`0x400` or `400`), or a decimal with a `#` in front (`#1024`). The view scrolls to that byte and puts the cursor on it.

## Searching

Open the find bar with Ctrl+F. A **Hex** toggle in the bar switches what it searches for:

- With Hex off, it searches for text, matching the bytes of what you type.
- With Hex on, it searches for a hex pattern, so `4d 5a` finds those two bytes in order.

The previous and next arrows step through the matches.

## Copying

Copy gives you the current selection, or the byte under the cursor when nothing is selected, in two forms: as hex bytes, or as text. Pick the form you want from the Copy menu.

## View as hex, view as text

Any file can be opened in the inspector on demand, not only the ones detected as binary. Right-click and choose **View as hex** to open the current file in the inspector, and **View as text** to go back to the normal text or code view. This is useful for peeking at the bytes of a file that is technically text, or for forcing a borderline file one way or the other.

## Editing bytes

The inspector is read-only out of the box. Turn on **Allow binary editing** in Settings (it needs the Binary inspector on) and the hex pane gains an **Edit** toggle. With Edit on:

- Typing **overwrites** the byte under the cursor. Type in the hex column, two characters to a byte, or in the text column, one character to a byte.
- **Insert** switches to insert mode, where typing adds bytes instead of overwriting them.
- **Delete** and **Backspace** remove bytes.
- Undo and redo work as everywhere else.
- **Ctrl+S** writes the changes back to the file, through the same safe-save path as every other format.

Editing raw bytes can corrupt a file that another program expects in a particular shape, so the editor stays off until you switch it on.
