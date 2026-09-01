# Sass / SCSS Notes

> **Topic:** Sass (Syntactically Awesome Style Sheets)
> **Reference:** Sass Tutorial for Beginners - CSS With Superpowers
> **Video:** https://youtu.be/_a5j7KoflTs

---

## 1. What is Sass?

**Sass** stands for **Syntactically Awesome Style Sheets**.

Sass is a **CSS preprocessor** that extends CSS with additional features such as:

* Variables
* Nesting
* Mixins
* Functions
* Operators
* Partials
* Modules
* Inheritance
* Control directives

Sass helps make CSS easier to:

* Write
* Organize
* Reuse
* Maintain
* Scale

Sass code is compiled into normal CSS that browsers can understand.

```text
Sass / SCSS
     ↓
  Compiler
     ↓
    CSS
     ↓
   Browser
```

---

# 2. Sass vs CSS

### CSS

```css
.container {
    width: 100%;
}

.container .title {
    color: red;
}
```

### SCSS

```scss
.container {
    width: 100%;

    .title {
        color: red;
    }
}
```

SCSS allows related selectors to be nested inside one another.

---

# 3. Sass Syntaxes

Sass provides two main syntaxes:

### SCSS

Uses `.scss` extension.

```scss
$primary-color: blue;

body {
    color: $primary-color;
}
```

SCSS syntax is very similar to normal CSS.

### Indented Sass

Uses `.sass` extension.

```sass
$primary-color: blue

body
    color: $primary-color
```

The `.sass` syntax uses indentation instead of `{}` and `;`.

### Difference

| SCSS           | Sass             |
| -------------- | ---------------- |
| Uses `{}`      | Uses indentation |
| Uses `;`       | Does not use `;` |
| Similar to CSS | Different syntax |
| `.scss`        | `.sass`          |

For beginners, **SCSS is generally easier to adopt because it looks like CSS**.

---

# 4. Installing Sass

Sass can be installed using npm.

```bash
npm install -g sass
```

Check the installed version:

```bash
sass --version
```

---

# 5. Compiling Sass

Suppose we have:

```text
style.scss
```

Compile it into:

```text
style.css
```

Command:

```bash
sass style.scss style.css
```

---

# 6. Watch Mode

During development, it is useful to automatically compile Sass whenever the source file changes.

```bash
sass --watch style.scss style.css
```

Now Sass watches the SCSS file for changes.

---

# 7. Compiling an Entire Folder

```bash
sass --watch scss:css
```

Example:

```text
project/
├── scss/
│   └── style.scss
│
└── css/
    └── style.css
```

The SCSS files inside `scss/` are compiled into CSS files inside `css/`.

---

# 8. Sass Variables

Variables allow us to store values and reuse them.

### Syntax

```scss
$variable-name: value;
```

Example:

```scss
$primary-color: blue;
$font-size: 18px;

body {
    color: $primary-color;
    font-size: $font-size;
}
```

Compiled CSS:

```css
body {
    color: blue;
    font-size: 18px;
}
```

---

# 9. Types of Values Stored in Variables

Sass variables can store different types of values.

### Colors

```scss
$primary-color: #3498db;
```

### Numbers

```scss
$width: 100px;
```

### Strings

```scss
$font: Arial;
```

### Boolean

```scss
$is-dark: true;
```

### Lists

```scss
$font-stack: Arial, Helvetica, sans-serif;
```

### Maps

```scss
$colors: (
    primary: blue,
    secondary: green
);
```

---

# 10. Variable Reuse

Instead of repeating the same value:

```scss
button {
    background-color: #3498db;
}

a {
    color: #3498db;
}

.title {
    color: #3498db;
}
```

Use a variable:

```scss
$primary-color: #3498db;

button {
    background-color: $primary-color;
}

a {
    color: $primary-color;
}

.title {
    color: $primary-color;
}
```

This makes changes easier.

---

# 11. Variable Scope

Variables can have local or global scope.

```scss
$color: blue;

.container {
    $color: red;

    color: $color;
}
```

The `.container` uses its local `$color`.

---

# 12. CSS Custom Properties vs Sass Variables

### Sass Variable

```scss
$primary-color: blue;
```

Sass variables are processed during compilation.

### CSS Variable

```css
:root {
    --primary-color: blue;
}
```

CSS variables exist at runtime in the browser.

---

# 13. Nesting

Sass allows CSS selectors to be nested.

### CSS

```css
nav {
    background: black;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline-block;
}

nav ul li a {
    color: white;
}
```

### SCSS

```scss
nav {
    background: black;

    ul {
        list-style: none;

        li {
            display: inline-block;

            a {
                color: white;
            }
        }
    }
}
```

---

# 14. Parent Selector `&`

The `&` symbol refers to the current parent selector.

```scss
.button {
    color: white;

    &:hover {
        color: red;
    }

    &:active {
        color: blue;
    }
}
```

Compiled CSS:

```css
.button {
    color: white;
}

.button:hover {
    color: red;
}

.button:active {
    color: blue;
}
```

---

# 15. Using `&` with Class Names

```scss
.button {
    &-primary {
        background: blue;
    }

    &-secondary {
        background: gray;
    }
}
```

Compiled CSS:

```css
.button-primary {
    background: blue;
}

.button-secondary {
    background: gray;
}
```

---

# 16. Nesting Properties

Sass also allows related properties to be nested.

```scss
.box {
    font: {
        family: Arial;
        size: 18px;
        weight: bold;
    }
}
```

Compiled CSS:

```css
.box {
    font-family: Arial;
    font-size: 18px;
    font-weight: bold;
}
```

---

# 17. Nesting Media Queries

Media queries can be nested inside selectors.

```scss
.container {
    width: 100%;

    @media (max-width: 768px) {
        width: 90%;
    }
}
```

This keeps responsive styles close to the selector they affect.

---

# 18. Partials

A **partial** is an SCSS file intended to be included in another Sass file rather than compiled independently.

Partial filenames begin with `_`.

Example:

```text
_variables.scss
_buttons.scss
_header.scss
```

---

# 19. `@use`

Modern Sass uses `@use` to load another Sass file.

```scss
@use "variables";
```

Example:

### `_variables.scss`

```scss
$primary-color: blue;
```

### `style.scss`

```scss
@use "variables";

body {
    color: variables.$primary-color;
}
```

---

# 20. `@forward`

`@forward` makes members from one Sass module available to another module.

Example:

```scss
@forward "variables";
@forward "buttons";
```

This is useful when organizing a larger Sass project.

---

# 21. `@import`

Older Sass code commonly used:

```scss
@import "variables";
```

However, Sass's modern module system recommends using:

```scss
@use
```

and:

```scss
@forward
```

instead of `@import`.

---

# 22. Mixins

A **mixin** is a reusable block of styles.

### Creating a mixin

```scss
@mixin center {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

### Using a mixin

```scss
.container {
    @include center;
}
```

---

# 23. Mixins with Parameters

Mixins can accept parameters.

```scss
@mixin button($background, $color) {
    background: $background;
    color: $color;
}
```

Use it:

```scss
.primary {
    @include button(blue, white);
}

.secondary {
    @include button(gray, black);
}
```

---

# 24. Default Parameters

A mixin can have a default value.

```scss
@mixin button($background: blue) {
    background: $background;
}
```

Use:

```scss
.primary {
    @include button;
}

.secondary {
    @include button(red);
}
```

---

# 25. Multiple Parameters

```scss
@mixin box($width, $height, $color) {
    width: $width;
    height: $height;
    background: $color;
}
```

Usage:

```scss
.box {
    @include box(200px, 100px, blue);
}
```

---

# 26. `@content`

Mixins can accept a block of styles using `@content`.

```scss
@mixin responsive {
    @media (max-width: 768px) {
        @content;
    }
}
```

Usage:

```scss
.container {
    width: 100%;

    @include responsive {
        width: 90%;
    }
}
```

---

# 27. Sass Functions

Sass provides built-in functions for manipulating values.

Examples include:

```scss
lighten()
darken()
rgba()
rgb()
percentage()
round()
ceil()
floor()
```

Example:

```scss
$color: blue;

.title {
    color: darken($color, 20%);
}
```

> Note: Some older global color functions have been deprecated in modern Sass in favor of module-based functions.

---

# 28. Custom Functions

You can create your own Sass functions.

```scss
@function double($number) {
    @return $number * 2;
}
```

Usage:

```scss
.box {
    width: double(100px);
}
```

Result:

```css
.box {
    width: 200px;
}
```

---

# 29. `@return`

The `@return` directive returns a value from a Sass function.

```scss
@function spacing($value) {
    @return $value * 8px;
}
```

Use:

```scss
.container {
    padding: spacing(2);
}
```

Result:

```css
.container {
    padding: 16px;
}
```

---

# 30. Sass Operators

Sass supports mathematical operators.

```scss
.container {
    width: 100px + 50px;
}
```

Result:

```css
.container {
    width: 150px;
}
```

Common operators:

```text
+
-
*
/
%
```

---

# 31. Addition

```scss
.box {
    width: 100px + 50px;
}
```

Result:

```css
.box {
    width: 150px;
}
```

---

# 32. Subtraction

```scss
.box {
    width: 200px - 50px;
}
```

Result:

```css
.box {
    width: 150px;
}
```

---

# 33. Multiplication

```scss
.box {
    width: 50px * 2;
}
```

Result:

```css
.box {
    width: 100px;
}
```

---

# 34. Division

Division in Sass has syntax considerations because `/` is also used in CSS values.

Modern Sass recommends using `math.div()` for division.

```scss
@use "sass:math";

.box {
    width: math.div(100px, 2);
}
```

Result:

```css
.box {
    width: 50px;
}
```

---

# 35. Modulo

```scss
$value: 10 % 3;
```

Result:

```text
1
```

---

# 36. String Interpolation

Interpolation allows Sass values to be inserted into selectors, property names, and strings.

Syntax:

```scss
#{$variable}
```

Example:

```scss
$name: "primary";

.button-#{$name} {
    color: blue;
}
```

Result:

```css
.button-primary {
    color: blue;
}
```

---

# 37. Lists

Sass supports lists of values.

```scss
$font-stack: Arial, Helvetica, sans-serif;
```

Lists can be separated using:

* Spaces
* Commas

Example:

```scss
$spacing: 10px 20px 30px;
```

---

# 38. Maps

Maps store key-value pairs.

```scss
$colors: (
    primary: blue,
    secondary: green,
    danger: red
);
```

Access a value using:

```scss
map.get($colors, primary);
```

Modern Sass:

```scss
@use "sass:map";

.button {
    background: map.get($colors, primary);
}
```

---

# 39. `@extend`

`@extend` allows one selector to inherit the styles of another selector.

```scss
.message {
    padding: 10px;
    border: 1px solid black;
}

.success {
    @extend .message;
    color: green;
}
```

The `.success` selector shares the styles of `.message`.

---

# 40. Placeholder Selectors

A placeholder selector starts with `%`.

```scss
%message {
    padding: 10px;
    border: 1px solid black;
}
```

Use:

```scss
.success {
    @extend %message;
    color: green;
}
```

Placeholder selectors are not emitted as standalone CSS selectors unless extended.

---

# 41. Control Directives

Sass supports programming-like control structures.

Common directives:

```text
@if
@else
@else if
@for
@each
@while
```

---

# 42. `@if`

```scss
$theme: dark;

body {
    @if $theme == dark {
        background: black;
        color: white;
    }
}
```

---

# 43. `@else`

```scss
$theme: light;

body {
    @if $theme == dark {
        background: black;
    } @else {
        background: white;
    }
}
```

---

# 44. `@else if`

```scss
$size: medium;

.box {
    @if $size == small {
        width: 100px;
    } @else if $size == medium {
        width: 200px;
    } @else {
        width: 300px;
    }
}
```

---

# 45. `@for`

The `@for` directive repeats styles.

```scss
@for $i from 1 through 3 {
    .item-#{$i} {
        width: 100px * $i;
    }
}
```

Generated selectors:

```css
.item-1
.item-2
.item-3
```

---

# 46. `@each`

`@each` loops through a list.

```scss
$colors: red, green, blue;

@each $color in $colors {
    .text-#{$color} {
        color: $color;
    }
}
```

---

# 47. `@while`

`@while` repeatedly executes code while a condition is true.

```scss
$i: 1;

@while $i <= 3 {
    .item-#{$i} {
        width: 100px * $i;
    }

    $i: $i + 1;
}
```

---

# 48. Sass Color Operations

Sass provides functions for manipulating colors.

Examples:

```scss
lighten()
darken()
mix()
rgba()
```

Example:

```scss
$primary: blue;

.button {
    background: $primary;
}
```

Color functions can be used to create variations of a base color.

---

# 49. Sass Maps and Themes

Maps can be useful for managing themes.

```scss
@use "sass:map";

$theme: (
    background: #ffffff,
    text: #222222,
    primary: #3498db
);

body {
    background: map.get($theme, background);
    color: map.get($theme, text);
}

.button {
    background: map.get($theme, primary);
}
```

---

# 50. Sass Project Structure

A larger project can organize Sass files like this:

```text
scss/
├── abstracts/
│   ├── _variables.scss
│   ├── _functions.scss
│   └── _mixins.scss
│
├── base/
│   ├── _reset.scss
│   └── _typography.scss
│
├── components/
│   ├── _buttons.scss
│   ├── _cards.scss
│   └── _navbar.scss
│
├── layout/
│   ├── _header.scss
│   └── _footer.scss
│
└── style.scss
```

This makes large stylesheets easier to manage.

---

# 51. Sass Compilation Workflow

The complete process is:

```text
Write SCSS
    ↓
Sass Compiler
    ↓
Generate CSS
    ↓
HTML links CSS
    ↓
Browser renders webpage
```

Browsers normally receive the compiled CSS, not the SCSS source.

---

# 52. Sass Advantages

* Variables reduce repetition.
* Nesting makes related styles easier to organize.
* Mixins allow reusable styles.
* Functions allow reusable calculations.
* Partials help organize large projects.
* Operators allow calculations.
* Control directives provide logic and iteration.
* Modules help structure Sass projects.
* SCSS is easy to understand for developers familiar with CSS.

---

# 53. Sass Disadvantages

* Requires a compilation step.
* Adds another tool to the development workflow.
* Excessive nesting can make CSS difficult to maintain.
* Excessive use of `@extend` can create unexpected selectors.
* Developers need to understand both Sass and CSS.
* Some older Sass features have been deprecated.

---

# 54. Important Sass Commands

### Install Sass

```bash
npm install -g sass
```

### Check version

```bash
sass --version
```

### Compile a file

```bash
sass style.scss style.css
```

### Watch a file

```bash
sass --watch style.scss style.css
```

### Watch directories

```bash
sass --watch scss:css
```

---

# 55. Quick Revision

| Concept        | Purpose                                   |
| -------------- | ----------------------------------------- |
| Variable       | Store reusable values                     |
| Nesting        | Nest selectors                            |
| `&`            | Reference parent selector                 |
| Mixin          | Reuse groups of styles                    |
| `@include`     | Use a mixin                               |
| Function       | Reusable calculation                      |
| `@return`      | Return function result                    |
| `@use`         | Load a Sass module                        |
| `@forward`     | Re-export module members                  |
| Partial        | Split Sass into reusable files            |
| `@extend`      | Share selector styles                     |
| `%placeholder` | Create extend-only selector               |
| `@if`          | Conditional logic                         |
| `@for`         | Repeat a block                            |
| `@each`        | Loop through values                       |
| `@while`       | Loop while condition is true              |
| Map            | Store key-value pairs                     |
| Interpolation  | Insert Sass values into strings/selectors |
| Operators      | Perform calculations                      |

---

# 56. Most Important Syntax

### Variable

```scss
$color: blue;
```

### Nesting

```scss
.nav {
    ul {
        li {
            color: red;
        }
    }
}
```

### Parent selector

```scss
.button {
    &:hover {
        background: blue;
    }
}
```

### Mixin

```scss
@mixin center {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

### Include

```scss
.container {
    @include center;
}
```

### Function

```scss
@function double($value) {
    @return $value * 2;
}
```

### Use

```scss
@use "variables";
```

### Extend

```scss
.success {
    @extend .message;
}
```

### Condition

```scss
@if $value > 10 {
    color: red;
}
```

### Loop

```scss
@for $i from 1 through 3 {
    .item-#{$i} {
        width: 100px;
    }
}
```

---

# 57. Final Takeaway

Sass extends CSS with features that make stylesheets easier to write and maintain.

The core concepts to remember are:

```text
Sass
│
├── Variables
├── Nesting
├── Parent Selector (&)
├── Mixins
├── Functions
├── Operators
├── Partials
├── Modules
│   ├── @use
│   └── @forward
├── @extend
├── Interpolation
├── Lists
├── Maps
├── Conditions
│   └── @if
└── Loops
    ├── @for
    ├── @each
    └── @while
```

The main purpose of Sass is to make CSS **more reusable, organized, maintainable, and powerful**, while ultimately compiling the code into standard CSS that browsers can render.

---

## Reference

**Video:** Sass Tutorial for Beginners - CSS With Superpowers

**YouTube:** https://youtu.be/_a5j7KoflTs

The video is listed in multiple web-development roadmaps as a Sass tutorial covering Sass/SCSS fundamentals.
