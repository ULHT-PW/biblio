# Aplicação biblioteca com integração de autenticação

### configuração do servidor de email
Autenticado na Conta Gmail Google que pretende configurar a App Password.
1. Clicar na imagem que se encontra no canto superior direito com o icon/fotografia do utilizador. Após clicar sobre a mesma deverá sugir um menu infra onde surge um outro botão azul com o text "Gerir Conta Google". Clicar nesse botão.
2.  Após a ação anterior deverá abrir um novo tab com dashboard da conta Google. No lado esquerdo do ecrã deverá clicar em "Segurança".
3.  A meio da página de segurança deverá existir um grupo de opções "Como iniciar sessão na Google" e no mesmo deverá ter a opção "Validação em 2 passos" ativada. Caso a mesma não esteja ativa, terá de a ativar e configurar.
4.  Na searchbar no header da página segurança deverá pesquisar "Palavras-passe de apps" e seleciona a opção que irá surgir onde redirecciona o utilizador para a página "Palavras-passe de apps".
5.  Na página "Palavras-passe de apps" deverá surgir um fieldset com o titúlo "As suas palavras-passe de aplicações" onde pede para introduzir o nome de uma aplicação. Pode introduzir um nome qualquer como por exemplo: django-pw-email e clicar "Criar". # Atencao irá surgir um pop-up com uma palavra-chave que será apenas mostrado uma vez. Devem copiar app password e retirar os espacos em branco da nesna.
6. Configure o backend de e-mail em settings.py 
  * para que os e-mails de redefinição de senha sejam enviados aos utilizadores. 
  * Especifique o username da conta Google e a password de API criada.

```python
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend’
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu.email@gmail.com'
EMAIL_HOST_PASSWORD = 'googleAppPassword'
```
