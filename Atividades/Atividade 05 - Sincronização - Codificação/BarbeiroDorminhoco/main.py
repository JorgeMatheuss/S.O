# ALUNOS: CARLOS HENRIQUE, CHARLES, EDMARQUES, JORGE MATHEUS.
# ALGORITMO DO BARBEIRO DORMINHOCO EM PYTHON, ATIVIDADE 5.

import threading
import time
import random
class Barbearia:
    def __init__(self, cadeiras):
        self.cadeiras = cadeiras
        self.clientes = 0
        self.barbeiro_dormindo = True
        self.lock = threading.Lock()
        self.estado_barbeiro = threading.Condition(self.lock)
        self.estado_cliente = threading.Condition(self.lock)

    def barbeiro(self):
        while True:
            with self.lock:
                if self.clientes == 0:
                    print("Barbeiro dormindo...")
                    self.barbeiro_dormindo = True
                    self.estado_barbeiro.wait()
                self.clientes -= 1
                print("Barbeiro está cortando cabelo.")
            time.sleep(random.uniform(0.1, 1))

    def cliente(self):
        while True:
            with self.lock:
                if self.clientes < self.cadeiras:
                    self.clientes += 1
                    print("O cliente chegou!")
                    if self.barbeiro_dormindo:
                        print("Acordando o barbeiro!")
                        self.estado_barbeiro.notify()
                        self.barbeiro_dormindo = False
                    self.estado_cliente.wait()

def barbearia_thread():
    barbearia = Barbearia(3) 
    thread_barbeiro = threading.Thread(target=barbearia.barbeiro)
    thread_cliente = [threading.Thread(target=barbearia.cliente) for _ in range(5)]

    thread_barbeiro.start()
    for thread in thread_cliente:
        thread.start()

    thread_barbeiro.join()
    for thread in thread_cliente:
        thread.join()
barbearia_thread()