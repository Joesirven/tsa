import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users import UserRepository, UserOut, UserOutWithPassword


class TSAAuthenticator(Authenticator):
    async def get_account_data(
        self,
        email: str,
        users: UserRepository,
    ):
        return users.get_one(email)

    def get_account_getter(
        self,
        users: UserRepository = Depends(),
    ):
        return users

    def get_hashed_password(self, user: UserOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return user.hashed_password

    def get_account_data_for_cookie(self, user: UserOut):
        return user.email, UserOut(**user.dict())


authenticator = TSAAuthenticator(os.environ["SIGNING_KEY"])
