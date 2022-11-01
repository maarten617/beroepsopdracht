from queue import PriorityQueue


print("het is 1940 je woond in duitland en hitler komt aan de macht.")
input("wat doe je?")
print("a: je vlucht naar nederland.")
print("b: je sluit je aan bij de nazies.")

choice = input()

if choice =='a':
    input("goede keuzen.Waar in nederland ga je naartoe?.")
    print("a: noord nederland.")
    print("b: zuid nederland.")
    print("c: midden nederland.")

    choice = input()

    if choice == 'a':
        input("oehw noord nederland. goede keuze.")
        input("je moet ergens onderdak vinden waar doe je dat?")
        print("a: je vraagt aan iemand met een groot huis of je een deel van het huis mag huren om tijdelijk in te wonen?")
        print("b: je zoekt naar een klein huur huisje met alleen een bed")
        print("c: je kijkt of je naar een van de eilanden kan gaan om daar te zoeken naar een huisje.")

        choice = input()

        if choice == 'a':
            input("goede keuzen veel mensen zullen een logeer kamer over hebben waar je kan blijven.")
            input("je vind een 3 huisjes met mensen die je wel een kamer willen geven aleen moet je hier natuurlijk wel voor betalen. welke kamer kies je?")
            print("a: je neemt de kamer van 300 euro per maand in je kamer staat een bed en een kast?")
            print("b: je neemt de kamer van 400 euro per maand in je kamer staat hetzelfde als a maar je hoeft niet voor je eigen eten te zorgen je mag gewoon mee eten.")
            print("c: je neemt de kamer van 600 euro die heeft hetzelfde als kamer b maar je hebt nu je eigen douche.")
            
            choice = input()

            if choice == 'a':
                print('fail je bent blut')
            
            if choice == 'b':
                print('fail je bent blut')

            if choice == 'c':
                print('fail je bent blut')
        

        elif choice == 'b':
            input("helaas alle huur huizen zitten vol je bent hier erg boos om en gaat naar de kroeg om je pijn weg te zuipen.")
            input("je komt in een heftig gevecht, slaat een man op zijn hoofd met een stoel en de man sterft hierdoor. de polietie pakt je op en je krijgt levenslang.")
            print("fail!!")


        elif choice == 'c':
            input("een eiland. goede keuze.")
            input("je hebt hier familie waar je kan blijven slapen")
            input("wat ga je doen om ze te bedanken?")
            print("a:niks")
            print("b:je helpt ze zo veel als je kan.")

            choice = input()
            if choice =='a':
                input("ze vinden dat je doet alsof je het niet waardeerd en ze sturen je terug naar duitsland.")
                input("je word neergeschoten als je terug komt in duitsland")
                print("fail!!")
            if choice =='b':
                print("je kan blijven tot je weer terug kan naar duitsland.")
                print("win!!!")

    
    elif choice == 'b':
        input("oehw zuid nederland. goede keuze.")
        input("je moet ergens onderdak vinden waar doe je dat?")
        print("a: je vraagt aan iemand met een groot huis of je een deel van het huis mag huren om tijdelijk in te wonen?")
        print("b: je zoekt naar een klein huur huisje met aleen een bed.")
        print("c: je kijkt of je naar belgië kan gaan om daar te zoeken naar een huisje.")

        choice = input()


        if choice == 'a':
            input("goede keuzen veel mensen zullen een logeer kamer over hebben waar je kan blijven.")
            input("je vind een 3 huisjes met mensen die je wel een kamer willen geven aleen moet je hier natuurlijk wel voor betalen. welke kamer kies je?")
            print("a: je neemt de kamer van 300 euro per maand in je kamer staat een bed en een kast?")
            print("b: je neemt de kamer van 400 euro per maand in je kamer staat hetzelfde als a maar je hoeft niet voor je eigen eten te zorgen je mag gewoon mee eten.")
            print("c: je neemt de kamer van 600 euro die heeft hetzelfde als kamer b maar je hebt nu je eigen douche.")

            choice = input()

            if choice == 'a':
                print('fail je bent blut')
            
            if choice == 'b':
                print('fail je bent blut')

            if choice == 'c':
                print('fail je bent blut')
        
        elif choice == 'b':
            input("helaas alle huur huizen zitten vol je bent hier erg boos om en gaat naar de kroeg om je pijn weg te zuipen.")
            input("je komt in een heftig gevecht, slaat een man op zijn hoofd met een stoel en de man sterft hierdoor. de polietie pakt je op en je krijgt levenslang.")
            print("fail!!")


        elif choice == 'c':
            input("belgië. goede keuze.")
            input("je hebt hier familie waar je kan blijven slapen")
            input("wat ga je doen om ze te bedanken?")
            print("a:niks")
            print("b:je helpt ze zo veel als je kan.")

            choice = input()
            if choice =='a':
                input("ze vinden dat je doet alsof je het niet waardeerd en ze sturen je terug naar duitsland.")
                input("je word neergeschoten als je terug komt in duitsland")
                print("fail!!")
            if choice =='b':
                print("je kan blijven tot je weer terug kan naar duitsland.")
                print("win!!!")

    elif choice == 'c':
        input("oehw midden nederland. riskante keuze.")
        input("je moet ergens onderdak vinden waar doe je dat?")
        input("nergens alle huizen in midden nederland zijn te duur voor jou budget wat doe je er aan?")
        print("a: je gaat naar noord nederland.")
        print("b: je gaat naar zuid nederland.")
        print("c: je gaat terug naar duitsland en hoopt dat het minder erg was dan je had verwacht.")
        
        choice = input()

        if choice == 'a':
            input("oehw noord nederland. goede keuze.")
            input("je moet ergens onderdak vinden waar doe je dat?")
            print("a: je vraagt aan iemand met een groot huis of je een deel van het huis mag huren om tijdelijk in te wonen?")
            print("b: je zoekt naar een klein huur huisje met aleen een bed.")
            print("c: je kijkt of je naar belgië kan gaan om daar te zoeken naar een huisje.")

            choice = input()

            if choice == 'a':
                input("goede keuzen veel mensen zullen een logeer kamer over hebben waar je kan blijven.")
                input("je vind een 3 huisjes met mensen die je wel een kamer willen geven aleen moet je hier natuurlijk wel voor betalen. welke kamer kies je?")
                print("a: je neemt de kamer van 300 euro per maand in je kamer staat een bed en een kast?")
                print("b: je neemt de kamer van 400 euro per maand in je kamer staat hetzelfde als a maar je hoeft niet voor je eigen eten te zorgen je mag gewoon mee eten.")
                print("c: je neemt de kamer van 600 euro die heeft hetzelfde als kamer b maar je hebt nu je eigen douche.")
            
                choice = input()

                if choice == 'a':
                    print('fail je bent blut')
            
                if choice == 'b':
                    print('fail je bent blut')

                if choice == 'c':
                    print('fail je bent blut')    
                    
            elif choice == 'b':
                input("helaas alle huur huizen zitten vol je bent hier erg boos om en gaat naar de kroeg om je pijn weg te zuipen.")
                input("je komt in een heftig gevecht, slaat een man op zijn hoofd met een stoel en de man sterft hierdoor. de polietie pakt je op en je krijgt levenslang.")
                print("fail!!")


            elif choice == 'c':
                input("belgie. goede keuze.")
                input("je hebt hier familie waar je kan blijven slapen")
                input("wat ga je doen om ze te bedanken?")
                print("a:niks")
                print("b:je helpt ze zo veel als je kan.")

                choice = input()
                if choice =='a':
                    input("ze vinden dat je doet alsof je het niet waardeerd en ze sturen je terug naar duitsland.")
                    input("je word neergeschoten als je terug komt in duitsland")
                    print("fail!!")
                if choice =='b':
                    print("je kan blijven tot je weer terug kan naar duitsland.")
                    print("win!!!")

    elif choice == 'b':
            input("oehw zuid nederland. goede keuze.")
            input("je moet ergens onderdak vinden waar doe je dat?")
            print("a: je vraagt aan iemand met een groot huis of je een deel van het huis mag huren om tijdelijk in te wonen?")
            print("b: je zoekt naar een klein huur huisje met aleen een bed.")
            print("c: je kijkt of je naar belgië kan gaan om daar te zoeken naar een huisje.")

    elif choice == 'c':
            input("oei je word gezien als een verrader en word ter plekker geëxuciteerd.")
            input("fail!!")

elif choice =='b':
    input("nice!! goede keuzen. Wat ga je als eerst doen om hitler te helpen")
    print("a:je sluit je aan bij de luchtmacht.")
    print("b:je sluit je aan bij de landmacht.")
    print("c:je sluit je aan bij de marine.")
    choice = input()
    
    if choice == 'a':
        input("de luchtmacht goede keuzen. Wat wil je doen bij de luchtmacht?")
        print("a: leren vliegen.")
        print("b: leren onderhouden/repareren van een vliegtuig.")

        choice = input()

        if choice =='a':
            input("je vliegtuig stort neer")
            print("fail!!!")
        if choice =='b':
            input("je bent verkeerd geinformeerd en je blaast perongeluk een vliegtuig motor op")
            input("fail!!")
        
    if choice == 'b':
        input("de landmacht goede keuze. Wat wil je doen bij de landmacht?")
        print("a:leren een tank te besturen.")
        print("b:leren om een sluipschutter te worden.")

        choice = input()  

        if choice == 'a':
            input("iemand rijd tijdens training perongeluk over je voet heen")
            input("je bent ongeschikt voor het leger")
            input("win!! je hoeft het leger nietmeer in.")
        if choice == 'b':
            input("bij je eerste training word je door een mede soldaat in je scheen geschoten omdat hij boos is dat hij steeds mist")
            input("win!! je ben ongeschikt voor het leger en hoeft ze niet meer te helpen")

    if choice == 'c':
        input("de marine goede keuze. Wat wil je doen bij de marine?")
        print("a:leren een duiker te worden.")
        print("b:leren wapens op het ship besturen.")

        choice = input()
        
        if choice == 'a':
            input("je leert duiker te worden en laat allemaal geheime informatie op de zee bodem voor de landen tegen duitsland")
            input("win!! je bent een hulp tegen de nazies geworden")
        
        if choice == 'b':
            input("je ship word opgeblazen als jullie de kust uit varen")
            input("fail!!")