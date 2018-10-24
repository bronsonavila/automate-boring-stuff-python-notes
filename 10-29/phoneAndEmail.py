#! /usr/bin/env python3

import re
import pyperclip

# Create regex for phone numbers:

phoneRegex = re.compile(r'''
# Valid phone number formats:
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?    # Area code (optional)
(\s|-)                        # First separator
\d\d\d                        # First 3 digits
-                             # Separator
\d\d\d\d                      # Last 4 digits
((ext(\.)?\s|x)               # Extension word (optional)
    (\d{2,5}))?               # Extension number (optional)
)
''', re.VERBOSE)

# Create regex for email addresses:

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+   # Name part
@                 # @ symbol
[a-zA-Z0-9_.+]+   # Domain name part
''', re.VERBOSE)

# Get text from clipboard:

text = pyperclip.paste()

# Extract phone numbers and email addresses from text:

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy extracted phone numbers and email addresses to clipboard:

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
