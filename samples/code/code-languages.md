# Syntax highlighting: every supported language

One fenced block per language DopusWorX highlights, each with comments, strings,
numbers, keywords, and functions/types so the colours are easy to check. Open in
Reading mode to see them all rendered; the same grammars drive Live and Source.

## Web / JS family

### JavaScript

```javascript
// Fetch a user and greet them
const greet = async (id) => {
  const res = await fetch(`/api/users/${id}`);
  const user = await res.json();
  return `Hello, ${user.name}! You have ${user.points ?? 0} points.`;
};
greet(42).then(console.log);
```

### TypeScript

```typescript
interface User { id: number; name: string; admin?: boolean }

function describe<T extends User>(u: T): string {
  const role = u.admin ? "admin" : "member";
  return `#${u.id} ${u.name} (${role})`;
}
```

### JSX

```jsx
function Badge({ count }) {
  return (
    <span className="badge" title="unread">
      {count > 99 ? "99+" : count}
    </span>
  );
}
```

### TSX

```tsx
const List = ({ items }: { items: string[] }) => (
  <ul>{items.map((it, i) => <li key={i}>{it}</li>)}</ul>
);
```

### HTML

```html
<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><title>Demo</title></head>
  <body><h1 id="top">Hello &amp; welcome</h1></body>
</html>
```

### CSS

```css
:root { --accent: #e0742f; }
.button:hover {
  color: var(--accent);
  transition: color 150ms ease-in-out;
}
```

### SCSS

```scss
$accent: #e0742f;
.card {
  border: 1px solid darken($accent, 10%);
  &__title { font-weight: 700; }
}
```

### Less

```less
@accent: #e0742f;
.card {
  border: 1px solid lighten(@accent, 10%);
  .title { font-weight: 700; }
}
```

## Systems

### C

```c
#include <stdio.h>
/* sum the first n integers */
int sum(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) total += i;
    return total;
}
```

### C++

```cpp
#include <vector>
#include <numeric>

template <typename T>
T total(const std::vector<T>& xs) {
    return std::accumulate(xs.begin(), xs.end(), T{0});  // fold
}
```

### Rust

```rust
fn fib(n: u64) -> u64 {
    match n {
        0 | 1 => n,
        _ => fib(n - 1) + fib(n - 2),
    }
}
```

### Go

```go
package main

import "fmt"

func main() {
    nums := []int{1, 2, 3}
    sum := 0
    for _, n := range nums { sum += n }
    fmt.Printf("sum = %d\n", sum)
}
```

### Swift

```swift
struct Point { var x, y: Double }

func distance(_ a: Point, _ b: Point) -> Double {
    let dx = a.x - b.x, dy = a.y - b.y
    return (dx * dx + dy * dy).squareRoot()
}
```

## JVM / application

### Java

```java
public class Greeter {
    // null-safe greeting
    public static String greet(String name) {
        return "Hello, " + (name == null ? "world" : name) + "!";
    }
}
```

### C#

```csharp
public record User(int Id, string Name) {
    public string Describe() => $"#{Id} {Name}";
}
```

### Kotlin

```kotlin
fun main() {
    val nums = listOf(1, 2, 3, 4)
    println(nums.filter { it % 2 == 0 }.sum())  // 6
}
```

### Scala

```scala
object Main extends App {
  val squares = (1 to 5).map(n => n * n)
  println(squares.mkString(", "))
}
```

### Dart

```dart
int factorial(int n) => n <= 1 ? 1 : n * factorial(n - 1);

void main() => print('5! = ${factorial(5)}');
```

## Scripting

### Python

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def norm(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

### Ruby

```ruby
# Sum the even numbers
def even_sum(nums)
  nums.select(&:even?).reduce(0, :+)
end

puts even_sum([1, 2, 3, 4])  # => 6
```

### PHP

```php
<?php
function greet(string $name = "world"): string {
    return "Hello, {$name}!";
}
echo greet("DopusWorX");
```

### Perl

```perl
use strict;
use warnings;

my @nums = (1 .. 5);
my $sum  = 0;
$sum += $_ for @nums;
print "sum = $sum\n";
```

### Lua

```lua
local function map(t, f)
  local r = {}
  for i, v in ipairs(t) do r[i] = f(v) end
  return r
end
print(table.concat(map({1, 2, 3}, function(x) return x * x end), ", "))
```

### R

```r
# Mean of a numeric vector
mean_of <- function(x) {
  sum(x) / length(x)
}
print(mean_of(c(2, 4, 6, 8)))
```

### Bash

```bash
#!/usr/bin/env bash
# Count markdown files
count=$(find . -name '*.md' | wc -l)
echo "Found ${count} markdown files"
```

### PowerShell

```powershell
# Five largest files in the current folder
Get-ChildItem -File |
  Sort-Object Length -Descending |
  Select-Object -First 5 Name, Length
```

### Batch

```batch
@echo off
setlocal
set "name=%~1"
if "%name%"=="" set "name=world"
echo Hello, %name%!
```

### VBScript

```vbscript
' Greet a user, VBScript style
Dim count
count = 3
Function Greet(name)
    If count > 0 Then
        Greet = "Hello, " & name & "!"
    Else
        Greet = "Goodbye"
    End If
End Function
WScript.Echo Greet("World")
```

### AutoHotkey

```autohotkey
; Increment a counter on a hotkey
#SingleInstance Force
global Count := 0
^!s::                  ; Ctrl+Alt+S
    Count += 1
    MsgBox, 64, Status, Pressed %Count% times
return
```

### NirCmd

```nircmd
// Announce a result, set volume, take a screenshot
speak text "Build finished" 2 100
setsysvolume 40000
savescreenshot "~$folder.desktop$\shot.png"
wait 1500
```

## Data / config / query

### JSON

```json
{
  "name": "DopusWorX",
  "version": "0.2.1",
  "languages": ["python", "rust", "go"],
  "enabled": true,
  "ratio": 1.618
}
```

### YAML

```yaml
name: DopusWorX
version: 0.2.1
features:
  - syntax-highlighting
  - math
enabled: true
```

### TOML

```toml
[package]
name = "dopusworx"
version = "0.2.1"

[features]
math = true
langs = ["python", "rust"]
```

### INI

```ini
; sample config
[server]
host = 127.0.0.1
port = 8080
debug = false
```

### SQL

```sql
-- Top customers by revenue
SELECT c.name, SUM(o.total) AS revenue
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.name
ORDER BY revenue DESC
LIMIT 5;
```

### XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
  <book id="bk101">
    <title>Markdown for Opus</title>
    <price currency="USD">9.99</price>
  </book>
</catalog>
```

### CSV

```csv
region,product,units,price
North,Widget,1200,4.50
South,Gizmo,275,29.99
```

## Other

### LaTeX

```latex
\documentclass{article}
\begin{document}
The Gaussian integral: $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$.
\end{document}
```

### Dockerfile

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
CMD ["node", "build.mjs"]
```

### Markdown

```markdown
# Title

- **bold**, *italic*, `code`
- [a link](https://example.com)

> a blockquote
```

### Diff

```diff
--- a/viewer.css
+++ b/viewer.css
@@ -529,7 +529,7 @@
 #content .mdwx-csv {
-    width: max-content; min-width: 100%;
+    width: max-content;
 }
```
