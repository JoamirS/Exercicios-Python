import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

# Settings email
email.To = 'james@outlook.com'
email.Subject = 'Email Automático'

email.HTMLBody = '''
<p> Olá Lira, aqui é Joamir no código Python. </p>

<p> O faturamento da loja foi de R$ 15000. </p>

<p> Grande abraço! </p>
<p> Código Python </p>
'''

email.Send()
print('Email enviado')
