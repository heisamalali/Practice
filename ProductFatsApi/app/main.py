from fastapi import FastAPI
from app.routers import routers
app = FastAPI(
    title='Inventory Management Api',
    description='Inventory Management API',
    version='1.0',
)

for router in routers:
    app.include_router(router)

@app.get('/health', tags=['health'])
async def health_check():
    """health check api"""
    return {
        'status': 'ok',
        'message': 'Health Check API working',
    }

if __name__ == '__main__':
    import  uvicorn
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000,reload=True)