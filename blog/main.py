from fastapi import FastAPI
from database import engine
import models
from routers import blog, user, authentication

app = FastAPI()

# Create all the table if not exists
models.Base.metadata.create_all(engine)

# Register our route 
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)