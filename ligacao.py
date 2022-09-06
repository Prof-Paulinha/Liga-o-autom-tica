from twilio.rest import Client

account_sid = "AC6d790a0b9f6fc5f79dd83d1bd2751b03"
token = "92903287d5dbb88ef341d24c004f2b8b"
meu_numero = "+5543996191305"
numero_twilio = "+18125949240"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language = "pt-BR">
Olá Lorena! Você ganhou na mega sena, faça um Pix para a Paula!
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to = meu_numero,
    from_ = numero_twilio,
    twiml = mensagem
)

