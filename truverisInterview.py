import requests
import hashlib

#gets the body of the url that is being passed in
def getBody(url):
    req = requests.get(url)
    return(str(req.content))

#hashes and concatenates and prints the encoded value
def concatAndHash(body,email):
    body = body + str(email)
    print(hashlib.sha256(body.encode('utf-8')).hexdigest())

if __name__ == "__main__":
    concatAndHash(getBody("https://truveris.github.io/jobs/"),"sr594@njit.edu")
