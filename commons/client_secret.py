import string
import secrets
import bcrypt


# token = secrets.token_bytes()
# print(token)

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
print(password)

# while True:
#     password = ''.join(secrets.choice(alphabet) for i in range(10))
#     if (any(c.islower() for c in password)
#             and any(c.isupper() for c in password)
#             and sum(c.isdigit() for c in password) >= 3):
#         break

# print(password)

# plain_text = b"OneGalaxy-is-Nebula"
# encrypted_text = bcrypt.hashpw(plain_text, bcrypt.gensalt(rounds=10, prefix=b"2a"))
# print(encrypted_text)



