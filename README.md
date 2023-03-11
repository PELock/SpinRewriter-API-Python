# Spin Rewriter - Article Rewriter with ENL Semantic Spinning (for Python 3 and PyPi & pip)

The only article spinner that truly understands the meaning of your content.

With ENL technology, Spin Rewriter is the perfect tool for SEO specialists that need unique, human-quality content to rank higher on Google.

[![How to use Spin Rewriter Tutorial](https://img.youtube.com/vi/hIZgag6ChhA/0.jpg)](https://www.youtube.com/watch?v=hIZgag6ChhA)

## Why Spin Rewriter? Start ranking higher, for more keywords.

You already know that quality unique content does wonders for your Google rankings. You also know that such content takes ages to write — or it costs you an arm and two legs if you hire someone to write it for you.

Spin Rewriter saves you both time and money. It takes a single article and turns it into dozens of 100% unique, human-quality articles. All these unique articles will let you rank higher, and for more profitable keywords.

## What are the benefits of our API?

As a user, Spin Rewriter API allows you to use the ENL Semantic Spinning technology inside other compatible software products.

This means that you can — for example — spin your articles using our amazing technology directly inside your favorite article distribution software.

You never have to load the Spin Rewriter website and interrupt your workflow by spinning your article here, and then pasting it to your article distribution software. You can use Spin Rewriter directly from compatible desktop software products, online services, WordPress plugins, etc.

As a developer, you can use the amazing Spin Rewriter technology inside your own application or service. Whenever you need to rewrite a block of text, simply send it to our servers and Spin Rewriter will do all the hard work for you. We developed our algorithms — you make the most of them!

#### Installation (for Python 3)

Preferred way of WebApi interface installation is via [pip](https://pypi.org/project/pip/).

Run:

```
pip install spin-rewriter-api
```

or 

```
python3 -m pip install spin-rewriter-api
```

And then add this import to your source code:

```python
from spinrewriterapi import SpinRewriterAPI
```

Installation package is available at https://pypi.org/project/spin-rewriter-api/


```python
###############################################################################
#
# Spin Rewriter API for Python >= 3 (PyPi) example of how to
# generate unique variation.
#
# Note: Spin Rewriter API server is using a 120-second timeout.
# Client scripts should use a 150-second timeout to allow for HTTP connection
# overhead.
#
# SDK Version    : v1.0
# Language       : Python 3
# Dependencies   : spin-rewriter-api
# Website        : https://www.spinrewriter.com/
# Contact email  : info@spinrewriter.com
#
# SDK Author     : Bartosz Wójcik (https://www.pelock.com)
#
###############################################################################

#
# include Spin Rewriter API module
#
from spinrewriterapi import SpinRewriterAPI

# your Spin Rewriter email address goes here
email_address = "test@example.com"

# your unique Spin Rewriter API key goes here
api_key = "1ab234c#d5e67fg_h8ijklm?901n234"

# Spin Rewriter API settings - authentication:
spinrewriter_api = SpinRewriterAPI(email_address, api_key)

#
# (optional) Set a list of protected terms.
# You can use one of the following formats:
# - protected terms are separated by the '\n' (newline) character
# - protected terms are separated by commas (comma-separated list)
# - protected terms are stored in a Python [] array
#
protected_terms = "John, Douglas Adams, then"
#protected_terms = "John\nDouglas\nAdams\nthen"
#protected_terms = ["John", "Douglas", "Adams", "then"]

spinrewriter_api.set_protected_terms(protected_terms)

# (optional) Set whether the One-Click Rewrite process automatically protects
# Capitalized Words outside the article's title.
spinrewriter_api.set_auto_protected_terms(False)

# (optional) Set the confidence level of the One-Click Rewrite process.
spinrewriter_api.set_confidence_level("medium")

# (optional) Set whether the One-Click Rewrite process uses nested spinning syntax (multi-level spinning) or not.
spinrewriter_api.set_nested_spintax(True)

# (optional) Set whether Spin Rewriter rewrites complete sentences on its own.
spinrewriter_api.set_auto_sentences(False)

# (optional) Set whether Spin Rewriter rewrites entire paragraphs on its own.
spinrewriter_api.set_auto_paragraphs(False)

# (optional) Set whether Spin Rewriter writes additional paragraphs on its own.
spinrewriter_api.set_auto_new_paragraphs(False)

# (optional) Set whether Spin Rewriter changes the entire structure of phrases and sentences.
spinrewriter_api.set_auto_sentence_trees(False)

# (optional) Sets whether Spin Rewriter should only use synonyms (where available) when generating spun text.
spinrewriter_api.set_use_only_synonyms(False)

# (optional) Sets whether Spin Rewriter should intelligently randomize the order of paragraphs and lists when
# generating spun text.
spinrewriter_api.set_reorder_paragraphs(False)

# (optional) Sets whether Spin Rewriter should automatically enrich generated articles with headings, bulpoints, etc.
spinrewriter_api.set_add_html_markup(False)

# (optional) Sets whether Spin Rewriter should automatically convert line-breaks to HTML tags.
spinrewriter_api.set_use_html_linebreaks(False)

# Make the actual API request and save the response as a native JSON object.
text = "John will book a room. Then he will read a book by Douglas Adams."

# Make the actual API request and save the response as a native JSON dictionary or False on error
result = spinrewriter_api.get_unique_variation(text)

if result:
    print("Spin Rewriter API response")
    print(result)
else:
    print("Spin Rewriter API error")
```

## Need help, have some questions?

For more information visit our site https://www.spinrewriter.com/

Bartosz Wójcik

* Visit my site at — https://www.pelock.com
* Twitter — https://twitter.com/PELock
* GitHub — https://github.com/PELock