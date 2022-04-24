from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

my_posts = [
    {"id": 1, "title": "Hello World", "content": "First post content", "published": True},
    {"id": 2, "title": "Hello Mars", "content": "Second post content", "published": False},
]

@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_to_save = {}
    post_to_save['id'] = len(my_posts) + 1
    post_to_save.update(post.dict())
    my_posts.append(post_to_save)
    return {"data": my_posts}


# make a curl request to http://localhost:8000/createpost
# curl -X POST -H "Content-Type: application/json" -d '{"title": "My first post", "content": "This is my first post", "published": true, "rating": 3}' http://localhost:8000/createpost