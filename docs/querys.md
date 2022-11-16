# QUERYS

This querys are used in PostgreSQL 14

Blog

```sql
CREATE TABLE portfolio.prod."BLOG" (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT null,
    subtitle VARCHAR(120) NOT null,
    description VARCHAR(240) NOT null,
    date TIMESTAMPTZ,
    updated TIMESTAMPTZ,
    position int
);

insert into portfolio.prod."BLOG" (
    title, 
    subtitle, 
    description, 
    "date", 
    updated, 
    "position"
    ) 
    values (
    'Hello World', 
    'Ghost in the Shell', 
    'I am glad I did my first step into the new world 🥚', 
    '2020-05-04 02:11:35', 
    '2020-05-04 02:11:35', 
    1
);

commit;
```

Projects

```sql
CREATE TABLE portfolio.prod."PROJECTS" (
    id SERIAL PRIMARY KEY,
    image VARCHAR(120) NOT null,
    cover VARCHAR(120) NOT null,
    title VARCHAR(50) NOT null,
    subtitle VARCHAR(120) NOT null,
    stack VARCHAR(240) NOT null,
    description VARCHAR(240) NOT null,
    url VARCHAR(240),
    position int
    date TIMESTAMPTZ
);

insert into portfolio.prod."PROJECTS" (
    image,
    cover,
    title, 
    subtitle,
    stack,
    description, 
    url,
    position,
    "date"
    ) 
    values (
    'lib/images/renato.jpg', 
    'lib/images/renato.jpg', 
    'BotOS',
    'Cryptocurrency bot',
    'Python, Raspberry Pi, Telegram API, Coinbase API, Bash'
    'A bot that automatically sends you personality alerts on cryptocurrency prices',
    'https://github.com/ruizdiazever/BotOS',
    1,
    '2020-05-04 02:11:35'
);
```
