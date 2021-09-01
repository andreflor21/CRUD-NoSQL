from app.models.posts_error_model import PostsKeysError
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
    def __init__(self, data: dict) -> None:
        try:
            self.title: str = data['title']
            self.author: str = data['author']
            self.content: str = data['content']
            self.tags: list = data['tags']
        except KeyError:
            raise PostsKeysError(**data)

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

    @classmethod
    def update(cls,post_id: int, data: dict):
        
        try:

            update_keys = [item for item in data.keys() if item in cls.post_keys]
            if len(update_keys) == 0:
                raise PostsKeysError(**data)
                

            update_info = dict(zip(update_keys, data.values()))
            update_info["updated_at"] = datetime.utcnow()
            update = {"$set": update_info}
            
            result = db.posts.update_one({"id": post_id}, update)

            if bool(result.acknowledged and result.modified_count):
                post = db.posts.find_one({"id": post_id})
                del post["_id"]

                return post
        
        except TypeError:
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
            post = db.posts.find_one({"id": post_id})
            del post["_id"]
        
            return post
        
        except TypeError:
            
            return False

    @staticmethod
    def delete_post(post_id: int):
        try:
            deleted_post = db.posts.find_one({"id": post_id})
            del deleted_post["_id"]
        
        except TypeError:
            return False
        
        finally:     
            result = db.posts.delete_one({"id": post_id})
        
            if bool(result.acknowledged and result.deleted_count):
                return deleted_post