from fastapi import FastAPI
from blog.database import engine
from blog import models
from blog.routers import blog, user, authentication

app = FastAPI()

# Create all the table if not exists
models.Base.metadata.create_all(engine)

# Register our route 
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)