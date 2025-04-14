## Telegram_bot для транслитерации ФИО на латиницу




### 1) Склонируйте репозиторий

### 2)Соберите Docker-образ:
 ```docker build -t telegram-bot .```

### 3) Запустите контейнер (подставьте свой токен)
```docker run -d --name bot -e TOKEN='ваш_токен_бота' telegram-bot```

### Дополнительные команды

Просмотр логов:
```docker logs bot```


Остановка бота:
```docker logs bot```

Запуск после остановки

```docker start bot```




