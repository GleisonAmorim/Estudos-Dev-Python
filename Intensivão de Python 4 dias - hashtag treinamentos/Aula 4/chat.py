''' Organizando ideias 

Titulo
    botão de iniciar o chat
        popup
            Bem vindo
            escreva seu nome
            entrar no chat
Chat
    fulano entrou no chat
    mensagens do usuário
campo para enviar mensagem
botão de enviar

Sempre que for criar app ou site com flet seguir os três passos abaixo
1 importar o flat
2 criar a função principal do app
3 passa o nome da função para o flet.app para rodar o app chamando a função'''

import flet as ft #importando flet e apelidando de ft

def main(pagina): 
    texto = ft.Text("Communication") #criando o texto que é exibido quando a pagina inicial se abre
    
    nome_usuario = ft.TextField(label="Digite o seu nome") #campo de input para receber o nome do usuário
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes)) #adiciona ao campo o texto da menagem enviada
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel) #cria um canal para duas pessoas se comunicarem
    
    def enviar_mensagem(evento):#cria o evento de enviar mensagem
        texto_campo_mensgem = f" {nome_usuario.value}:  {campo_mensagem.value}" #texto do campo de mensagem recebe o valor que foi enviado
                                                                                #coloca o nome do usuário que enviou a mensagem
        pagina.pubsub.send_all(texto_campo_mensgem)
        campo_mensagem.value="" #limpa o campo mensagem
        pagina.update()
        
    campo_mensagem = ft.TextField(label="Envie sua mensagem", #cria o campo de enviar mensagem
                                on_submit=enviar_mensagem)    #e habilita a função de enviar com enter (on_submit)        
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) #cria botão de enviar mensagem
    
    def entrar_chat(evento): #cria a função de entrar no chat
        popup.open=False #fecha o popup
        pagina.remove(botao_iniciar) #remove o botão iniciar chat
        pagina.add(chat) #adiciona o chat
        linha_mensagem = ft.Row(             #adiciona o campo de mensagem e o botão enviar dentro de uma linha
            [campo_mensagem, botao_enviar]   #para ficar o campo de mensagem ao lado o botão     
        )
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()
    
    popup = ft.AlertDialog( #cria um popup que começa fechado e abre quando eu clico no botão iniciar chat
        open=False, 
        modal=True, 
        title=ft.Text("Bem vind@ ao Communication"), #texto em cima da caixa
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)] #cria o botão entrar no chat
        )

    def iniciar_chat(evento): #criando a função do botão iniciar chat
        pagina.dialog = popup
        popup.open=True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat) # criando o botão iniciar chat

    pagina.add(texto) #adicionando o texto a página inicial   
    pagina.add(botao_iniciar) #adicionando o botão iniciar chat

ft.app(main) #formato de aplicativo
#ft.app(main, view=ft.WEB_BROWSER) # FORMATO DE SITE
