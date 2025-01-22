import asyncpg

class AsyncDB:
    def __init__(self, host='localhost', port=5432, user='user', password='password', database='database', loop=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.loop = loop
        self.pool = None

    async def connect(self):
        """Tạo pool kết nối bất đồng bộ."""
        self.pool = await asyncpg.create_pool(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            min_size=5,  # Số lượng kết nối tối thiểu trong pool
            max_size=10  # Số lượng kết nối tối đa trong pool
        )

    async def close(self):
        """Đóng pool kết nối."""
        await self.pool.close()

    async def fetch(self, query, *args):
        """Thực hiện một truy vấn và trả về tất cả kết quả."""
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def fetchrow(self, query, *args):
        """Thực hiện một truy vấn và trả về hàng đầu tiên của kết quả."""
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query, *args)

    async def execute(self, query, *args):
        """Thực hiện một truy vấn mà không cần trả về kết quả (INSERT, UPDATE, DELETE)."""
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

# Sử dụng framework
import asyncio

async def main():
    db = AsyncDB(user='postgres', password='postgres', database='asyncpgdb')
    await db.connect()

    try:
        # Ví dụ: Thực hiện một truy vấn để lấy dữ liệu
        result = await db.fetch('SELECT * FROM demo LIMIT 10')
        for row in result:
            print(row)

        # Thực hiện một truy vấn khác bất đồng bộ
        row = await db.fetchrow('SELECT * FROM demo WHERE id = $1', 1)
        if row:
            print(row)

        # Thực hiện một lệnh INSERT
        await db.execute('INSERT INTO demo (name) VALUES ($1)', 'some value')

    finally:
        await db.close()

# Chạy chương trình bất đồng bộ
asyncio.run(main())