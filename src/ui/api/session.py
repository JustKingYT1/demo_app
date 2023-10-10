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
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
            
            case 200:
                self.error = None
                self.user.userID = answer["result"][0]


    def login(self, login: str, password: str):
        answer: dict = resolvers.login(user=AccountLog(userID=self.user.userID, login=login, password=password))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
            
            case 200:
                self.error = None
                self.user = UserAccount(userID=answer["result"][0],
                                        login=answer["result"][1],
                                        password=answer["result"][2],
                                        access_level=resolvers.get_access_level(answer["result"][0]))
                self.auth = True
    
    def register(self, login: str, password: str):
        answer: dict = resolvers.register(user=AccountLog(userID=self.user.userID, login=login, password=password))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
                
            case 200:
                self.error = answer["msg"]
                self.user = UserAccount(userID=answer["result"][0],
                                        login=answer["result"][1],
                                        password=answer["result"][2],
                                        access_level=resolvers.get_access_level(answer["result"][0]))
                self.auth = True

    def update(self, password: str):
        answer: dict = resolvers.update(AccountPass(password=password), userID=self.user.userID)

        match answer["code"]:
            case 400:
                self.error = answer["msg"]

            case 200:
                self.error = None