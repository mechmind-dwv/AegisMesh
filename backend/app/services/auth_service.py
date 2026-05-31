from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

class AuthService:

    def hash_password(self, password):

        return pwd_context.hash(password)

    def verify_password(
        self,
        password,
        hashed
    ):

        return pwd_context.verify(
            password,
            hashed
        )
