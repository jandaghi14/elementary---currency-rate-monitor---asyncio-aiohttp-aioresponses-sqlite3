import sqlite3

class CurrencyDatabase():
    def __init__(self , filename):
        self.conn = None
        self.filename = filename
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.filename)
        print("Connection created!")
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        print("Connection committed and closed!")
        
if __name__ == '__main__':
    with CurrencyDatabase('CurrencyCache.db') as conn:
        cursor = conn.cursor()
        print(cursor.execute('SELECT * FROM cache').fetchall())