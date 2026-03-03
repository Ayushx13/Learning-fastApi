from fastapi import FastAPI

app = FastAPI()


# @app -> path operation decorator , get -> http method or Operation , "/" -> path
@app.get("/")
def index(): #path operation function
    return {
        "data": "Blog List"
    }


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