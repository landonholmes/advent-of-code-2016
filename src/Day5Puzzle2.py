from hashlib import md5
instructions = "ojvtpuvg"

integer_hash = 0
password = ['', '', '', '', '', '', '', '']

while True:
    hashed = md5(instructions+str(integer_hash)).hexdigest()

    if hashed.startswith("00000"):
        try:
            if password[int(hashed[5])] == '':  # only overwrite the non-filled out letters
                password[int(hashed[5])] = hashed[6]
                print password
        except:
            pass  # don't do anything for letters (the int conversion breaks)

    integer_hash += 1

    if len(''.join(password)) == 8:
        break


print ''.join(password)
