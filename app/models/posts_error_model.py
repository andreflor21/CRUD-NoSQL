class PostsKeysError(Exception):
    keys = ["title", "author", "content", "tags"]

    def __init__(self, **kwargs) -> None:
        self.message = {
            "wrong fields": [key for key in kwargs if key not in self.keys]
        }
        super().__init__(self.message)