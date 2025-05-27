from mysql.connector import pooling
from mysql.connector import Error


class Connection():
    DATA_BASE = "books_db"
    USERNAME = "root"
    PASSWORD = "admin"
    DB_PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "books_pool"
    pool = None
    
    @classmethod
    def obtain_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    password = cls.PASSWORD,
                    username = cls.USERNAME,
                    database = cls.DATA_BASE,
                )
                return cls.pool
            except Exception as e:
                print(f"Error connecting to DB: {e}")
        else:
            return cls.pool
        
    @classmethod
    def obtain_connection(cls):
        pool = cls.obtain_pool()
        if pool is None:
            raise ConnectionError("Not able to obtain pool connection.")
        return pool.get_connection()
    
    @classmethod
    def release_connection(cls, connection):
        connection.close()
        