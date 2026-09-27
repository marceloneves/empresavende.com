"""Gera /termos-de-uso/, /politica-de-privacidade/ e /404.html reaproveitando o topo e o rodapé do index.html.
Rode de novo após mudar o header/footer da home:  python3 scripts/build-legal.py"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
home = (ROOT / 'index.html').read_text(encoding='utf-8')

def grab(tag):
    return re.search(rf'    <{tag} class="(?:header|footer)".*?</{tag}>', home, re.S).group(0)

def absolutize(html):
    html = re.sub(r'href="#topo"', 'href="/"', html)
    html = re.sub(r'href="#', 'href="/#', html)
    html = html.replace('src="favicon.svg"', 'src="/favicon.svg"').replace(' aria-current="page"', '')
    return html

header, footer = absolutize(grab('header')), absolutize(grab('footer'))

EMPRESA = 'PMTurbo'
CNPJ = '54.008.386/0001-07'
ENDERECO = 'Rua Desembargador Vítor Lima, 260, Sala 214, Trindade, Florianópolis/SC, CEP 88040-401'
EMAIL = 'contato@pmturbo.com'
TELEFONE = '(48) 98810-5199'
ATUALIZADO = '27 de setembro de 2026'

IDENT = f'''<div class="legal__card">
            <p><b>{EMPRESA}</b> · CNPJ {CNPJ}</p>
            <p>{ENDERECO}</p>
            <p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a> · Telefone/WhatsApp: {TELEFONE}</p>
          </div>'''

TERMOS = f'''
<p class="legal__intro">Estes Termos de Uso regulam o acesso e o uso do <b>EmpresaVende</b>, sistema de gestão para empresas de serviço disponível em empresavende.com e app.empresavende.com. Ao criar uma conta ou usar o sistema, você concorda com estes termos.</p>

<h2 id="t1">1. Quem somos</h2>
<p>O EmpresaVende é um produto desenvolvido e operado pela {EMPRESA}, doravante “PMTurbo” ou “nós”:</p>
{IDENT}

<h2 id="t2">2. Definições</h2>
<ul>
  <li><b>Plataforma:</b> o sistema EmpresaVende, incluindo o painel web e o aplicativo instalável no celular (PWA).</li>
  <li><b>Contratante:</b> a empresa (pessoa jurídica ou profissional autônomo) que cria a conta e contrata um plano.</li>
  <li><b>Usuários:</b> as pessoas a quem o Contratante dá acesso (administrador, comercial, técnico, financeiro).</li>
  <li><b>Dados do Contratante:</b> todas as informações cadastradas na Plataforma, como clientes, oportunidades, orçamentos, agendas, ordens de serviço, fotos e comprovantes.</li>
</ul>

<h2 id="t3">3. Conta e acesso</h2>
<ul>
  <li>A conta é criada por um responsável com poderes para representar o Contratante, que se torna o administrador da organização.</li>
  <li>O segmento de atuação escolhido na criação da conta define o vocabulário, o catálogo inicial, o checklist e o comprovante do serviço, e <b>não pode ser alterado depois</b>.</li>
  <li>O Contratante é responsável por manter as informações de cadastro corretas, por guardar as senhas em sigilo e por todas as ações feitas pelos Usuários que cadastrar.</li>
  <li>O administrador pode criar, alterar e desativar Usuários a qualquer momento. O número de Usuários é ilimitado em todos os planos.</li>
</ul>

<h2 id="t4">4. Planos, período de teste e pagamento</h2>
<ul>
  <li>Os planos diferem pelo <b>limite de orçamentos</b> e têm os valores divulgados em <a href="/#precos">empresavende.com/#precos</a>, que podem ser pagos mensal ou anualmente.</li>
  <li>Pode ser oferecido um período de teste gratuito. Ao final dele, o uso continuado depende da contratação de um plano.</li>
  <li>Os valores são cobrados antecipadamente, a cada ciclo. Em caso de atraso, o acesso poderá ser limitado ou suspenso após aviso, até a regularização.</li>
  <li>O Contratante pode mudar de plano a qualquer momento. Se o volume de orçamentos ultrapassar o limite do plano, poderemos solicitar a mudança para um plano compatível.</li>
  <li>Os valores podem ser reajustados, com aviso prévio de pelo menos 30 dias. O reajuste vale a partir do ciclo seguinte ao aviso.</li>
</ul>

<h2 id="t5">5. Cancelamento</h2>
<ul>
  <li>Não há fidelidade: o Contratante pode cancelar a qualquer momento, e o acesso continua até o fim do período já pago. Não há reembolso proporcional de períodos em curso, salvo quando exigido por lei.</li>
  <li>Após o cancelamento, os Dados do Contratante ficam disponíveis para exportação mediante solicitação por 30 dias e depois são excluídos, salvo obrigação legal de guarda.</li>
  <li>A PMTurbo pode suspender ou encerrar contas que violem estes termos, com aviso prévio sempre que possível.</li>
</ul>

<h2 id="t6">6. Uso permitido</h2>
<p>É proibido usar a Plataforma para:</p>
<ul>
  <li>atividades ilegais, fraudulentas ou que violem direitos de terceiros;</li>
  <li>cadastrar dados pessoais sem base legal ou enviar comunicações não solicitadas (spam);</li>
  <li>tentar acessar dados de outras empresas, burlar limites de plano ou mecanismos de segurança;</li>
  <li>copiar, revender, fazer engenharia reversa ou sobrecarregar a Plataforma de forma automatizada.</li>
</ul>

<h2 id="t7">7. Dados do Contratante</h2>
<ul>
  <li>Os Dados do Contratante <b>pertencem ao Contratante</b>. A PMTurbo os utiliza apenas para prestar o serviço, conforme a <a href="/politica-de-privacidade/">Política de Privacidade</a>.</li>
  <li>Cada empresa tem seus dados isolados das demais. Nenhum Usuário de uma empresa tem acesso aos dados de outra.</li>
  <li>Para os dados pessoais dos clientes cadastrados, o Contratante é o <b>controlador</b> e a PMTurbo atua como <b>operadora</b>, nos termos da Lei nº 13.709/2018 (LGPD). Cabe ao Contratante ter base legal para o tratamento e atender os titulares.</li>
</ul>

<h2 id="t8">8. Disponibilidade e suporte</h2>
<ul>
  <li>Trabalhamos para manter a Plataforma disponível 24 horas por dia, mas podem ocorrer interrupções para manutenção, atualizações ou por falhas de terceiros (hospedagem, internet, provedores de e-mail).</li>
  <li>A Plataforma é atualizada continuamente. Funcionalidades podem ser melhoradas, alteradas ou descontinuadas, preservando o acesso aos dados já cadastrados.</li>
  <li>O suporte é prestado pelos canais informados neste documento, em dias úteis e horário comercial.</li>
</ul>

<h2 id="t9">9. Propriedade intelectual</h2>
<p>O software, a marca EmpresaVende, os layouts, os textos e os modelos (catálogos, checklists e comprovantes padrão) pertencem à PMTurbo. A contratação dá ao Contratante uma licença de uso não exclusiva e intransferível, válida enquanto o plano estiver ativo.</p>

<h2 id="t10">10. Responsabilidades</h2>
<ul>
  <li>A PMTurbo não se responsabiliza pelo conteúdo cadastrado pelos Usuários, pelos serviços prestados pelo Contratante aos seus clientes nem por decisões tomadas com base nas informações do sistema.</li>
  <li>Os comprovantes, certificados e demais documentos emitidos pela Plataforma são de responsabilidade do Contratante, que deve conferir se atendem às exigências do seu segmento.</li>
  <li>Na máxima extensão permitida pela lei, a responsabilidade total da PMTurbo fica limitada ao valor pago pelo Contratante nos 12 meses anteriores ao fato.</li>
</ul>

<h2 id="t11">11. Alterações destes termos</h2>
<p>Estes termos podem ser atualizados. Mudanças relevantes serão comunicadas por e-mail ou dentro da Plataforma com pelo menos 15 dias de antecedência. Continuar usando a Plataforma depois disso significa concordar com a nova versão.</p>

<h2 id="t12">12. Lei aplicável e foro</h2>
<p>Estes termos são regidos pelas leis brasileiras. Fica eleito o foro da Comarca de Florianópolis/SC para resolver qualquer questão, ressalvado o direito do consumidor de propor ação no foro do seu domicílio.</p>

<h2 id="t13">13. Contato</h2>
<p>Dúvidas sobre estes termos: <a href="mailto:{EMAIL}">{EMAIL}</a> ou {TELEFONE}.</p>
'''

PRIVACIDADE = f'''
<p class="legal__intro">Esta Política explica como a {EMPRESA} coleta, usa, compartilha e protege dados pessoais no <b>EmpresaVende</b> (empresavende.com e app.empresavende.com), de acordo com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018, “LGPD”).</p>

<h2 id="p1">1. Quem é o responsável</h2>
{IDENT}
<p>A PMTurbo tem dois papéis diferentes:</p>
<ul>
  <li><b>Controladora</b> dos dados das empresas contratantes e dos seus usuários (cadastro, login, cobrança, suporte) e dos visitantes deste site.</li>
  <li><b>Operadora</b> dos dados que as empresas contratantes cadastram sobre os clientes delas (nome, contato, endereço, histórico de serviços). Nesse caso, a <b>controladora é a empresa contratante</b>, e a PMTurbo trata os dados apenas conforme as instruções dela e para prestar o serviço.</li>
</ul>

<h2 id="p2">2. Quais dados tratamos</h2>
<ul>
  <li><b>Cadastro da conta:</b> nome da empresa, segmento, nome, e-mail e telefone do responsável e dos usuários, senha (guardada de forma criptografada) e perfil de acesso.</li>
  <li><b>Dados cadastrados pela empresa:</b> clientes, endereços, oportunidades, atividades, orçamentos, agendas, ordens de serviço, checklists, fotos, observações e comprovantes.</li>
  <li><b>Dados de contratação:</b> plano, histórico de pagamentos e dados de faturamento.</li>
  <li><b>Dados técnicos:</b> endereço IP, data e hora de acesso, tipo de navegador e dispositivo, e registros de alterações feitas no sistema (auditoria).</li>
  <li><b>Contato:</b> informações enviadas por e-mail, WhatsApp ou pelos formulários de contato.</li>
</ul>

<h2 id="p3">3. Para que usamos e com qual base legal</h2>
<ul>
  <li><b>Prestar o serviço</b> (criar a conta, autenticar, armazenar e exibir os dados, enviar comprovantes por e-mail): execução de contrato.</li>
  <li><b>Cobrança e obrigações fiscais:</b> cumprimento de obrigação legal e execução de contrato.</li>
  <li><b>Segurança, prevenção a fraudes e registros de acesso:</b> legítimo interesse e cumprimento do Marco Civil da Internet (Lei nº 12.965/2014).</li>
  <li><b>Suporte e comunicações sobre o serviço</b> (avisos de atualização, mudanças de plano ou destes documentos): execução de contrato e legítimo interesse.</li>
  <li><b>Comunicações de marketing:</b> somente com consentimento, que pode ser retirado a qualquer momento.</li>
</ul>
<p>Não vendemos dados pessoais e não usamos os dados cadastrados pelas empresas para publicidade.</p>

<h2 id="p4">4. Com quem compartilhamos</h2>
<p>Compartilhamos dados apenas com fornecedores necessários para o funcionamento do serviço, que seguem obrigações de segurança e confidencialidade:</p>
<ul>
  <li><b>Hospedagem, banco de dados e armazenamento de arquivos</b> (infraestrutura em nuvem);</li>
  <li><b>Envio de e-mails</b> (entrega dos comprovantes e avisos do sistema);</li>
  <li><b>Meios de pagamento</b>, para processar as cobranças;</li>
  <li><b>Autoridades públicas</b>, quando exigido por lei ou ordem judicial.</li>
</ul>
<p>Alguns desses fornecedores podem armazenar dados em servidores fora do Brasil. Nesses casos, a transferência internacional segue as hipóteses do art. 33 da LGPD, com garantias contratuais de proteção.</p>

<h2 id="p5">5. Como protegemos</h2>
<ul>
  <li>Isolamento dos dados por empresa diretamente no banco de dados: usuários de uma empresa não acessam dados de outra.</li>
  <li>Controle de acesso por perfil (administrador, comercial, técnico, financeiro).</li>
  <li>Conexões criptografadas (HTTPS) e senhas guardadas com criptografia.</li>
  <li>Fotos em armazenamento privado, acessadas somente por links temporários.</li>
  <li>Registro de auditoria das alterações feitas no sistema.</li>
</ul>
<p>Nenhum sistema é 100% seguro. Se ocorrer um incidente de segurança que possa causar risco ou dano relevante, avisaremos os afetados e a Autoridade Nacional de Proteção de Dados (ANPD), conforme a lei.</p>

<h2 id="p6">6. Por quanto tempo guardamos</h2>
<ul>
  <li>Os dados da conta e os dados cadastrados pela empresa são mantidos enquanto o plano estiver ativo.</li>
  <li>Após o cancelamento, ficam disponíveis para exportação por 30 dias e depois são excluídos.</li>
  <li>Registros de acesso são guardados por 6 meses (Marco Civil da Internet), e dados fiscais e de cobrança pelo prazo exigido pela legislação.</li>
</ul>

<h2 id="p7">7. Cookies e armazenamento no navegador</h2>
<p>O sistema usa o armazenamento local do navegador para manter você conectado, lembrar preferências (como o tema claro ou escuro) e permitir o funcionamento do aplicativo instalado no celular. Este site usa fontes do Google Fonts, carregadas a partir dos servidores do Google. Não usamos cookies de publicidade.</p>

<h2 id="p8">8. Seus direitos</h2>
<p>Pela LGPD, você pode solicitar:</p>
<ul>
  <li>confirmação de que tratamos seus dados e acesso a eles;</li>
  <li>correção de dados incompletos, inexatos ou desatualizados;</li>
  <li>anonimização, bloqueio ou eliminação de dados desnecessários ou tratados em desconformidade;</li>
  <li>portabilidade dos dados;</li>
  <li>informação sobre com quem compartilhamos seus dados;</li>
  <li>revogação do consentimento, quando essa for a base legal.</li>
</ul>
<p>Os pedidos são respondidos em até 15 dias. Se você é <b>cliente de uma empresa que usa o EmpresaVende</b>, faça o pedido diretamente a essa empresa, que é a controladora dos seus dados. Nós a apoiaremos para atender você.</p>

<h2 id="p9">9. Encarregado de dados (DPO)</h2>
<p>O canal para assuntos de privacidade e proteção de dados é <a href="mailto:{EMAIL}">{EMAIL}</a>. Você também pode reclamar à ANPD.</p>

<h2 id="p10">10. Crianças e adolescentes</h2>
<p>O EmpresaVende é destinado a empresas e não é direcionado a menores de 18 anos.</p>

<h2 id="p11">11. Alterações desta política</h2>
<p>Esta Política pode ser atualizada. A data da última atualização aparece no topo da página, e mudanças relevantes serão comunicadas por e-mail ou dentro do sistema.</p>
'''

def toc(body):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    links = '\n'.join(f'            <a href="#{i}">{t}</a>' for i, t in items)
    return f'<nav class="legal__toc" aria-label="Nesta página">\n            <p>Nesta página</p>\n{links}\n          </nav>'

def page(slug, title, description, body, other):
    other_slug, other_title = other
    return f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | EmpresaVende</title>
    <meta name="description" content="{description}" />
    <meta name="theme-color" content="#15803d" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
    <link rel="canonical" href="https://empresavende.com/{slug}/" />
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="pt_BR" />
    <meta property="og:site_name" content="EmpresaVende" />
    <meta property="og:title" content="{title} | EmpresaVende" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="https://empresavende.com/{slug}/" />
    <meta property="og:image" content="https://empresavende.com/og-image.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/styles.css" />
  </head>
  <body>
    <a class="skip" href="#conteudo">Pular para o conteúdo</a>

{header}

    <main id="conteudo">
      <section class="legal-hero">
        <div class="container container--narrow">
          <p class="eyebrow">Legal</p>
          <h1>{title}</h1>
          <p class="legal__updated">Última atualização: {ATUALIZADO}</p>
        </div>
      </section>

      <div class="container legal">
        <aside>
          {toc(body)}
        </aside>
        <article class="legal__body">
{body}
          <p class="legal__see">Veja também: <a href="/{other_slug}/">{other_title}</a></p>
        </article>
      </div>
    </main>

{footer}
  </body>
</html>
'''

for slug, title, desc, body, other in [
    ('termos-de-uso', 'Termos de uso', 'Termos de uso do EmpresaVende, sistema de gestão para empresas de serviço da PMTurbo.', TERMOS, ('politica-de-privacidade', 'Política de privacidade')),
    ('politica-de-privacidade', 'Política de privacidade', 'Como o EmpresaVende, da PMTurbo, trata e protege dados pessoais conforme a LGPD.', PRIVACIDADE, ('termos-de-uso', 'Termos de uso')),
]:
    out = ROOT / slug / 'index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(page(slug, title, desc, body, other), encoding='utf-8')
    print('ok', out.relative_to(ROOT))


# ---------- 404 ----------
NOT_FOUND = f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Página não encontrada | EmpresaVende</title>
    <meta name="robots" content="noindex" />
    <meta name="theme-color" content="#15803d" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/styles.css" />
  </head>
  <body>
{header}

    <main id="conteudo" class="notfound">
      <div class="container container--narrow">
        <p class="notfound__code">404</p>
        <h1>Esta página não existe</h1>
        <p class="lead">O endereço pode ter mudado ou foi digitado errado. Veja por onde continuar:</p>
        <div class="hero__cta">
          <a class="btn btn--primary btn--lg" href="/">Ir para o início</a>
          <a class="btn btn--outline btn--lg" href="/#precos">Ver planos e preços</a>
        </div>
      </div>
    </main>

{footer}
  </body>
</html>
'''
(ROOT / '404.html').write_text(NOT_FOUND, encoding='utf-8')
print('ok 404.html')
