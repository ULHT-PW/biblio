# Aplicação biblioteca com integração de autenticação

### configuração do servidor de email
Na conta Google associada configurar o acesso de aplicações externas
1. Ativar o Acesso a Apps Menos Seguros: 
  * No Google, aceda à página de segurança da sua Conta. 
  * Na secção "Acesso a apps menos seguros" ative essa opção. 
    * Isso permite que aplicativos menos seguros, como o Django, acessem sua conta de e-mail do Google. No entanto, este método é menos seguro e não é recomendado para contas sensíveis.
1. Habilitar o Acesso a APIs: 
  1. Aceda ao Google Cloud Console
  1. Crie um novo projeto ou selecione um projeto existente e habilite a API do Gmail para esse projeto.
1. Gerar Credenciais da API: 
  1. Crie uma chave de API
2. configure o backend de e-mail em settings.py 
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
