from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# @app -> path operation decorator , get -> http method or Operation , "/" -> path
@app.get("/blog")
def index(limit: int =10 , published: bool = True , sort: Optional[str] = None): #path operation function
    if published:
        return {"data": f"{limit} Published Blog List" }
    else:
        return {"data": f"{limit} Unpublished Blog List" }
        


@app.get("/blog/unpublished")
def unpublished_blogs():
    return {
        "data": "All unpublished blogs"
    }


@app.get("/blog/{id}")
def get_blog(id: int):
    return {
        #"data": f"Blog with id {id}"
        "data": "Blog with id " + str(id)
    }


@app.get("/blog/{id}/comments")
def get_blog_comments(id: int):
    return {
        "data": {
            "1": "This is the first comment",
            "2": "This is the second comment"
        }
    }