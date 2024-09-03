from config import TOKEN

from typing import List, Optional
from kvsqlite import Client

ID = TOKEN.split(":")[0]

db_: Optional[Client] = None


def db() -> Client:
    global db_
    if db_ is not None:
        return db_

    db_ = Client("ytm.db")
    return db_


async def get_users() -> List[int]:
    return await db().get(ID + "-USERS") or []


async def update_users(users_ids: List[int]) -> bool:
    return await db().set(ID + "-USERS", users_ids)


async def update_user(user_id: int, _: int = 1) -> bool:
    users = await get_users()
    if _ == 1:
        users.append(user_id)
    else:
        if user_id in users:
            users.remove(user_id)
    return await update_users(users)


async def is_user(user_id: int) -> bool:
    users = await get_users()

    return bool(user_id in users)


async def get_audio(vid_id: str) -> Optional[str]:
    return await db().get(vid_id)


async def add_audio(vid_id: str, msg_link: str) -> bool:
    return await db().set(vid_id, msg_link)
