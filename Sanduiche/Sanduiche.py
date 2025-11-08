def mostrar_menu():
    print("\n" + "=" * 35)
    print("     MONTADOR DE SANDUÍCHE")
    print("=" * 35)
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente")
    print("4 - Mostrar sanduíche")
    print("5 - Finalizar pedido")
    print("=" * 35)

def main():
    pilha_sanduiche = []
    
    print("Bem-vindo ao Montador de Sanduíche!")
    print("Monte seu sanduíche camada por camada!")
    
    while True:
        mostrar_menu()
        opcao = input("\nDigite a opção desejada (1-5): ").strip()
        
        if opcao == "1":
            # Adicionar ingrediente
            ingrediente = input("Digite o nome do ingrediente: ").strip()
            if ingrediente:
                pilha_sanduiche.append(ingrediente)
                print(f"✓ '{ingrediente}' adicionado!")
            else:
                print("❌ Nenhum ingrediente informado.")
        
        elif opcao == "2":
            # Remover ingrediente do topo
            if not pilha_sanduiche:
                print("❌ Sanduíche vazio! Nada para remover.")
            else:
                removido = pilha_sanduiche.pop()
                print(f"✓ '{removido}' removido!")
        
        elif opcao == "3":
            # Ver último ingrediente
            if not pilha_sanduiche:
                print("❌ Sanduíche vazio!")
            else:
                print(f"📌 Último ingrediente: '{pilha_sanduiche[-1]}'")
        
        elif opcao == "4":
            # Mostrar sanduíche completo
            if not pilha_sanduiche:
                print("🍞 Sanduíche vazio! Adicione ingredientes.")
            else:
                print("\n" + "=" * 35)
                print("     SEU SANDUÍCHE")
                print("=" * 35)
                print("Ordem (base → topo):")
                for i, ingrediente in enumerate(pilha_sanduiche, 1):
                    print(f"{i}º - {ingrediente}")
                print(f"Total: {len(pilha_sanduiche)} ingredientes")
        
        elif opcao == "5":
            # Finalizar pedido
            if pilha_sanduiche:
                print("\n🎉 PEDIDO FINALIZADO!")
                print(f"Seu sanduíche tem {len(pilha_sanduiche)} ingredientes")
                print("🍔 Aproveite!")
            else:
                print("\n❌ Pedido cancelado! Sanduíche vazio.")
            break
        
        else:
            print("❌ Opção inválida! Digite 1-5.")

# Executar o programa
if __name__ == "__main__":
    main()