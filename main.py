# -*- coding: utf-8 -*-

"""Simple command-line tool for Google Image Custom Search.
Command-line application that does a search and download.
"""

__author__ = 'kakkoyun@gmail.com (Kemal Akkoyun)'

import os
import pprint

from google_image_search_service import GoogleImageSearchService


def main():
    API_KEY = os.environ['GOOGLE_API_KEY']
    ENGINE_ID = os.environ['GOOGLE_SEARCH_ENGINE_ID']

    service = GoogleImageSearchService(API_KEY, ENGINE_ID)
    result = service.image_search('arnolfini paradoy')

    pprint.pprint(result)

if __name__ == '__main__':
    main()