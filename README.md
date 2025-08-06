## About
Simple email notifier about AD password expiration

Working as a script on Windows with AD Tools installed

## Installation
First of all - install AD tools, or use this script on a Windows AD Server

To install you need to clone rep and create .env file and fill it, that's all

```cmd
clone https://github.com/UselessHumster/password_expiration_alarms.git
uv sync
cp .env_template .env
notepad .env
```

After filling .env - build and install project, and you are good to go
```
uv build
uv tools install 
uv run notifier
```


## !Warning
Installation not tested, I wrote it just for myself, and it is possible that I forgot some steps
