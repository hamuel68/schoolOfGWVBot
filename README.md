# School of GWV Assistant Discord Bot

This repo contains the source code for a discord bot created for the [School of GWV](https://discord.gg/k54fFHz45a), a community discord server to help new players learn about Counter-Strike.

  

## Overview

The purpose of this bot is to manage help requests from students in the discord server. It is purpose-built for this server only.

  

Students should be able to submit a help request in existing text channels. After submitting a request (max 1 per channel at any time), it should post a notification to an admin-only channel and tag GWV (or other instructors) so they can easily view all open requests and respond to them.

  

Other potential features could be added in the future, such as integration with the chatGPT API, for times where no instructor is available.

  

## Prerequisites
1. Python is installed, preferred [version 3.11.5](https://www.python.org/downloads/release/python-3115/) (Note: later versions currently do not work as of 11/11/2023)

  

## Installation Instructions
These are installation instructions for if you want to use this code in your own bot.

 1. Navigate to https://discord.com/developers/applications and create a new application
 2. Keep a note of your token, you will need it to deploy the bot
 3. Give the bot administrator privilleges for it to work correctly
 4. Now open the project in your IDE and open the terminal in the root folder, run `pip install virtualenv`. Keep the console open for now.
 5. In the same console, run `virtualenv .venv`. This will create a virtual environment for your python code to run in. You should see a folder .venv in your root directory.
 6. Make sure to select your interpreter for the virtual instance of python
 7. At this point, you should restart your terminal so that you are installing all dependencies in the correct environment
 8. Run `pip install discord.py[voice]`in the terminal, followed by `pip install python-dotenv`. This will allow us to use the token we created at the start.
 9. Create a file in the root directory called `.env`
 10. Open this file and write 
> DISCORD_API_TOKEN='put your token here'
 11.  Create a folder `logs`in the root directory and a file inside it called `Logs.log`(remember correct capitalisation)
 12. Finally, run main and your bot should appear online for whichever server(s) you have added it to.
