from fastapi import FastAPI, Body 


app = FastAPI()

# Create a GET ReST API

@app.get("/api")
# Get api 
def first_api():
    return {"msg" : "hello_world"}

# Create a GET ReST API with path parameters
# Need to use %20 as spaces
@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return({"msg": path_param})

# Create a GET ReST API with query parameters
# fast api knows that it is a query parameter because of the missing {} in the url 
@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}

# Create a GET ReST API with path parameters AND query parameters
@app.get("/books/{path_param}/")
def first_apiV4(path_param: str, actor: str):
    # Curl command to test is 
    # curl 'http://127.0.0.1:8000/books/main_actor/?actor=Harry'
    return {"msg": path_param, "actor": actor}

# Create a POST ReST API
#  curl 'http://127.0.0.1:8000/books/create_book' -d "{'title': 'Harry Potter', 'author' : 'J.K Rowling', 'category': fiction'}" 
@app.post("/books/create_book")
def first_api_postV5(new_book = Body()):
    print(new_book)
    return {"msg": new_book}


# Create a PUT ReST API 


# Create a DELETE ReST API
