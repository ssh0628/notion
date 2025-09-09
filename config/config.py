# /config/config.py

PORT = 8080
# test user info
INFO = {
    # username : {password:password}
    "asd123" : {"password":"asd123"}, 
}

PROJECT = {
    # username :[{id, name, date}]
    "asd123" : [
        {"id" : "project1", "name": "first project", "create_date":"2002-01-20"},
        {"id" : "project2", "name": "second project", "create_date":"2005-10-01"}, 
        {"id" : "project3", "name": "third project", "create_date":"2007-07-30"}
        ], 
    "qwe123":[
        {}
    ]
}
