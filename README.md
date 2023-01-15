# Daily Muster Alert

![reminder-status](https://github.com/ethancboone/muster-alert/actions/workflows/check.yml/badge.svg)

# Disclaimer 
This tool is not a replacement for manually checking the status of your Google Forms muster response. It is still your responsibility to ensure that you have mustered every morning. 
# About
This respository is designed to provide updated notificiations if you have not completed the daily Google Forms muster. 

This is accomplished using the following tools: 
- Gmail API
- Twilio

## [Gmail API](https://developers.google.com/gmail/api/guides)
This is used to interact with a gmail email address. Using this API, you're able to interact with your gmail account in several ways. These include reading your messages, reading your labels, and writing and sending emails. 

## [Twilio](https://www.twilio.com)
The Twilio API is used to send updates regarding your muster status. Use of this repository only requires the free tier. 

With Twilio, you're able to create SMS and automated calls to numbers of your choice. 

# Getting Started
If you would also utilize this tool, you will have to set up a few different tools. The overall steps for this project are captured below: 

1. Setup new Gmail account
    - *YOU SHOULD NOT USE YOUR PRIMARY EMAIL ADDRESS TO MITIGATE THE CHANCES OF ANYTHING GETTING MESSED UP*
    - Forward the muster emails from your primary email address to the newly created Gmail account

2. Setup Gmail API with your new Gmail account
    - Follow the directions in the [Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)

3. Create Twilio Account

4. Clone this repository

5. Locally add the credentials.json file

6. Run the following command:
    ```
    python src/inbox_check.py
    ```

7. Ensure that a token.json file has been created. Once its created, commit to the repository. 

    ```
    git add . 
    git commit -m "My Initial Commit"
    git push
    ```

    - Validate that the credentials.json and token.json files are not pushed into the repository. 

8. Added sensitive information to [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets). These are all added under Actions. 
    - The following secrets will need to be added, with the specific naming convention. Format is Required_Name: Description. 
        - MY_PHONE_NUMBER: Phone number you would like to recieve notifications on. 
        - TWILIO_PHONE_NUMBER: Phone number that is created from your Twilio account
        - TWILIO_SID: SID from your Twilio account
        - TWILIO_TOKEN: Token from your Twilio account
        - CREDENTIALS: The contents of the credentials.json file from the Gmail API. This is all the contents of the json file, including brackets. 
        - TOKEN: The contents of the token.json file from the Gmail API. This is all the contents of the json file, including brackets.


# Assumptions 
The code in this repository was made using the following assumptions: 
- The muster email subject is "Virtual Muster" 
- Reminders are sent Monday through Friday
- Holidays are not considered


