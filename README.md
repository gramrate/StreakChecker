# Preface

I would like to dedicate this project to Alisa Epifanova for motivation during the development process.

___

# Telegram Streak Checker

Telegram Streak Cheker - A bot that implements the streak system in Telegram.

If you text back and forth a lot, running this would be a great solution. The bot will tell you how many days in a row
you are texting.

___

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_ID` - Your API ID, a unique identifier for your app in the cloud service.  
`API_HASH` - API Hash, a secret key used in conjunction with the API ID.  
`PHONE_NUMBER` - Phone number associated with your cloud account.  
`CLOUD_PASSWORD` - Cloud password if enabled for additional security.

___

## Constant Variables

```
src/config/consts.py
```

To run this project, you will need to add the following сonstant variables to your consts.py file

`chat_check` - List of unique telegram-ids, those in the chat with whom the bot will be working
`user_id` - Your unique telegram-id is required for correct work
`database` - The path to your database, by default `database = 'src/db/database.db'`
`session_path` - The path to your session, by default `session_path = 'src/streak-checker-session'`

___

## Deployment

To deploy this project run

Install poetry as python dependency management

```bash
  pip3 install poetry
```

Install dependencies

```bash
  poetry install
```

Run ENV

```bash
  poetry shell
```

Start bot

```bash
  poetry run python3 -m src/main
```

___

## Features

- while nothing

___

## Special Thanks

- [Zoom](https://github.com/Zoom-Developer/) - for help in writing the structure.
- [Vanya](https://github.com/stupidcabbage) - I stole README from him.
