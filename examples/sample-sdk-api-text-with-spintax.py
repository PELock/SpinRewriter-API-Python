###############################################################################
#
# Spin Rewriter API for Python >= 3 (PyPi) basic usage example.
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
#protected_terms =  [ "John", "Douglas", "Adams", "then" ]

spinrewriter_api.set_protected_terms(protected_terms)

# (optional) Set whether the One-Click Rewrite process automatically protects Capitalized Words outside the article's title.
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

# (optional) Set the desired spintax format to be used with the returned spun text.
spinrewriter_api.set_spintax_format("{|}")

# Make the actual API request and save the response as a native JSON object.
text = "John will book a room. Then he will read a book by Douglas Adams."

# Make the actual API request and save the response as a native JSON dictionary or False on error
result = spinrewriter_api.get_text_with_spintax(text)

if result:
    print("Spin Rewriter API response")
    print(result)
else:
    print("Spin Rewriter API error")
