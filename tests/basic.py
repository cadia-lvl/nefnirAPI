import requests
import os

test_file = 'basic.txt'
expected_file = 'basic_exp.txt'
recieve_file = 'basic_recv.txt'
if os.path.exists(recieve_file):
    os.remove(recieve_file)
with open(test_file, 'r') as f:
    r = requests.post('http://localhost:8080/lemmitizer', files={'file': f})
    with open(recieve_file, 'wb') as f2:
        f2.write(r.content)
    with open(expected_file, 'rb') as f2:
        expected = f2.read()
        if expected != r.content:
            print("Different file recieved then expected")
        print((r.content))


