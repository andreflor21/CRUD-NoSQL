
from flask import Flask, request


from app.models.posts_model import Post

def init_app(app: Flask):
    

    @app.post("/posts")
    def create_post():
        data = request.json

        post = Post(title=data["title"], author=data["author"], content=data["content"], tags=data["tags"])
        response =  post.create()
        if response:
            return {"data": response}, 201

        return {"msg": "erro"}, 400

    @app.get("/posts")
    def read_posts():
        posts = Post.read_all()

        return {"data": posts}, 200
    
    @app.get("/posts/<int:post_id>")
    def read_post_by_id(post_id: int):
        post = Post.read_specifc_post(post_id=post_id)

        return {"data": post}, 200

    @app.delete("/posts/<int:post_id>")
    def delete_post(post_id):
        response = Post.delete_post(post_id=post_id)
        if response:
            return "", 204
        
        return {"msg": "Post not found"}, 404