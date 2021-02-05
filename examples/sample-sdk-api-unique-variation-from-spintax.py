###############################################################################
#
# Spin Rewriter API for Python >= 3 (PyPi) example of how to
# generate unique variation from the provided spintax template.
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

#
# Spin Rewriter API settings - authentication:
#

# your Spin Rewriter email address goes here
email_address = "test@example.com"

# your unique Spin Rewriter API key goes here
api_key = "1ab234c#d5e67fg_h8ijklm?901n234"

# Authenticate yourself.
spinrewriter_api = SpinRewriterAPI(email_address, api_key)

# (optional) Sets whether Spin Rewriter should only use synonyms (where available) when generating spun text.
spinrewriter_api.set_use_only_synonyms(False)

# (optional) Sets whether Spin Rewriter should intelligently randomize the order of paragraphs
# and lists when generating spun text.
spinrewriter_api.set_reorder_paragraphs(False)

# (optional) Sets whether Spin Rewriter should automatically enrich generated articles with headings, bulpoints, etc.
spinrewriter_api.set_add_html_markup(False)

# (optional) Sets whether Spin Rewriter should automatically convert line-breaks to HTML tags.
spinrewriter_api.set_use_html_linebreaks(False)

#
# IMPORTANT:
#
# When using the action 'get_unique_variation_from_spintax', your text
# should already contain valid {first option|second option} spinning syntax.
#
# No additional processing is done on your text, Spin Rewriter simply
# provides one of the unique variations of the given (already spun) text.
#
text = "John {will|will certainly} {book|make a reservation for} a {room|hotel suite}."

# Make the actual API request and save the response as a native JSON dictionary or False on error
result = spinrewriter_api.get_unique_variation_from_spintax(text)

if result:
    print("Spin Rewriter API response")
    print(result)
else:
    print("Spin Rewriter API error")