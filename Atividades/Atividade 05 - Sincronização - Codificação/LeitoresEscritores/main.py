# ALUNOS: CARLOS HENRIQUE, CHARLES, EDMARQUES, JORGE MATHEUS.
# ALGORITMO LEITORES/ESCRITORES EM PYTHON, ATIVIDADE 5.

import threading
import time
import random

class LeitorEscritor:
    def __init__(self):
        self.leitores = 0
        self.lock = threading.Lock()
        self.resource = 0

    def ler(self):
        with self.lock:
            self.leitores += 1
            if self.leitores == 1:
                self.resource += 1
            print(f"Leitor lendo: {self.resource}")

    def liberar_leitura(self):
        with self.lock:
            self.leitores -= 1
            if self.leitores == 0:
                self.resource -= 1

    def escrever(self):
        with self.lock:
            self.resource += 1
            print(f"Escritor escrevendo: {self.resource}")

    def liberar_escrita(self):
        with self.lock:
            self.resource -= 1

def leitor(leitor_escritor):
    while True:
        time.sleep(random.uniform(0.1, 1))
        leitor_escritor.ler()
        time.sleep(random.uniform(0.1, 1))
        leitor_escritor.liberar_leitura()

def escritor(leitor_escritor):
    while True:
        time.sleep(random.uniform(0.1, 1))
        leitor_escritor.escrever()
        time.sleep(random.uniform(0.1, 1))
        leitor_escritor.liberar_escrita()

thread_leitor_escritor = LeitorEscritor()
thread_leitor = [threading.Thread(target=leitor, args=(thread_leitor_escritor,)) for _ in range(3)]
thread_escritor = [threading.Thread(target=escritor, args=(thread_leitor_escritor,)) for _ in range(2)]
for thread in thread_leitor:
    thread.start()
for thread in thread_escritor:
    thread.start()
for thread in thread_leitor:
    thread.join()
for thread in thread_escritor:
    thread.join()
