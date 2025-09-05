# Como instalar o Projeto

Para instalar o projeto, siga os passos abaixo:

1. Clone o repositório:
   ```
   git clone https://github.com/mtcaio/klubi-tech-challenge
   ```

2. Navegue até o diretório do projeto:
   ```
   cd klubi-tech-challenge/src
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Inicie o aplicativo Streamlit:
   ```
   streamlit run main.py
   ```

## Decisões Técnicas

1. **Escolha do Framework**: Optei por utilizar o Streamlit devido à sua simplicidade e eficiência na criação de aplicações web.

2. **Estrutura do Projeto**: A estrutura do projeto foi organizada em diretórios da seguinte forma:
   ```
   klubi-tech-challenge/
   ├── data/
   ├── models/
   ├── src/
   │   ├── main.py
   │   ├── utils.py
   │   └── ...
   └── requirements.txt
   ```

Na seção `src`, estão os arquivos principais do aplicativo, o entrypoint `main.py`, a seção de utilitários `helpers` contem classes auxiliares, enquanto `data` armazenam os dados utilizados.

O código foi modularizado em 4 classes principais classes: `CarChatbot`, `DataContext`, `OpenAISettings` e `Logger`, cada uma com as seguintes responsabilidades:

    A classe `CarChatbot` é responsável pela lógica principal do chatbot, incluindo a interação com o usuário e a exibição dos dados dos carros. 

    A classe `DataContext` gerencia o carregamento e a consulta dos dados dos carros a partir do arquivo JSON. 

    A classe `OpenAISettings` encapsula as configurações relacionadas à API da OpenAI, facilitando a manutenção e a reutilização do código. 

    A classe `Logger` é responsável por configurar e gerenciar os logs da aplicação, permitindo um monitoramento eficaz das operações e facilitando a depuração.

3. **Gerenciamento de Dependências**: Utilizei o `pip` e um arquivo `requirements.txt` para gerenciar as dependências do projeto, com suas devidos versões para evitar incompatibilidade.

4. **Link de Acesso**: O projeto pode ser acessado localmente através do endereço `http://localhost:8501` após iniciar o aplicativo Streamlit. Ou pela URL pública: [Klubi Challenge](https://klubi-tech-challenge.streamlit.app/)

# Plano de Negócios

1. Se você fosse lançar esse buscador no mercado, qual seria seu modelo de negócios?

    Meu modelo de negócios seria baseado em uma plataforma voltada para compradores de veículos, totalmente gratuita para quem busca carros. O foco seria gerar a melhor experiência de busca e comparação, com filtros avançados e recomendações inteligentes. A receita viria de comissão sobre vendas, anúncios patrocinados de veículos em destaque e parcerias com financeiras e seguradoras, oferecendo soluções de financiamento e seguros diretamente na plataforma.

2. Como você atrairia seus primeiros usuários? (Estratégia de aquisição, canais, etc)

    Para atrair os primeiros usuários, eu utilizaria uma combinação de marketing digital e parcerias estratégicas. Isso incluiria campanhas nas redes sociais, Google Ads e Meta Ads para conquistar novos usuários. Proporia parcerias com concessionárias para promover a plataforma em seus pontos de venda. Além disso, ofereceria um período de teste gratuito para novos usuários, incentivando a experimentação da plataforma.

3. Qual seria sua estimativa de CAC (Custo de Aquisição de Cliente)?

    A estimativa de CAC seria em torno de R$ 15 a R$ 40 por cliente, considerando os custos de marketing digital, utilizando a plataforma de anúncios do Google e do Facebook. Já com parcerias estratégicas, esse custo poderia ser reduzido, pensando em valores em torno de R$ 10 a R$ 25. A princípio a ideia seria investir cerca de R$ 1.000,00 a R$ 3.000,00 mensais em marketing digital para adquirir entre 100 a 200 novos usuários por mês.

4. Qual seria sua proposta de LTV (Lifetime Value) e como você maximizaria isso?

    A proposta de LTV seria calculado com base na jornada do comprador, incluindo comissão por venda, upsell de serviços financeiros (financiamento, seguro, garantia estendida) e retenção via recompra futura. Para maximizar, eu focaria em criar confiança, oferecer alertas personalizados (queda de preço, novos anúncios) e incentivar o usuário a retornar quando buscar outro carro ou indicar a plataforma para amigos.

5. Que tipo de monetização você considera viável para essa aplicação?

    Além do modelo de assinatura e comissão por venda, consideraria a implementação de recursos premium, como anúncios em destaque, que poderiam ser oferecidos por uma taxa de serviço para vendedores. Também poderia explorar parcerias com empresas de financiamento de veículos, oferecendo serviços financeiros integrados na plataforma, gerando assim uma nova fonte de receita.

6. Há alguma estratégia de retenção de usuários que você aplicaria?

    Implementaria alertas inteligentes e personalizados, como notificações quando novos carros compatíveis aparecem ou quando o preço cai. Ofereceria ferramentas de comparação e histórico de preços para manter o comprador engajado. Criaria uma experiência confiável, com avaliações verificadas dos vendedores e suporte ao cliente, garantindo segurança e incentivando a recompra ou indicação.
