###############################################################################
#
# Spin Rewriter API for Python >= 3 (PyPi) example of how to check
# the available quota for your account.
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

# Make the actual API request and save the response as a native JSON dictionary or False on error
result = spinrewriter_api.get_quota()

if result:
    print("Spin Rewriter API response")
    print(result)
else:
    print("Spin Rewriter API error")
