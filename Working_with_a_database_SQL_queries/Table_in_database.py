import psycopg2

PGHOST = 'ep-silent-sky-agdcdira-pooler.c-2.eu-central-1.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = 'npg_S5xkYCgLMW3m'
PORT = 5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS user_1112121(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(20) NOT NULL
                );
            CREATE TABLE IF NOT EXISTS messages(
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP NOT NULL,
                text VARCHAR(50),
                user_id INT NOT NULL,
                reactions INT,
                CONSTRAINT fk_user
                    FOREIGN KEY (user_id)
                    REFERENCES user_1112121(id)
                    ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS settings(
                    language VARCHAR(100) NOT NULL,
                    users_settings VARCHAR(100) NOT NULL
                    
            )
        """
        cursor.execute(query)
