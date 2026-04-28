# BB Codes Reference Guide for PHCorner

This guide is based on the official help page: https://phcorner.org/help/bb-codes/

## About BB Codes
BB Codes (Bulletin Board Codes) are a lightweight markup language used to format forum posts. They are a safer alternative to HTML, using tags within square brackets `[ ]` to apply styling or embed content.

## Important Notes
- Most tags require both an opening `[tag]` and a closing `[/tag]` tag.
- Some tags accept options via an equals sign `=` (e.g., `[tag=value]`).
- Improperly nested or unclosed tags may result in formatting not being applied.

---

## 1. Text Formatting

### Basic Formatting
| Tag | Description | Example |
| :-- | :--- | :--- |
| `[B]` | Bold | `[B]bold text[/B]` → **bold text**[reference:0] |
| `[I]` | Italic | `[I]italic text[/I]` → *italic text*[reference:1] |
| `[U]` | Underline | `[U]underlined text[/U]` → <u>underlined text</u>[reference:2] |
| `[S]` | Strikethrough | `[S]struck-through text[/S]` → ~~struck-through text~~[reference:3] |

### Advanced Formatting
| Tag | Description | Example |
| :-- | :--- | :--- |
| `[COLOR=value]` | Changes text color | `[COLOR=red]red text[/COLOR]` → <span style="color:red">red text</span>[reference:4] |
| `[FONT=name]` | Changes font face | `[FONT=Courier New]Courier New font[/FONT]`[reference:5] |
| `[SIZE=size]` | Changes text size (1 to 7) | `[SIZE=7]big text[/SIZE]`[reference:6] |
| `[HEADING=level]` | Creates headings (levels 1-3) | `[HEADING=1]Heading 1[/HEADING]`[reference:7] |
| `[PLAIN]` | Disables BB code parsing | `[PLAIN]Not [B]bold[/B][/PLAIN]` → Not `[B]bold[/B]`[reference:8] |

---

## 2. Links, Media, and Images

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[URL]` or `[URL=url]` | Creates a hyperlink | `[URL]https://example.com[/URL]` or `[URL=https://example.com]Example[/URL]`[reference:9] |
| `[EMAIL]` or `[EMAIL=address]` | Creates a mailto: link | `[EMAIL=name@example.com]Email Me[/EMAIL]`[reference:10] |
| `[USER=ID]` | Links to a user's profile | `[USER=1]Username[/USER]`[reference:11] |
| `[IMG]` | Embeds an image | `[IMG]https://example.com/image.png[/IMG]`[reference:12] |
| `[MEDIA=site]` | Embeds media from sites like YouTube | `[MEDIA=youtube]kQ0Eo1UccEE[/MEDIA]`[reference:13] |
| `[ATTACH]` | Inserts a post attachment | `[ATTACH]123[/ATTACH]` or full size `[ATTACH=full]123[/ATTACH]`[reference:14] |
| `[DOWNLOAD="url"]` | Creates a download button | `[DOWNLOAD="More examples here..."] /t/1430977/ [/DOWNLOAD]`[reference:15] |

---

## 3. Lists and Tables

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[LIST]` | Creates a bullet list | `[LIST] [*]Item 1 [*]Item 2 [/LIST]`[reference:16] |
| `[LIST=1]` | Creates a numbered list | `[LIST=1] [*]Entry 1 [*]Entry 2 [/LIST]`[reference:17] |
| `[TABLE]`, `[TR]`, `[TD]`, `[TH]` | Creates a table | See example[reference:18] |

---

## 4. Alignment and Indentation

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[LEFT]` | Left-aligns text | `[LEFT]Left-aligned[/LEFT]`[reference:19] |
| `[CENTER]` | Centers text | `[CENTER]Centered[/CENTER]`[reference:20] |
| `[RIGHT]` | Right-aligns text | `[RIGHT]Right-aligned[/RIGHT]`[reference:21] |
| `[INDENT]` | Indents text (nestable) | `[INDENT]Indented text[/INDENT]` or `[INDENT=2]More indented[/INDENT]`[reference:22] |

---

## 5. Quoting and Spoilers

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[QUOTE]` | Quotes text from another source | `[QUOTE]Quoted text[/QUOTE]`[reference:23] |
| `[QUOTE=Author]` | Attributed quote | `[QUOTE=A person]Something they said[/QUOTE]`[reference:24] |
| `[SPOILER]` | Hides spoiler content until clicked | `[SPOILER]Hidden text[/SPOILER]`[reference:25] |
| `[ISPOILER]` | Inline spoiler text within a sentence | `Click the [ISPOILER]word[/ISPOILER] to reveal.`[reference:26] |

---

## 6. Code Display

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[CODE]` | Block code display with syntax highlighting | `[CODE]General code[/CODE]`[reference:27] |
| `[CODE=lang]` | Block code with specified language syntax | `[CODE=php]echo $hello . ' world';[/CODE]`[reference:28] |
| `[ICODE]` | Inline code without syntax highlighting | `[ICODE]inline code[/ICODE]`[reference:29] |
| `[ICODE=rich]` | Inline code that supports simple formatting | `[ICODE=rich][COLOR=red]Rich[/COLOR] code[/ICODE]`[reference:30] |

---

## 7. Galleries

| Tag | Description | Example |
| :-- | :--- | :--- |
| `[GALLERY=option]` | Embeds gallery media items or albums | `[GALLERY=media, X]Gallery BB Code[/GALLERY]`[reference:31] |

---
