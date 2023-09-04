import bcrypt

class Utils:

    @classmethod
    def encrypt(self, pass_user):
        salt_rounds = 10
        # Generar una salt aleatoria y encriptar la contraseña
        salt = bcrypt.gensalt(rounds=salt_rounds)
        hashed_password = bcrypt.hashpw(pass_user.encode('utf-8'), salt)
        return hashed_password