# Syntax highlighting sampler

A fenced block per language, each with comments, strings, numbers, keywords and
functions so the colours are easy to check. This is a representative set, not all
of the roughly 150 supported languages: the common ones are built in, and the
rest (under "More languages" below) load on demand. Open in Reading mode to see
them rendered.

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

## More languages (loaded on demand)

These grammars aren't bundled; they load the first time a block in that language
is shown. Open this file in Reading mode and the colours fill in a moment later.

### Nix

```nix
# a tiny dev shell
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [ pkgs.hello ];
  shellHook = "echo ready";
}
```

### Zig

```zig
const std = @import("std");
pub fn main() void {
    const n: u32 = 42; // the answer
    std.debug.print("n = {d}\n", .{n});
}
```

### Solidity

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
contract Counter {
    uint256 public count;
    function inc() public { count += 1; }
}
```

### Svelte

```svelte
<script>
  let count = 0;
  const inc = () => count += 1;
</script>
<button on:click={inc}>Clicked {count} times</button>
```

### Elixir

```elixir
defmodule Greeter do
  @greeting "hello"
  def hi(name), do: "#{@greeting}, #{name}"
end
```

### HCL / Terraform

```hcl
# a resource
resource "aws_s3_bucket" "data" {
  bucket = "my-bucket"
  tags   = { Env = "dev" }
}
```

### WGSL

```wgsl
@vertex
fn main(@location(0) pos: vec3<f32>) -> @builtin(position) vec4<f32> {
  return vec4<f32>(pos, 1.0); // clip space
}
```

### Haskell

```haskell
-- factorial
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

### Clojure

```clojure
;; greet someone
(defn greet [name]
  (str "hello, " name))
(greet "world")
```

### Julia

```julia
# sum of squares
function sumsq(xs)
    return sum(x^2 for x in xs)
end
sumsq([1, 2, 3])
```

### OCaml

```ocaml
(* double each item *)
let double xs = List.map (fun x -> x * 2) xs
let () = print_int (List.length (double [1; 2; 3]))
```

### F#

```fsharp
// squares
let squares = [ for x in 1..5 -> x * x ]
printfn "%A" squares
```

### Erlang

```erlang
%% greet someone
-module(greeter).
-export([hi/1]).
hi(Name) -> "hello, " ++ Name.
```

### Groovy

```groovy
// greet someone
def greet(name) { "hello, $name" }
println greet("world")
```

### Scheme

```scheme
;; square a number
(define (square x) (* x x))
(display (square 9))
```

### Objective-C

```objective-c
// greet someone
#import <Foundation/Foundation.h>
NSString *greet(NSString *name) {
    return [NSString stringWithFormat:@"hello, %@", name];
}
```

### MATLAB / Octave

```octave
% sum of squares
function s = sumsq(xs)
  s = sum(xs .^ 2);
end
```

### Mathematica

```mathematica
(* square each item *)
squares[xs_] := Map[#^2 &, xs]
squares[{1, 2, 3}]
```

### Verilog

```verilog
// a 4-bit counter
module counter(input clk, output reg [3:0] q);
  always @(posedge clk) q <= q + 1;
endmodule
```

### VHDL

```vhdl
-- a 2-input and gate
entity and2 is
  port (a, b : in bit; y : out bit);
end entity;
```

### Tcl

```tcl
# greet someone
proc greet {name} {
  return "hello, $name"
}
puts [greet world]
```

### Fortran

```fortran
! sum of squares
program sumsq
  integer :: i, s = 0
  do i = 1, 3
    s = s + i*i
  end do
  print *, s
end program
```

### Crystal

```crystal
# greet someone
def greet(name : String)
  "hello, #{name}"
end
puts greet("world")
```
