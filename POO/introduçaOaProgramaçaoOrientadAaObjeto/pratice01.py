import smtplib
import ssl

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        meu_mailer = Mailer("password_reset@teste.com", "myverysafepassword", self.email)
        meu_mailer.send_email("Reset your password", "Instruções para resetar a senha, com o link de resetar")


class Mailer:
    def __init__(self, from_email, from_password, to_email):
        self.from_email = from_email
        self.from_password = from_password
        self.to_email = to_email

    def send_email(self, subject, message):
        body = f"Subject:{subject}\n\n{message}".encode('utf-8')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context
        ) as server:
            server.login(self.from_email, self.from_password)
            try:
                server.sendmail(self.from_email, self.to_email, body)
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                raise ValueError


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()

# ines = User("Ines", "ines2020@gmail.com", "ines1997")

# alexandre = User("Ale", "eskalo@gmail.com", "eskalo123")

# ines.reset_password()

# alexandre.reset_password()

# print(ines)
# print(alexandre)
# print(ines.name)
# print(ines.email)
# print(alexandre.password)

"""
    Na Programação Orientada a Objeto muitas coisas tem nome, e é importante sabermos quais são
    são jargões importantes para uma boa comunicação no mercado!
    Vamos parar para resumir tudo o que aprendemos até agora, e dar nomes ao que fizemos.
"""

# Class: Entidade "geral" que definimos com base no problema que queremos resolver.

# Objeto: Entidade "específica", criada apartir das regras definidas pela entidade "geral". Pense que a class é o modelo e o objeto a escultura que o modelo faz.

# Instância: esse é novo! Sabe quando criamos um objeto apartir de uma class! Então! Dizemos que esse objeto é uma instância dessa classe! Ou, também dizemos que a classe instanciou um objeto!

# Atributo: outro novo! Um atributo é uma informação de uma instância que você criou. O nome de um User, por exemplo.

# Mensagem: Forma com que objetos interagem - chamando funções uns dos outros. Um chamado como esse é um envio de mensagem a outro objeto. "User, resete sua senha!"

# Abstração: Pilar da Programação Orientada a Objetos. Se refere a sempre criar entendidades que farão as ações que resolverão seu problema.

# Encapsulamento: Pilar da Programação Orientada a Objetos. Se refere a poder instanciar uma entidade e enviar mensagens a ela sem saber como ela funciona por dentro