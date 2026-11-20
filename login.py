import secrets

# token = screts.token_hex(16)
class Login:
    def __init__(self, username, password, token):
        self.username = username
        self.password = password
        self.token = token
    def username_(self, *args):
        if not self.username and self.username.replace(" ",""):
           return "Username não pode ficar vazio e ou conter espaço."
        return "Username válido."
    def password_(self):
        if not self.password:
            return "Password não pode ficar vazio."
        return "Password Válido."
        if len(self.password) < 4 or len(self.password) > 8:
            return "Password deve conter no mínimo 4  e no máximo 8 caracteres."
        return "Password Válido."
    def gerar_token(self):
        if self.password_() =="Password Válido.":
            self.token = secrets.token_hex(16)
            return self.token
        return "Não foi possivel gerar o token."


    def logar_sistema(self, username,token):
        if self.username == username:
            if self.token == token:
                return "Validado"
        return "Não Validado"



login = Login ("Rafael","123456", "")

print(login.logar_sistema("Rafael", '78ac36eedb0969040c447b20aeb2b010'))
# print(login.password_())
print(login.gerar_token())