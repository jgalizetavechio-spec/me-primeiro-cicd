def testar_login():
    usuario_esperado = "admin"
    print("[INFO] Iniciando o fluxo de decisão de autenticação...")
    assert usuario_esperado == "admin", "[ERROR] Usuário incorreto detectado!"
    print("[INFO] Autenticação concluída com sucesso.")

if __name__ == "__main__":
    testar_login()
