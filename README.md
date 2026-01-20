# PostgreSQL



## Insert data into table

```sql
1. INSERT INTO table_name(fields, ...)
2. VALUES ('ex1', 'ex2', ...);

```

2. To select information from the columns we need
```sql
1. SELECT name, email FROM user;
```

3. Select only the information that is greater or less than the parameter we need
```sql
1. SELECT * FROM user WHERE age > 16;
```
   

4. Sorting in order and vice versa
```sql
   - SELECT * FROM user ORDER BY age;
   - SELECT * FROM user ORDER BY age DESC;
```
    
5. Find data behind similar symbols
```sql
1. SELECT * FROM user WHERE user_name ilike 'artem'
```
6. Example with join
```sql
SELECT 
    messages.id,
    messages.text,
    messages.user_id,
    messages.reactions,
    user_1112121.name,
    user_1112121.email
FROM messages
LEFT JOIN user_1112121 
    ON messages.user_id = user_1112121.id;
   
