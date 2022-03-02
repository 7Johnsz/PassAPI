<p align="center">
  <img src="/img/PassAPI.png">
</p>

<div align="center">
    <em>simple, elegant and safe</em>
</div>

---

## Introduction
PassAPI is a password generator in hash format and fully developed in Python, with the aim of teaching how to handle and build
- Strong points:

    - [x] Token verification by authorization header :tada:
    - [x] Fully OpenSource :tada:
    - [x] Already comes with ratelimit :tada:
    - [x] Easy to understand :tada:
    - [x] Frequently updated :tada:

- Weak points:
    - [ ] Possible lack of functions, but we will update with time 🔍

## Requirements
Recommended Python 3.6+

Developed in Python 3.10.1

## Installation

```console
$ pip install -r requirements.txt


--> 100%
```

## Using
### Starting 
* Starting the `main.py`, in your console it should work like this:

```console
INFO:     Started server process [2364]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
```

* Note: if this appears in your console, don't worry just add the hash in your .env 

```console
[!] You didn't generate a hash to protect your APIKEY, so we generated one for you!
 
[+] Here: "Hash"
[+] You should put it there in .env  
```

### Using the PassAPI

* You will need some application to inject the API (REST Client), for example:

    -   <p>
            <a href="https://www.postman.com/">Postman</a>
        </p>
    - <p>
        <a href="https://insomnia.rest/">Insomnia</a>
     </p>

    - **REST Client** which is an extension of Visual Studio Code
    - You can use FastAPI application by accessing your server url and adding /docs
        - `http://127.0.0.1/docs`
* and others...

### Testing

* Here is an example POST (Using the REST Client):

```console
POST http://127.0.0.1:8080/ HTTP/1.1
Content-Type: application/json
Authorization: "HASH"

{
    "length": 5
}
```

* Output:

```console
{
    "detail": [
      {
        "password":"phG[P",
        "timestamp":"2022-03-01 23:14:06"
      }
    ]
}
```

* Note: The rate limit already configured is 50 requests in 1 minute, but you can change it in `/src/routers/routers.py`

## License

PassAPI is released under [the MIT License](LICENSE). Check [LICENSE](LICENSE) file for more information.
