from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/terms')
def terms():
    return '''
        Termos de Uso para a Exclusão de Dados

        Estes termos de uso descrevem como os usuários podem solicitar a exclusão de dados deixados em nosso site. Nós nos comprometemos a proteger a privacidade de nossos usuários e a garantir que todas as informações coletadas sejam usadas de maneira justa e transparente.

        Exclusão de Dados

        Se um usuário deseja que seus dados sejam excluídos, ele deve entrar em contato conosco por meio do formulário de contato em nosso site e solicitar a exclusão de seus dados. Os usuários devem fornecer informações suficientes para nos permitir identificar os dados a serem excluídos e confirmar que são proprietários desses dados.

        Processamento da Solicitação

        Após receber a solicitação de exclusão de dados, nós avaliaremos e processaremos a solicitação em um período razoável de tempo. Reservamos o direito de recusar solicitações que sejam excessivamente repetitivas, requerem esforço técnico desproporcional, coloquem em risco a privacidade de outros usuários ou que sejam impraticáveis ​​(por exemplo, devido a requisitos legais aplicáveis).

        Confirmação da Exclusão

        Uma vez que os dados são excluídos, eles não poderão mais ser recuperados e qualquer conteúdo associado a esses dados não será mais acessível. Confirmaremos a exclusão de dados por meio do endereço de e-mail fornecido pelo usuário.

        Alterações nos Termos de Uso

        Reservamos o direito de fazer alterações nestes termos de uso a qualquer momento, mediante aviso prévio aos usuários. Recomendamos que os usuários revisem regularmente estes termos de uso para garantir que estejam cientes de quaisquer alterações.

        Contato

        Se você tiver dúvidas sobre estes termos de uso ou sobre a exclusão de dados, entre em contato conosco através do formulário de contato em nosso site.
    '''

@app.route('/privacy')
def privacy():
    return '''
        Política de Privacidade para Coleta de Número de Seguidores do Instagram

        Esta política de privacidade descreve como a coleta de números de seguidores do Instagram é realizada e protegida. Nós nos comprometemos a proteger a privacidade de nossos usuários e a garantir que todas as informações coletadas sejam usadas de maneira justa e transparente.

        Coleta de Dados

        Para coletar o número de seguidores do Instagram de uma lista de usuários, precisamos obter acesso ao perfil público de cada usuário na plataforma do Instagram. A coleta será feita apenas com o consentimento prévio e explícito do proprietário da conta do Instagram.

        Uso de Dados

        Os números de seguidores coletados serão usados ​​apenas para fins de análise e pesquisa. Essas informações nos permitirão avaliar a popularidade de um usuário no Instagram em relação a outros usuários na mesma lista. Nenhum dado pessoal do usuário será compartilhado com terceiros sem o consentimento prévio e explícito do proprietário da conta do Instagram.

        Proteção de Dados

        Tomamos medidas de segurança adequadas para garantir que os dados coletados sejam protegidos contra acesso não autorizado, uso indevido, alteração, divulgação ou destruição. Os dados coletados são armazenados em um servidor seguro e restrito apenas a membros da equipe que precisam acessá-lo para fins de análise.

        Cookies

        Usamos cookies para coletar informações sobre o uso do nosso site. Os cookies são arquivos de texto armazenados no computador do usuário que nos permitem identificar o navegador e o dispositivo do usuário. As informações coletadas por meio de cookies são usadas apenas para melhorar a experiência do usuário e aprimorar nossos serviços.

        Alterações na Política de Privacidade

        Reservamos o direito de fazer alterações nesta política de privacidade a qualquer momento, mediante aviso prévio aos usuários. Recomendamos que os usuários revisem regularmente esta política de privacidade para garantir que estejam cientes de quaisquer alterações.

        Contato

        Se você tiver dúvidas sobre esta política de privacidade ou sobre as práticas de coleta de dados, entre em contato conosco através do endereço de e-mail fornecido em nosso site.
    '''
    
    
@app.route('/delete')
def delete():
    return '''Entre em contato conosco para deletar! loris@loristron.com'''

if __name__ == '__main__':
    app.run(port=8080, debug=True)