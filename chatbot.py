import webbrowser as wb
import pyautogui as pg 
from time import sleep
import os

def processar_resposta(resposta, nome_completo):
    if resposta == '1':
        nome_social = input(f'{os.linesep}{nome_completo}, para facilitar sua experiência e fornecer informações relevantes de forma rápida e eficiente, como gostaria de ser chamado(a)?{os.linesep}Queremos tratá-lo da melhor forma possível!{os.linesep}')
        
        atua_tjmg = input(f'{os.linesep}Você atua no tjmg?{os.linesep}[ 1 ] Sim{os.linesep}[ 2 ] Não{os.linesep}')
        if atua_tjmg == '1':
            matricula_tjmg = input(f'Informe sua matrícula no Tribunal de Justiça de Minas Gerais.{os.linesep}')
            instancia = input (f'{os.linesep}Você trabalha na 1ª ou 2ª Instância do tjmg?{os.linesep}[ 1 ] 1ª instância{os.linesep}[ 2 ] 2ª instância{os.linesep}')
            comarca = input (f'{os.linesep}Qual é a comarca em que atua?{os.linesep}')
            cargo = input (f'{os.linesep}Qual é o seu cargo ou função na instituição?{os.linesep}')
        elif atua_tjmg == '2':
            publico == str("Público Externo")
        elif atua_tjmg != '1' and atua_tjmg != '2':
            print(f'Opção inválida, gentileza selecionar 1 ou 2')
        
        email = input(f'{os.linesep}Por favor, nos informe um e-mail de contato para envio de informações importantes.{os.linesep}')
        
        celular = input(f'{os.linesep}Qual é o número de celular cadastrado no WhatsApp?{os.linesep}')
        
        intragram = input(f'{os.linesep}Informe seu usuário do Instagram para interagirmos também por lá também!{os.linesep}')
        
        linkedin = input(f'{os.linesep}Informe seu usuário do Linkedin para conectarmos profissionalmente.!{os.linesep}')
        
        print(f'{os.linesep}Obrigada pelo envio das informações, com elas posso oferecer um atendimento mais personalizado e eficiente a você.')
        
        assunto = input(f'{os.linesep}Deseja tratar sobre qual assunto? Seleciona entre as opções a seguir:{os.linesep}[ 1 ] Cursos Para se Inscrever {os.linesep}[ 2 ] Cursos em Andamento{os.linesep}[ 3 ] Cursos Encerrados{os.linesep}[ 4 ] Palestras{os.linesep}[ 5 ] Seminários{os.linesep}[ 6 ] Pós-graduação{os.linesep}[ 7 ] Suporte técnico{os.linesep}[ 8 ] Voltar ao Menu Anterior {os.linesep}[ 9 ] Sair{os.linesep}')        
        if assunto == '1':
            print(f'Para consultar a lista de Cursos Para se Inscrever, acesse o site da EJEF e SIGA!')
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-para-se-inscrever/')
            print(f'[ 2 ] SIGA - https://siga.tjmg.jus.br/mod/inscricoes/index2.php')
            print(f'[ 3 ] Sair')
        elif assunto == '2':
            print(f'Para consultar a lista de Cursos em Andamento, acesse o site da EJEF e SIGA!')
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-em-andamento/')
            print(f'[ 2 ] Painel do Estudante SIGA - https://siga.tjmg.jus.br/mod/paineldoestudante.php/')
            print(f'[ 3 ] Moodle Campus 2 - https://ead2.tjmg.jus.br/campus2/')
            print(f'[ 4 ] Moodle Campus 3 - https://ead2.tjmg.jus.br/campus3/')
            print(f'[ 5 ] Sair')
        elif assunto == '3':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '4':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '5':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '6':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '7':
            print(f'voltar ao menu anterior')       
        elif assunto == '8':
            print(f'sair')        
        elif assunto == '9':
            print(f'Obrigada e volte sempre!')            
        else:
            print('Opção inválida, gentileza escolher as opções entre 1 e 9')
    
    if resposta == '2':
        assunto = input(f'{os.linesep}Deseja tratar sobre qual assunto? Seleciona entre as opções a seguir:{os.linesep}[ 1 ] Cursos Para se Inscrever {os.linesep}[ 2 ] Cursos em Andamento{os.linesep}[ 3 ] Cursos Encerrados{os.linesep}[ 4 ] Palestras{os.linesep}[ 5 ] Seminários{os.linesep}[ 6 ] Pós-graduação{os.linesep}[ 7 ] Suporte técnico{os.linesep}[ 8 ] Voltar ao Menu Anterior {os.linesep}[ 9 ] Sair{os.linesep}')
        if assunto == '1':
            print(f'Para consultar a lista de Cursos Para se Inscrever, acesse o site da EJEF e SIGA!')
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-para-se-inscrever/')
            print(f'[ 2 ] SIGA - https://siga.tjmg.jus.br/mod/inscricoes/index2.php')
            print(f'[ 3 ] Sair')
        elif assunto == '2':
            print(f'Para consultar a lista de Cursos em Andamento, acesse o site da EJEF e SIGA!')
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-em-andamento/')
            print(f'[ 2 ] Painel do Estudante SIGA - https://siga.tjmg.jus.br/mod/paineldoestudante.php/')
            print(f'[ 3 ] Moodle Campus 2 - https://ead2.tjmg.jus.br/campus2/')
            print(f'[ 4 ] Moodle Campus 3 - https://ead2.tjmg.jus.br/campus3/')
            print(f'[ 5 ] Sair')
        elif assunto == '3':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '4':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '5':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '6':
            print(f'Para consultar a lista de Cursos Encerrados, acesse o site da EJEF e SIGA!') 
            print(f'[ 1 ] Site EJEF - https://ejef.tjmg.jus.br/topicos/cursos/cursos-encerrados/')
            print(f'[ 2 ] Certificados SIGA - https://siga.tjmg.jus.br/certificadosvirtuais/')
            print(f'[ 3 ] Sair')
        elif assunto == '7':
            print(f'voltar ao menu anterior')       
        elif assunto == '8':
            print(f'sair')        
        elif assunto == '9':
            print(f'sair')            
        else:
            print(f'Opção inválida, gentileza escolher as opções entre 1 e 9')

contatos = ['dashboard/contatos.xlsx']

print('Olá, eu sou o atendente virtual automatizado da EJEF!')
print('Seja bem-vindo(a)!')
sleep(3)
nome_completo = input(f'{os.linesep}Qual o seu nome completo?{os.linesep}')
while True:
    resposta = input(f'{nome_completo}, antes de começarmos, já se cadastrou para receber nossas novidades?! Há muitas ações educacionais disponíveis para todos os públicos! {os.linesep}Deseja realizar o seu cadastro?{os.linesep}[ 1 ] Cadastrar agora!{os.linesep}[ 2 ] Já estou cadastrado(a)!{os.linesep}')
    processar_resposta(resposta,nome_completo)