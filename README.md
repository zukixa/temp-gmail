# temp-gmail-api

## Features

- **Create Temporary Emails:** Generate disposable emails quickly.
- **Fetch Messages:** Retrieve emails for the created email account.
- **Search by Keyword:** Efficiently search through the inbox to find relevant messages.
- **Session Management:** Handles browser-like sessions and cookies automatically.

## Installation

To use this module, ensure you have Python installed on your machine along with the `curl_cffi` package. You can install the required package using pip:

```bash
pip install curl-cffi
```

## Usage

Here's a basic example of how to use the GMail class from the module:

```py
from temp-gmail import GMail
# Creating an instance of the GMail class

gmail_instance = GMail()

# Creating a temporary email

email_address = gmail_instance.create_email()
print("Generated Email:", email_address)

# Loading the email list for the new email

emails = gmail_instance.load_list()
print("Emails:", emails)

# Example: Check for new items with a specific keyword

message_info = gmail_instance.check_new_item("welcome")
print("Message Details:", message_info)
```

## Methods

Here is a brief overview of some of the methods included in the GMail class:

```diff
- create_email()
> No parameters required.
> Returns the generated email address.
- load_list()
> No parameters required.
> Fetches all messages for the current email account.
- load_item(message_id)
> message_id: ID of the message to retrieve.
> Returns the contents of the specified message.
- check_new_item(keyword)
> keyword: The keyword to search for in messages.
> Searches all messages for the keyword and returns the first message ID with a match.
```

## Dependencies

curl_cffi: A Python package that provides a way to interact with curl via CFFI.
