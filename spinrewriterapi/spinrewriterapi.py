#!/usr/bin/env python

###############################################################################
#
# Spin Rewriter API for Python 3 (PyPi)
#
# The only article spinner that truly understands the meaning of your content.
#
# With ENL technology, Spin Rewriter is the perfect tool for SEO specialists
# that need unique, human-quality content to rank higher on Google.
#
# Note: Spin Rewriter API server is using a 120-second timeout.
# Client scripts should use a 150-second timeout to allow for HTTP connection
# overhead.
#
# SDK Version    : v1.0
# Language       : Python 3
# Dependencies   : requests (https://pypi.python.org/pypi/requests/)
# Website        : https://www.spinrewriter.com/
# Contact email  : info@spinrewriter.com
#
# SDK Author     : Bartosz Wójcik (https://www.pelock.com)
#
###############################################################################

# required external package - install with "pip install requests"
import requests
from typing import Union


class SpinRewriterAPI(object):
    """Main Spin Rewriter API class. Initialize it first with your email and API key."""

    # 
    # @var string default AutoIt Obfuscator WebApi endpoint
    # 
    _api_url: str = "http://www.spinrewriter.com/action/api"

    #
    # @var dict Data to be send to the API service
    #
    _data: dict = {}

    def __init__(self, email_address: str, api_key: str):
        """Spin Rewriter API constructor, complete with authentication.
        :param email_address
        :param api_key
        """

        # make this an object (NOT an Array)
        self._data['email_address'] = email_address
        self._data['api_key'] = api_key

    def parse_bool(self, boolean_number_or_text) -> str:
        """Parse a boolean value encoded either as a boolean type, string of "true" / "false" or a number 0/1
        :param boolean_number_or_text:
        :return: output boolean value in preferred format
        :rtype: bool
        """
        result = False

        if isinstance(boolean_number_or_text, str):
            result = True if boolean_number_or_text.lower() == "true" else False
        elif isinstance(boolean_number_or_text, bool):
            result = boolean_number_or_text
        elif isinstance(boolean_number_or_text, int):
            result = True if int(boolean_number_or_text) == 1 else False

        return "true" if result is True else "false"

    def get_quota(self) -> Union[dict, bool]:
        """Returns the API Quota (the number of made and remaining API calls for the 24-hour period).
        :returns: Json encoded response in dict format or False on error
        :rtype: dict, bool
        """
        self._data['action'] = "api_quota"
        return self.make_request()

    def get_text_with_spintax(self, text: str) -> Union[dict, bool]:
        """Returns the processed text with the {first option|second option} spinning syntax.
        :param text:
        :returns: Json encoded response in dict format or False on error
        :rtype: dict, bool
        """
        self._data['action'] = "text_with_spintax"
        self._data['text'] = text
        return self.make_request()

    def get_unique_variation(self, text: str) -> Union[dict, bool]:
        """Returns one of the possible unique variations of the processed text.
        :param {string} text
        :returns: Json encoded response in dict format or False on error
        :rtype: dict, bool
        """
        self._data['action'] = "unique_variation"
        self._data['text'] = text
        return self.make_request()

    def get_unique_variation_from_spintax(self, text: str) -> Union[dict, bool]:
        """Returns one of the possible unique variations of given text that already contains valid spintax. No additional processing is done.
        :param {string} text
        :returns: Json encoded response in dict format or False on error
        :rtype: dict, bool
        """
        self._data['action'] = "unique_variation_from_spintax"
        self._data['text'] = text
        return self.make_request()

    def set_protected_terms(self, protected_terms: Union[list, str]) -> bool:
        """Sets the list of protected keywords and key phrases.
        :param {Array|string} protected_terms (array of words, comma separated list, newline separated list)
        :rtype: bool
        """
        self._data['protected_terms'] = ""

        if isinstance(protected_terms, list):
            # array of words
            for protected_term in protected_terms:
                protected_term = protected_term.strip()
                if isinstance(protected_term, str) and len(protected_term) > 2:
                    self._data['protected_terms'] += protected_term + "\n"

            self._data['protected_terms'] = self._data['protected_terms'].strip()
            return True
        elif "," in protected_terms:
            # comma separated list
            protected_terms_explode = protected_terms.split(",")
            for item in protected_terms_explode:
                protected_term = item.strip()
                if len(protected_term) > 2:
                    self._data['protected_terms'] += protected_term + "\n"

            self._data['protected_terms'] = self._data['protected_terms'].strip()
            return True

        elif "\n" in protected_terms.strip():
            # newline separated list (the officially supported format)
            protected_terms = protected_terms.strip()
            if len(protected_terms) > 0:
                self._data['protected_terms'] = protected_terms
                return True
            else:
                return False

        elif isinstance(protected_terms, str) and len(protected_terms.strip()) > 2 and len(protected_terms.strip()) < 50:
            # a single word or phrase (the officially supported format)
            self._data['protected_terms'] = protected_terms.strip()
            return True

        # invalid format
        return False

    def set_auto_protected_terms(self, auto_protected_terms: Union[bool, str, int]) -> bool:
        """Sets whether the One-Click Rewrite process automatically protects Capitalized Words outside the article's title.
        :param auto_protected_terms:
        :rtype: bool
        """
        self._data['auto_protected_terms'] = self.parse_bool(auto_protected_terms)
        return True

    def set_confidence_level(self, confidence_level: str) -> bool:
        """Sets the confidence level of the One-Click Rewrite process.
        :param confidence_level: One of the following 'low', 'medium', 'high'
        :rtype: bool
        """
        self._data['confidence_level'] = confidence_level
        return True

    def set_nested_spintax(self, nested_spintax: Union[bool, str, int]) -> bool:
        """Sets whether the One-Click Rewrite process uses nested spinning syntax (multi-level spinning) or not.
        :param nested_spintax:
        :rtype: bool
        """
        self._data['nested_spintax'] = self.parse_bool(nested_spintax)
        return True

    def set_auto_sentences(self, auto_sentences: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter rewrites complete sentences on its own.
        :param auto_sentences:
        :rtype: bool
        """
        self._data['auto_sentences'] = self.parse_bool(auto_sentences)
        return True

    def set_auto_paragraphs(self, auto_paragraphs: Union[bool, str, int]) -> bool:
        """
        Sets whether Spin Rewriter rewrites entire paragraphs on its own.
        :param auto_paragraphs:
        :rtype: bool
        """
        self._data['auto_paragraphs'] = self.parse_bool(auto_paragraphs)
        return True

    def set_auto_new_paragraphs(self, auto_new_paragraphs: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter writes additional paragraphs on its own.
        :param auto_new_paragraphs:
        :rtype: bool
        """
        self._data['auto_new_paragraphs'] = self.parse_bool(auto_new_paragraphs)
        return True

    def set_auto_sentence_trees(self, auto_sentence_trees: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter changes the entire structure of phrases and sentences.
        :param auto_sentence_trees:
        :rtype: bool
        """
        self._data['auto_sentence_trees'] = self.parse_bool(auto_sentence_trees)
        return True

    def set_use_only_synonyms(self, use_only_synonyms: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter should only use synonyms (where available) when generating spun text.
        :param use_only_synonyms:
        :rtype: bool
        """
        self._data['use_only_synonyms'] = self.parse_bool(use_only_synonyms)
        return True

    def set_reorder_paragraphs(self, reorder_paragraphs: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter should intelligently randomize the order of paragraphs and lists when generating spun text.
        :param reorder_paragraphs:
        :rtype: bool
        """
        self._data['reorder_paragraphs'] = self.parse_bool(reorder_paragraphs)
        return True

    def set_add_html_markup(self, add_html_markup: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter should automatically enrich generated articles with headings, bulpoints, etc.
        :param add_html_markup:
        :rtype: bool
        """
        self._data['add_html_markup'] = self.parse_bool(add_html_markup)
        return True

    def set_use_html_linebreaks(self, use_html_linebreaks: Union[bool, str, int]) -> bool:
        """Sets whether Spin Rewriter should automatically convert line-breaks to HTML tags.
        :param use_html_linebreaks:
        :rtype: bool
        """
        self._data['use_html_linebreaks'] = self.parse_bool(use_html_linebreaks)
        return True

    def set_spintax_format(self, spintax_format: str) -> bool:
        """Sets the desired spintax format to be used with the returned spun text.
        :param spintax_format: One of the following '{|}', '{~}', '[|]', '[spin]'
        :rtype: bool
        """
        self._data['spintax_format'] = spintax_format
        return True

    def make_request(self) -> Union[dict, bool]:
        """Sends a request to the Spin Rewriter API and return a Promise with JSON encoded response.
        :returns: Json encoded response in dict format or False on error
        :rtype: bool,dict
        """
        response = requests.post(self._api_url, data=self._data)

        # no response at all or an invalid response code
        if not response or not response.ok:
            return False

        try:
            # decode to json array
            result = response.json()

            # return original JSON response code
            return result

        # return False on error
        except ValueError:
            return False
