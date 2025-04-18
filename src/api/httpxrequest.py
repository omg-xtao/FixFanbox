import httpx

__all__ = ("HTTPXRequest",)

from persica.factory.component import AsyncInitializingComponent

timeout_int = 20
timeout = httpx.Timeout(
    timeout=timeout_int,
    read=timeout_int,
    write=timeout_int,
    connect=timeout_int,
    pool=timeout_int,
)


class HTTPXRequest(AsyncInitializingComponent):
    def __init__(self, *args, headers=None, **kwargs):
        self.client = httpx.AsyncClient(headers=headers, *args, **kwargs)

    async def shutdown(self):
        if self.client.is_closed:
            return
        await self.client.aclose()
