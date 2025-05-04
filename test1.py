# from fastapi import FastAPI
import fastapi

# app = FastAPI()
app = fastapi.Response('{"hello": "world"}', media_type="application/json", status_code=200)

print(app.__repr__())
print(repr(app))
print(str(app))
