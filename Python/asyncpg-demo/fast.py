import asyncpg
from pydantic import BaseModel
from typing import Optional, Type, TypeVar, List, Dict, Any
from contextlib import asynccontextmanager
from aiocache import cached

T = TypeVar('T', bound='Model')

class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None

    async def connect(self, dsn: str, **kwargs):
        self.pool = await asyncpg.create_pool(dsn=dsn, **kwargs)
    
    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    @asynccontextmanager
    async def transaction(self):
        if not self.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                yield conn

    async def execute(self, query: str, *args) -> int:
        if not self.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)

    async def fetch(self, query: str, *args) -> List[asyncpg.Record]:
        if not self.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    def cache(self, ttl: int = 60):
        def decorator(func):
            @cached(ttl=ttl)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

class Model(BaseModel):
    _table: str = ""
    _pk: str = "id"

    @classmethod
    async def create(cls: Type[T], **data) -> T:
        fields = ', '.join(data.keys())
        placeholders = ', '.join([f'${i+1}' for i in range(len(data))])
        query = f"INSERT INTO {cls._table} ({fields}) VALUES ({placeholders}) RETURNING *"
        
        if not database.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with database.pool.acquire() as conn:
            record = await conn.fetchrow(query, *data.values())
            return cls(**record)

    @classmethod
    async def get(cls: Type[T], pk: Any) -> Optional[T]:
        query = f"SELECT * FROM {cls._table} WHERE {cls._pk} = $1"
        if not database.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with database.pool.acquire() as conn:
            record = await conn.fetchrow(query, pk)
            return cls(**record) if record else None

    async def update(self):
        fields = ', '.join([f"{k} = ${i+1}" for i, k in enumerate(self.dict().keys())])
        query = f"UPDATE {self._table} SET {fields} WHERE {self._pk} = ${len(self.dict())+1}"
        
        if not database.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with database.pool.acquire() as conn:
            await conn.execute(query, *self.dict().values(), getattr(self, self._pk))

    async def delete(self):
        query = f"DELETE FROM {self._table} WHERE {self._pk} = $1"
        if not database.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with database.pool.acquire() as conn:
            await conn.execute(query, getattr(self, self._pk))

database = Database()

class User(Model):
    _table: str = "demo"
    _pk: str = "id"
    id: int
    name: str

# Usage
async def main():
    await database.connect(
        dsn="postgres://postgres:postgres@localhost/asyncpgdb",
        min_size=5,
        max_size=20
    )

    # new_user = await User.create(name="John Doe")
    # user = await User.get(1)
    # user.name = "Jane Doe"
    # await user.update()
    # await user.delete()
    # await database.disconnect()

import asyncio
asyncio.run(main())
