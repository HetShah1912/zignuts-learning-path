# XHTML Notes

> **Reference:** [Tutorialspoint — XHTML Tutorial](https://www.tutorialspoint.com/xhtml/?utm_source=chatgpt.com)

---

## 1. What is XHTML?

**XHTML** stands for **EXtensible HyperText Markup Language**.

It is an XML-based version of HTML designed to make HTML documents follow the stricter rules of XML.

XHTML is very similar to HTML 4.01, but XHTML requires documents to be **well-formed** and follow XML syntax rules.

### XHTML = HTML + XML Rules

The main idea is:

```text
HTML
  +
XML rules
  =
XHTML
```

XHTML was developed by the **World Wide Web Consortium (W3C)** to help developers transition from HTML to XML.

---

# 2. Why XHTML?

XHTML provides several advantages:

* Documents must be well-formed.
* Documents can be validated using XML-based tools.
* Code follows a consistent structure.
* XHTML documents are easier for machines to parse.
* XHTML combines HTML's markup vocabulary with XML's strict syntax.
* XHTML documents can work with XML-based tools.
* It encourages cleaner and more maintainable markup.

---

# 3. XHTML Basic Structure

A minimal XHTML 1.0 document looks like this:

```html
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/TR/xhtml1"
      xml:lang="en"
      lang="en">

<head>
    <title>My XHTML Page</title>
</head>

<body>

    <h1>Hello XHTML</h1>
    <p>This is an XHTML document.</p>

</body>

</html>
```

The important structural elements are:

```text
html
 ├── head
 │    └── title
 │
 └── body
```

---

# 4. XHTML Syntax Rules

XHTML follows stricter syntax rules than traditional HTML.

The major rules are:

1. XHTML documents must have a DOCTYPE.
2. Element names must be lowercase.
3. Attribute names must be lowercase.
4. Attribute values must be quoted.
5. All elements must be properly closed.
6. Empty elements must be self-closed.
7. Elements must be properly nested.
8. Attribute minimization is not allowed.
9. The `name` attribute is replaced by `id` in cases where XHTML requires it.
10. The `language` attribute of `<script>` is deprecated.

---

# 5. DOCTYPE Declaration

The DOCTYPE tells the browser and validator which XHTML specification the document follows.

Example:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

XHTML 1.0 defines three main DTDs:

* Strict
* Transitional
* Frameset

---

# 6. XHTML 1.0 DTDs

## 6.1 XHTML 1.0 Strict

Strict is intended for documents that avoid deprecated presentation-related elements and attributes and use CSS for presentation.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

---

## 6.2 XHTML 1.0 Transitional

Transitional was designed to make migration from older HTML easier.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

---

## 6.3 XHTML 1.0 Frameset

Frameset was intended for documents using frames.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```

---

# 7. Case Sensitivity

XHTML is case-sensitive because it follows XML rules.

### Incorrect

```html
<A HREF="page.html">Page</A>
```

### Correct

```html
<a href="page.html">Page</a>
```

Both the element name and attribute name should be lowercase.

---

# 8. Closing Tags

In XHTML, elements must be properly closed.

### Incorrect

```html
<p>This is a paragraph.
```

### Correct

```html
<p>This is a paragraph.</p>
```

---

# 9. Empty Elements

HTML allows some elements to appear without closing syntax.

XHTML requires empty elements to be closed using `/>`.

### HTML

```html
<br>
<img src="image.jpg">
<hr>
```

### XHTML

```html
<br />
<img src="image.jpg" />
<hr />
```

Other examples:

```html
<input type="text" />
<meta charset="UTF-8" />
<link rel="stylesheet" href="style.css" />
```

---

# 10. Proper Nesting

Elements must be nested correctly.

### Incorrect

```html
<b>
    <i>Text
</b>
</i>
```

### Correct

```html
<b>
    <i>Text</i>
</b>
```

The element opened last must be closed first.

---

# 11. Attribute Values Must Be Quoted

### Incorrect

```html
<input type=text>
```

### Correct

```html
<input type="text" />
```

Both single and double quotes can be used:

```html
<input type="text" />
<input type='text' />
```

Double quotes are generally preferred for consistency.

---

# 12. Attribute Minimization

HTML allows attributes to be minimized:

```html
<input type="checkbox" checked>
```

XHTML does not allow this form.

### Correct XHTML

```html
<input type="checkbox" checked="checked" />
```

Examples:

| HTML       | XHTML                 |
| ---------- | --------------------- |
| `checked`  | `checked="checked"`   |
| `disabled` | `disabled="disabled"` |
| `readonly` | `readonly="readonly"` |
| `selected` | `selected="selected"` |
| `multiple` | `multiple="multiple"` |
| `required` | `required="required"` |

---

# 13. `id` Attribute

XHTML prefers the `id` attribute instead of using the old `name` attribute for element identification.

### Example

```html
<img src="logo.png" id="logo" />
```

The `id` uniquely identifies an element within a document.

---

# 14. `language` Attribute

The `language` attribute of the `<script>` element is deprecated.

### Older style

```html
<script language="JavaScript" type="text/javascript">
    document.write("Hello");
</script>
```

### XHTML style

```html
<script type="text/javascript">
    document.write("Hello");
</script>
```

The `type` attribute identifies the scripting language.

---

# 15. XHTML Comments

Comments use the same syntax as HTML:

```html
<!-- This is a comment -->
```

Comments are not displayed in the webpage.

---

# 16. XHTML Attributes

Attributes provide additional information about elements.

Example:

```html
<a href="https://example.com" id="link">
    Example
</a>
```

Here:

```text
href = "https://example.com"
id   = "link"
```

are attributes.

### XHTML Attribute Rules

* Attribute names must be lowercase.
* Attribute values must be quoted.
* Attribute minimization is not allowed.
* Attributes must be used according to the selected XHTML DTD.

---

# 17. XHTML Events

Events are actions that happen in the browser.

Examples include:

* `onclick`
* `ondblclick`
* `onmousedown`
* `onmouseup`
* `onmouseover`
* `onmousemove`
* `onmouseout`
* `onkeypress`
* `onkeydown`
* `onkeyup`
* `onload`
* `onunload`
* `onfocus`
* `onblur`
* `onchange`
* `onsubmit`
* `onreset`
* `onselect`

Example:

```html
<button type="button" onclick="alert('Hello XHTML!')">
    Click Me
</button>
```

---

# 18. Common XHTML Event Categories

## Mouse Events

```html
onclick
ondblclick
onmousedown
onmouseup
onmouseover
onmousemove
onmouseout
```

## Keyboard Events

```html
onkeydown
onkeypress
onkeyup
```

## Form Events

```html
onfocus
onblur
onchange
onsubmit
onreset
onselect
```

## Window Events

```html
onload
onunload
```

---

# 19. Element Prohibitions

XHTML has restrictions on what certain elements can contain.

Examples include:

### `<a>`

An `<a>` element must not contain another `<a>` element.

### `<form>`

A `<form>` must not contain another `<form>`.

### `<label>`

A `<label>` must not contain another `<label>`.

### `<button>`

A `<button>` cannot contain certain interactive/form elements such as:

```text
input
select
textarea
label
button
form
fieldset
iframe
```

### `<pre>`

A `<pre>` element has restrictions on elements such as:

```text
img
object
big
small
sub
sup
```

These restrictions help XHTML documents remain structurally valid.

---

# 20. XHTML vs HTML

| Feature                | HTML                         | XHTML                             |
| ---------------------- | ---------------------------- | --------------------------------- |
| Case sensitivity       | Generally not case-sensitive | Case-sensitive                    |
| Closing tags           | Some may be omitted          | Required                          |
| Empty elements         | `<br>`                       | `<br />`                          |
| Attribute values       | Can sometimes be unquoted    | Must be quoted                    |
| Attribute minimization | Allowed                      | Not allowed                       |
| Nesting                | Browsers may tolerate errors | Must be properly nested           |
| XML rules              | No                           | Yes                               |
| Well-formedness        | Not strictly required        | Required                          |
| DOCTYPE                | Depends on HTML version      | Required for XHTML DTD validation |

XHTML documents must be **well-formed**, meaning elements must be correctly nested and closed.

---

# 21. Well-Formed XHTML

A well-formed XHTML document follows XML syntax rules.

### Example

```html
<p>
    This is
    <strong>well-formed</strong>
    XHTML.
</p>
```

The structure is:

```text
<p>
    <strong>...</strong>
</p>
```

Correct opening and closing order is important.

---

# 22. XHTML 1.1

XHTML 1.1 is a stricter and more modular version of XHTML.

It removes deprecated elements and attributes and is based on XHTML modules.

The main goal was to create a more modular XHTML document type that could be used across different devices.

---

# 23. XHTML 1.1 Modules

XHTML 1.1 is organized into modules.

Important modules include:

* Structure Module
* Text Module
* Hypertext Module
* List Module
* Object Module
* Presentation Module
* Edit Module
* Bidirectional Text Module
* Forms Module
* Table Module
* Image Module
* Client-side Image Map Module
* Server-side Image Map Module
* Style Attribute Module
* Style Element Module
* Link Module
* Base Module
* Scripting Module
* Target Module
* Events Module
* Metainformation Module

### Structure Module

Defines:

```text
html
head
body
title
```

### Text Module

Includes elements such as:

```text
p
h1-h6
br
strong
em
code
pre
blockquote
q
span
div
```

---

# 24. Character Entities

Special characters should be represented using character references when necessary.

Examples:

```html
&lt;
&gt;
&amp;
&quot;
&apos;
```

Meaning:

| Entity   | Character |
| -------- | --------- |
| `&lt;`   | `<`       |
| `&gt;`   | `>`       |
| `&amp;`  | `&`       |
| `&quot;` | `"`       |
| `&apos;` | `'`       |

---

# 25. CDATA

When XHTML contains JavaScript or CSS content, XML parsing rules can affect characters such as `<` and `&`.

CDATA can be used to tell the XML parser that the enclosed content should be treated as character data.

Example:

```html
<script type="text/javascript">
//<![CDATA[

    function hello() {
        alert("Hello XHTML!");
    }

//]]>
</script>
```

CDATA is particularly relevant when XHTML is processed as XML.

---

# 26. XHTML and CSS

XHTML handles the **structure** of a webpage, while CSS handles its **presentation**.

Example:

```html
<p class="message">
    Hello XHTML
</p>
```

CSS:

```css
.message {
    font-size: 20px;
}
```

The XHTML provides structure and CSS provides presentation.

---

# 27. XHTML and JavaScript

JavaScript can be used with XHTML for client-side behavior.

Example:

```html
<script type="text/javascript">
//<![CDATA[
    function showMessage() {
        alert("Hello XHTML!");
    }
//]]>
</script>

<button type="button" onclick="showMessage()">
    Click Me
</button>
```

---

# 28. XHTML Validation

Validation checks whether an XHTML document follows the rules defined by its DTD.

A validator can detect problems such as:

* Missing closing tags
* Incorrect nesting
* Invalid elements
* Invalid attributes
* Incorrect DOCTYPE
* Incorrect XHTML syntax

Tutorialspoint recommends using the **W3C Validator** for checking XHTML validity.

---

# 29. Why Validate XHTML?

Validation helps ensure:

* Correct markup
* Better consistency
* Fewer structural errors
* Compliance with the selected XHTML specification
* Easier maintenance
* Better interoperability with XML-aware tools

---

# 30. Converting HTML to XHTML

Existing HTML can be converted to XHTML by applying XHTML's stricter rules.

### Step 1 — Add DOCTYPE

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

### Step 2 — Add XHTML namespace

```html
<html xmlns="http://www.w3.org/TR/xhtml1">
```

### Step 3 — Use lowercase elements

```html
<h1>Hello</h1>
```

instead of:

```html
<H1>Hello</H1>
```

### Step 4 — Use lowercase attributes

```html
<a href="page.html">
```

### Step 5 — Quote attributes

```html
<input type="text" />
```

### Step 6 — Close all elements

```html
<p>Hello</p>
```

### Step 7 — Close empty elements

```html
<br />
<img src="image.jpg" alt="Image" />
```

### Step 8 — Properly nest elements

```html
<strong>
    <em>Text</em>
</strong>
```

### Step 9 — Remove attribute minimization

```html
<input type="checkbox" checked="checked" />
```

### Step 10 — Handle scripts and styles appropriately

Use CDATA where required when XHTML is being treated as XML.

These are the main conversion steps summarized by Tutorialspoint.

---

# 31. Final Summary

XHTML is an XML-based reformulation of HTML. Its main purpose was to make web documents follow stricter, well-formed XML rules.

The most important XHTML concepts are:

```text
XHTML
├── Introduction
├── Syntax
│   ├── DOCTYPE
│   ├── Lowercase elements
│   ├── Lowercase attributes
│   ├── Quoted attributes
│   ├── Closing tags
│   ├── Self-closing elements
│   ├── Proper nesting
│   └── No attribute minimization
│
├── Doctypes
│   ├── Strict
│   ├── Transitional
│   └── Frameset
│
├── Attributes
├── Events
├── XHTML vs HTML
├── XHTML 1.1
│   └── Modules
├── Tips & Tricks
├── Validation
└── HTML → XHTML Conversion
```

The core idea is:

> **XHTML = HTML vocabulary written according to XML's stricter rules.**

---

## Reference

**Primary Reference:**
[Tutorialspoint XHTML Tutorial](https://www.tutorialspoint.com/xhtml/?utm_source=chatgpt.com)

**Tutorial sections covered:** Introduction, Syntax, XHTML vs HTML, Doctypes, Attributes, Events, XHTML 1.1, Tips & Tricks, Validations, and Summary.
