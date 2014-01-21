gmailer
=======

A simple tool to send test emails using a Gmail or Google Apps account.

## Usage

    python gmailer.py USER PASSWORD RECIPIENT FILE [--subject SUBJECT]

Where:

* USER is the email address of the Google account to be used to send emails (e.g. me@gmail.com).
* PASSWORD is the password used to authenticate as the Google account.
* RECIPIENT is the email address of the user to send the email to. It also supports a comma-separated list of values.
* FILE is the location of the file containing the HTML body of the email to send.
* SUBJECT is the optional email subject. If not provided, the default value will be "Gmailer test - DATETIME"

## Examples

Login to Google as `me@gmail.com` (password `abcde123`) and send the HTML content from `./templates/goto_action.html` to `you@gmail.com`: 

    python gmailer.py me@gmail.com abcde123 you@gmail.com ./templates/goto_action.html

Same as before, but with custom subject line:

    python gmailer.py me@gmail.com abcde123 you@gmail.com ./templates/goto_action.html --subject "Sample email from Gmailer"