from config.firebase import conected_firebase
from firebase_admin import db

class HomeController:
    @staticmethod
    def test():
        return {"Hello": "World"}

    @staticmethod
    def register(email: str, password: str):
        print(email, password)
        try:
            ref = db.reference('users')  
            ref.set({
            "user_1": {
                "email": "user1@example.com",
                "name": "John Doe"
            }
        })

            return {"message": "User registered successfully", "user_id": user.uid}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
