transacoes = []

def adicionar_transacao(tipo, valor, descricao):
    transacoes.append({
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao
    })

def calcular_saldo():
    saldo = 0
    for t in transacoes:
        if t["tipo"] == "receita":
            saldo += t["valor"]
        elif t["tipo"] == "despesa":
            saldo -= t["valor"]
    return saldo

def listar_transacoes():
    print("\nTransações registradas:")
    for t in transacoes:
        print(f"{t['tipo'].capitalize()}: R$ {t['valor']} - {t['descricao']}")

# Exemplo de uso
adicionar_transacao("receita", 1000, "Venda")
adicionar_transacao("despesa", 200, "Aluguel")
adicionar_transacao("despesa", 150, "Internet")

listar_transacoes()
print(f"\nSaldo atual: R$ {calcular_saldo()}")
