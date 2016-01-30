# Django Rest Framework Crash Course

# Introdução
 - Quem sou eu.
 - O que é o Django Rest Framework. (Explicar as 3 palavras: Django, Rest, Framework)
   - Django
   - REST
     - Comparação com o modelo de Resources das versões anteriores.
     - Status codes
   - Framework
     - Falar sobre browsable API.

-----------
- SetUp

- Serializadores
    - Funciona como os forms do Django.
    - Serializers e ModelSerializers
-----------
    - Fields e Relations
    - Hyperlinks

- Views
    - Requests, responses, decorators.
    - Class base views.
    - Viewsets. Obs: Não use viewsets porque é mais fácil, isso pode complicar muito as coisas.

- Testes
    - O problema de testar com algumas coisas escondidas. Exemplo:
    ```
        class ArticleSerializaer(serializers.ModelSerializer)
            class Meta:
                model = Article
    ```
    Como testa isso? A mesma coisa para viewsets.
    Código implícito gera suposições (translate assumption: presunção, pretensão, suposição, hipótese).
    - Testes direto na view ou nos serializadores. Tente testar tudo.

- Autenticação
    - Casos de uso do DRF: APIs para navegadores e para clientes backend.
    - Autenticação e permissão (Quem é você? vs O que você tá fazendo aqui?)
    - Relacionado: AJAX, CORS e CSRF
    - Uso de JWT.

- Outras features
    - Versionamento
      - Porque? Porque você assinou um contrato com o cliente quando disponiblizou uma API.
      - Como? Mil maneiras.
    - Paginação
    - Renderers
    - Filtragem em qs params
    - Throttling
    - Extensões: cache, etags (https://github.com/chibisov/drf-extensions)
