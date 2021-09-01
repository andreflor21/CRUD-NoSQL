
from flask import Flask, request, jsonify
from pymongo import response


from app.models.posts_model import Post

def init_app(app: Flask):
    

    @app.post("/posts")
    def create_post():
        data = request.json
        try:
            post = Post(title=data["title"], author=data["author"], content=data["content"], tags=data["tags"])
            response =  post.create()
            if response:
                return {"data": response}, 201
        except KeyError as err:
            return {"error": "Wrong keys inserted"}, 406
        

    @app.get("/posts")
    def read_posts():
        posts = Post.read_all()

        return {"data": posts}, 200
    
    @app.get("/posts/<int:post_id>")
    def read_post_by_id(post_id: int):
        response = Post.read_specifc_post(post_id=post_id)

        if response:
            return {"data": response}, 200
        
        return {"error": "Post not found"}, 404

    @app.delete("/posts/<int:post_id>")
    def delete_post(post_id):
        response = Post.delete_post(post_id=post_id)

        if response:
            return {"data": response}, 200
        
        return {"error": "Post not found"}, 404


    @app.patch("/posts/<int:post_id>")
    def update_post(post_id: int):
        data: dict = request.json
        try:
            response = Post.update(post_id=post_id, data=data)
            if response:
                return {"data": response}, 200
        
            return {"error": "Post not found"}, 404
            
        except KeyError:
            return {"error": "Wrong keys inserted"}, 406