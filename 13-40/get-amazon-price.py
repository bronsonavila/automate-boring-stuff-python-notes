#! /usr/bin/env python3

import sys
import pyperclip
import bs4
import requests


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Only works on products with a '#newOfferAccordionRow' element:
    elements = soup.select(
        """#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 >
        div > div.a-column.a-span4.a-text-right.a-span-last >
        span.a-size-medium.a-color-price.header-price"""
    )
    return elements[0].text.strip()


if len(sys.argv) > 1:
    # Set product URL if included as an argument:
    productUrl = sys.argv[1]
else:
    # Get product URL from the user's clipboard if no argument provided:
    productUrl = pyperclip.paste()


price = getAmazonPrice(productUrl)

print('The price is ' + price)
