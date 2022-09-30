from fastapi import FastAPI,HTTPException,status,Depends
from database import users
from models import User
from schema import serializeDict,serializeList
from bson import ObjectId
from hashing import Hash
from JWTtoken import create_access_token
from oauth2hadler import get_current_user
from fastapi.security import  OAuth2PasswordRequestForm

app=FastAPI()

@app.get('/users')
async def index():
    print(users.find())
    return serializeList(users.find())

@app.get('/users/{id}')
async def index(id,current_user:User=Depends(get_current_user)):
    print(current_user)
    return serializeDict(users.find_one({"_id":ObjectId(id)}))

@app.post('/users')
def create_users(user:User):
    user.password=Hash.bcrypt(user.password)# şifre hashleme!!
    users.insert_one(dict(user))
    return serializeList(users.find())

@app.put('/users')
def update_users(id,user:User):
    # users.find_one_update({"_id":ObjectId(id),"$set":dict(user)})
    users.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return serializeDict(users.find_one({"_id":ObjectId(id)}))

@app.delete('/users/{id}')
def delete_user(id):
    users.find_one_and_delete({"_id":ObjectId(id)})
    return 'deleted'

@app.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends()):
    user=users.find_one({"email":request.username})
    if(not user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Hatalı Email")
    elif(not Hash.verify(user['password'],request.password)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Hatalı Şifre")
    else:
        #kullanıcıya ait bilgileri hashleniyor
        access_token = create_access_token(data={
            "email": user["email"],
            "name":user["name"],
            "surname":user["surname"],
            "id":str(user["_id"])
            })
        return {"access_token": access_token, "token_type": "bearer"}
        
        
    


    
