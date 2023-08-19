from fastapi import FastAPI
import uvicorn


count: int  = 0

app = FastAPI()

@app.get("/")
async def root():
    global count
    count += 1
    return {"message": f"{count}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
