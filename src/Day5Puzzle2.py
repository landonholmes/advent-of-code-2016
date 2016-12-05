from hashlib import md5
instructions = "ojvtpuvg"

integer_hash = 0
password = ""

while True:
    hashed = md5(instructions+str(integer_hash)).hexdigest()

    if hashed.startswith("00000"):
        password += hashed[5]
        print password

    integer_hash += 1

    if len(password) == 8:
        break


print password