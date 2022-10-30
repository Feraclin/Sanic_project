from hashlib import sha1

signature = sha1(f'{"CaY5iCkYtN7DqXdiYK1BvmGrQuaSA4Tl4bEk9my0jc0="}:{1234567}:{1}:{2}:{1000}'.encode()).hexdigest()

print(signature)
print(sha1('CaY5iCkYtN7DqXdiYK1BvmGrQuaSA4Tl4bEk9my0jc0=:1234567:1:2:1000'.encode()).hexdigest())
