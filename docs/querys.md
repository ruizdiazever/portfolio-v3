# QUERYS

This querys are used in PostgreSQL 14

Blog

```sql
CREATE TABLE portfolio.prod.blog (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT null,
    subtitle VARCHAR(120) NOT null,
    description VARCHAR(240) NOT null,
    date TIMESTAMPTZ,
    updated TIMESTAMPTZ,
    position int
);
commit;
```

```sql
insert into portfolio.prod.blog (
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
```
