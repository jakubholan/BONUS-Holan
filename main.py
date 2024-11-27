while True:
    #Vytvoří vstup pro daného uživatele
    vek = input("Zadej svůj věk (celočíselná hodnota): ")

    #Kontroluje zda je zdaná hodnot celočíselná
    if vek.isdigit():
        print("Děkujeme")
        break #Ukončuje cyklus pokud je ovšem cyklus správný
    else:
        print("Zadej pouze celočíselnou hodnotu.") 