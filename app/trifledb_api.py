from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version
from pydantic import BaseModel
from app.trifledb import TrifleDB


app = FastAPI(title="TrifleDB key-value store")
trifledb = TrifleDB()

class Data(BaseModel):
    value: str

@app.get("/{key}")
@version(1)
def get(key: str):
    value = trifledb[key]
    if not value:
        return "key not found"
    return value

@app.put("/{key}", status_code=200)
@version(1)
async def put(key: str, data: Data):
    trifledb[key] = data.value
    return True
    
app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}',
    enable_latest=True)