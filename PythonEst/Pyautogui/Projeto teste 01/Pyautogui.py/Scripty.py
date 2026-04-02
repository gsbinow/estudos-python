import pyautogui
import time
from functools import wraps


# --- FERRAMENTA DE CRONÔMETRO ---
def monitorar_etapa(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        print(f"🚀 Iniciando: {funcao.__name__.replace('_', ' ').title()}...")
        
        resultado = funcao(*args, **kwargs)
        
        fim = time.time()
        duracao = fim - inicio
        print(f"⏱️ Concluído em: {duracao:.2f}s\n" + "-"*30)
        return resultado
    return wrapper

# --- AÇÕES DO PROJETO (MODULARIZADO) ---


@monitorar_etapa
def abrir_navegador(nome_app):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write(nome_app)
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('win', 'up') # Maximizar

@monitorar_etapa
def acessar_url(url):
    # Clica na barra de endereços ou garante foco antes de digitar
    pyautogui.click(x=756, y=619) 
    pyautogui.write(url)
    pyautogui.press('enter')
    # Tempo de espera para o portal carregar (o ponto crítico da internet)
    time.sleep(6) 

@monitorar_etapa
def realizar_login(usuario, senha):
    pyautogui.write(usuario)
    pyautogui.press('tab')
    pyautogui.write(senha)
    pyautogui.press('tab')
    pyautogui.press('enter')

@monitorar_etapa
def busca_rme():
    time.sleep(5)
    pyautogui.click( x = 1122, y = 779 ) #Clique em ok
    pyautogui.click( x = 396, y= 244 ) 
    pyautogui.click( x = 327, y = 914 )
    pyautogui.click( x = 313, y = 567 )
  














# --- EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    print("🤖 INICIANDO AUTOMAÇÃO DE SUPRIMENTOS\n" + "="*30)
    
    abrir_navegador("Chrome")
    acessar_url('http://suprimentos.pma.es.gov.br:91/pma/')
    realizar_login('gbinow', '#######')
    busca_rme()
    
    print("✅ Processo finalizado com sucesso!")