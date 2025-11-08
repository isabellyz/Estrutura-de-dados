def mostrar_menu_navegacao():
    print("\n" + "=" * 45)
    print("        SISTEMA DE NAVEGAÇÃO WEB")
    print("=" * 45)
    print("1 - Visitar nova página")
    print("2 - Voltar à página anterior")
    print("3 - Ver página atual")
    print("4 - Mostrar histórico de navegação")
    print("5 - Limpar histórico")
    print("6 - Sair do navegador")
    print("=" * 45)

def sistema_navegacao_web():
    pilha_historico = []
    pagina_atual = "Página Inicial"
    
    print("🚀 Bem-vindo ao Sistema de Navegação Web!")
    print("Navegue pelas páginas usando o sistema de pilha.")
    
    while True:
        mostrar_menu_navegacao()
        opcao = input("\nDigite a opção desejada (1-6): ").strip()
        
        if opcao == "1":
            # Visitar nova página
            if pagina_atual != "Página Inicial":
                pilha_historico.append(pagina_atual)
            
            nova_pagina = input("Digite o nome da nova página: ").strip()
            if nova_pagina:
                pagina_atual = nova_pagina
                print(f"🌐 Navegando para: '{pagina_atual}'")
            else:
                print("❌ Nome da página não pode estar vazio!")
        
        elif opcao == "2":
            # Voltar à página anterior
            if not pilha_historico:
                print("❌ Não há páginas anteriores no histórico!")
            else:
                pagina_anterior = pilha_historico.pop()
                print(f"↩️ Voltando de '{pagina_atual}' para '{pagina_anterior}'")
                pagina_atual = pagina_anterior
        
        elif opcao == "3":
            # Ver página atual
            print(f"📄 Página atual: '{pagina_atual}'")
        
        elif opcao == "4":
            # Mostrar histórico de navegação
            if not pilha_historico:
                print("📋 Histórico vazio! Nenhuma página visitada anteriormente.")
            else:
                print("\n" + "=" * 45)
                print("        HISTÓRICO DE NAVEGAÇÃO")
                print("=" * 45)
                print("Ordem (mais antiga → mais recente):")
                print("-" * 45)
                
                for i, pagina in enumerate(pilha_historico, 1):
                    print(f"{i}º - {pagina}")
                
                print("-" * 45)
                print(f"Total de páginas no histórico: {len(pilha_historico)}")
                print(f"Página atual: {pagina_atual}")
        
        elif opcao == "5":
            # Limpar histórico
            if not pilha_historico:
                print("✅ Histórico já está vazio!")
            else:
                paginas_removidas = len(pilha_historico)
                pilha_historico.clear()
                print(f"🗑️ Histórico limpo! {paginas_removidas} páginas removidas.")
        
        elif opcao == "6":
            # Sair do navegador
            print("\n" + "=" * 45)
            print("         SESSÃO FINALIZADA")
            print("=" * 45)
            print(f"📊 Resumo da sessão:")
            print(f"   - Página final: '{pagina_atual}'")
            print(f"   - Páginas no histórico: {len(pilha_historico)}")
            print("👋 Obrigado por usar nosso navegador!")
            break
        
        else:
            print("❌ Opção inválida! Por favor, digite um número de 1 a 6.")

def demonstrar_pilha():
    print("\n" + "🔍 DEMONSTRAÇÃO DO CONCEITO DE PILHA (LIFO)")
    print("=" * 50)
    
    pilha_exemplo = []
    operacoes = [
        ("Adicionar", "Página 1"),
        ("Adicionar", "Página 2"), 
        ("Adicionar", "Página 3"),
        ("Remover", ""),
        ("Adicionar", "Página 4"),
        ("Remover", ""),
        ("Remover", "")
    ]
    
    print("Operações na pilha:")
    for operacao, valor in operacoes:
        if operacao == "Adicionar":
            pilha_exemplo.append(valor)
            print(f"→ PUSH('{valor}') → Pilha: {pilha_exemplo}")
        else:
            if pilha_exemplo:
                removido = pilha_exemplo.pop()
                print(f"← POP() = '{removido}' → Pilha: {pilha_exemplo}")
    
    print("\n💡 LIFO = Last In, First Out")
    print("   O último elemento adicionado é o primeiro a ser removido!")

if __name__ == "__main__":
    demonstrar_pilha()
    print("\n" + "=" * 60)
    sistema_navegacao_web()