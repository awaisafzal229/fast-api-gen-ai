from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "userName" : "Ali",
    "rollNo" : 20
},
{
    "userName" : "Awais",
    "rollNo" : 21
}
]
@app.get("/students")
def getStudents():
    return students

@app.get("/addStudent")
def addStudent(userName: str, rollNo: str):
    global students
    students.append({"userName": userName, "rollNo": rollNo})
    return students

@app.get("/")
def helloWorld():
    return "Hello, World!"

@app.get("/gettodos/{id}")
def getTodos(id):
    print("Get todos called",id)
    return id    

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

# @app.get("/getSingleTodo")
# def getSingleTodo():
#     print("Get todo called")
#     return "getSingleTodo called"
@app.get("/getSingleTodo")
def get_single_todo(userName:str, rollNo:str):
    print("Get todo called",userName, rollNo)
    return "getSingleTodo called"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"


def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


# @app.post("/gettodos")
# def get_todos_post():
#     print("Post method todos called")
#     return "post gettodos called"

# @app.post("/posttodos")
# def post_todos():
#     print("Post method todos called")
#     return "post posttodos called"


# # if __name__ == "__main__":
# #     uvicorn.run("your_module_name:app", host="127.0.0.1", port=8080, reload=True)
# def start():
#     uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)
#     # uvicorn.reload(True)












