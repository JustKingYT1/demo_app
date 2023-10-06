from ui.api import resolvers
from server.database.models import UserAccount, AccountLog, AccountPass, SignIn

class Session:
    auth: bool = False
    user: UserAccount = UserAccount(
            userID=-1,
            login='',
            password='',
            access_level=0
        )
    error: str = None
    server_available: bool = False


    def sign(self, FIO: str):
        answer: dict = resolvers.get_userID(data=SignIn(FIO=FIO))

        match answer:
            case {"code": 400}:
                self.error = answer["msg"]
            
            case {"code": 200}:
                self.user.userID = answer["result"][0]


    def login(self, login: str, password: str, userID: int):
        answer: dict = resolvers.login(user=AccountLog(userID=userID, login=login, password=password))
        match answer:
            case {"code": 400}:
                self.error = answer["msg"]
            
            case {"code": 200}:
                self.user = UserAccount(userID=answer["result"][1],
                                        login=answer["result"][2],
                                        password=answer["result"][3],
                                        access_level=resolvers.get_access_level(answer["result"][1]))
                self.auth = True
    
    def register(self, login: str, password: str, userID: int):
        answer: dict = resolvers.register(user=AccountLog(userID=userID, login=login, password=password))
        match answer:
            case {"code": 400}:
                self.error = answer["msg"]
                
            case {"code": 200}:
                self.user = AccountLog(userID=answer["result"][1],
                                        login=answer["result"][2],
                                        password=answer["result"][3])
                self.auth = True

    def update(self, password: str, userID: int):
        answer: dict = resolvers.update(AccountPass(password=password), userID=userID)

        match answer:
            case {"code": 400}:
                self.error = answer["msg"]