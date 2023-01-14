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
    - **YOU SHOULD NOT USE YOUR PRIMARY EMAIL ADDRESS TO MITIGATE THE CHANCES OF ANYTHING GETTING MESSED UP**
    - Forward the muster emails from your primary email address to the newly created Gmail account
2. Setup Gmail API with your new Gmail account
3. Create Twilio Account 
4. 


# Assumptions 
The code in this repository was made using the following assumptions: 
- The muster email subject is "Virtual Muster" 
- Reminders are sent Monday through Friday
- Holidays are not considered


