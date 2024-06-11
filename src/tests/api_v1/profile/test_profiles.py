import pytest
from httpx import AsyncClient
 
 

@pytest.mark.asyncio
async def test_get_profile_route(async_client: AsyncClient):
    response = await async_client.get("/api/v1/profile/2")
    assert response.status_code == 200