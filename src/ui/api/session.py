from ui.api import resolvers
from server.database.models import UserAccount

class Session:
    auth: bool = False
    user: UserAccount = UserAccount(
            userID=0,
            login='',
            password='',
            access_level=0
        )
    error: bool = False
     