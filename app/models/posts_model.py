from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv('DATABASE_URL'), int(os.getenv('DATABASE_PORT')))

db = client.kenzie_db
db.posts

class Post():
    post_keys = ["title", "author", "content", "tags"]
    def __init__(self, title: str, author: str, content: str, tags: list) -> None:
            self.title: str = title
            self.author: str = author
            self.content: str = content
            self.tags: list = tags


    def create(self):
        data = self.__dict__
        try:
            posts = list(db.posts.find())
            data['id'] = posts[-1]["id"] + 1

        except IndexError:
            data['id'] = 1
        
        finally:
            data['created_at'] = datetime.utcnow()
            data['updated_at'] = datetime.utcnow()
            id = db.posts.insert_one(data).inserted_id
            if id:
                del data["_id"]
                return data

    @staticmethod
    def update(post_id: int, data: dict):
        post_keys = ["title", "author", "content", "tags"]
        try:

            update_keys = [item for item in data.keys() if item in post_keys]
            if len(update_keys) == 0:
                raise KeyError

            update_info = dict(zip(update_keys, data.values()))
            update_info["updated_at"] = datetime.utcnow()
            update = {"$set": update_info}
            
            acknowledge = db.posts.update_one({"id": post_id}, update).acknowledged

            if acknowledge:
                post = list(db.posts.find({"id": post_id}))[0]
                del post["_id"]

                return post
        
        except IndexError:
            return False

    @staticmethod
    def read_all():
        posts_list = list(db.posts.find())
        for post in posts_list:
            del post["_id"]

        return posts_list

    @staticmethod
    def read_specifc_post(post_id: int):

        try:
            post = list(db.posts.find({"id": post_id}))[0]
            del post["_id"]
        
            return post
        
        except IndexError:
            
            return False

    @staticmethod
    def delete_post(post_id: int):
        try:
            deleted_post = list(db.posts.find({"id": post_id}))[0]
            del deleted_post["_id"]
        
        except IndexError:
            return False
        
        finally:     
            delete_count = db.posts.delete_one({"id": post_id}).deleted_count
        
            if delete_count == 1:
                return deleted_post