from hashlib import sha1

import jwt

signature = sha1(f'{"CaY5iCkYtN7DqXdiYK1BvmGrQuaSA4Tl4bEk9my0jc0="}:{1234567}:{1}:{2}:{1000}'.encode()).hexdigest()

# print(signature)
# print(sha1('CaY5iCkYtN7DqXdiYK1BvmGrQuaSA4Tl4bEk9my0jc0=:1234567:1:2:1000'.encode()).hexdigest())

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYW5vdGhlcl91c2VyIn0.IzTw7IgAiqyq3fAULd_81YqXGhWOOkEWGUF-MOa62J8"
secret = "U6rct6fv89jkjb8hHJJ95bKOjfodfu8KMBYf059ng909nIhnJNd"
test = jwt.decode(
            token, secret, algorithms=["HS256"]
        )
print(test.get('name'))