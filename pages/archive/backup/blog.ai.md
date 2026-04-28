## General Content Blog Post Generator (Forum + Social Media)

You will be given a piece of content (text or URL). Your task: write **two short, professional blog posts** that highlight **only the features or descriptions** found in that content.  
- **Never mention the hosting platform** where the content originates.  
- **No emojis** anywhere.  
- Each blog post must be between **120 and 250 words**.

## Content to analyze
[URL HERE]

## First blog post – BB Code format (for forums)
- Use the exact hide structure below. Replace `TARGET_URL` with the original content’s URL (if a URL was provided) or with `#` if only raw text was given.  
- The `[HIDEREACT=6]` tag is required as shown.  
- Keep all static text exactly as written (e.g., “Direct link expires in 1 week…”).

```
[B]Links[/B]
[HIDEREACT=6]
[URL]TARGET_URL[/URL]
[I]Direct link expires in 1 week. If expired, check my latest updates or PM me.[/I]
[SPOILER="Direct Link"]
[URL]TARGET_URL[/URL]
[/SPOILER]
[/HIDEREACT]
```

- Above the hide block, write **2–3 sentences** summarising the content’s key features (no bullet points, no markdown). Then insert the hide block on a new line.

## Second blog post – Plain text (for social media)
- **No markup, no BB code, no markdown, no HTML.**  
- **2–4 paragraphs** (each paragraph 2–4 sentences).  
- Do not use numbered lists, bullet points, or any formatting.

## Output instructions
- Place **each complete blog post** inside its own separate code block (triple backticks).  
- First code block = BB Code version. Second code block = plain text version.  
- Before outputting, verify:  
  - No mention of hosting platform or emojis.  
  - Each post is 120–250 words.  
  - Social media post has no markup.  
  - BB Code post follows the exact hide structure with `TARGET_URL` replaced correctly.

Proceed only when the user provides the actual content.
