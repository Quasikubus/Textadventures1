print("Du lebst als Sklav im Jahr 2000 vor Christus.")
print("Dein Ziel ist es, die wertvollen Schätze des Pharaos zu klauen. Diese befinden sich in dessen Grab, im Zentrum der Pyramide von Gyzeh.")
print("Dir ist bewusst, dass der Weg dorthin gefährlich ist. Du könntest dich verlaufen oder beim Auslösen von Fallen sterben.")
print()
print("Du stehst vor der Pyramide und hast zwei Möglichkeiten hineinzugelangen:")
print()
print("A: Du probierst unauffällig durch den Haupteingang zu laufen. Dafür müsstest du dich verkleiden.")
print()
print("B: Du gehst durch den Geheimgang, wofür du die Schlüssel benötigst.")
print()
done = False
while not done:
    
    antwort = input("Welchen Weg wählst du, A oder B ")
    antwort = antwort.strip().lower()

    if antwort == "a":
        print("Um unauffällig durchzukommen, brauchst du die Kleidung der Wächter.")
        print("Diese bekomst du, indem du einer der beiden Wächter wegführst.")
        print("So läufst du auf den Haupteingang zu und sprichst den ersten Wächter an.")
        print("Du machst ihn auf ein Problem beim Bau der Pyramide aufmerksam.")
        print("Du erklärst ihm, dass sich der Baufehler auf der anderen Seite der Pyramide befindet und überzeugst ihn mitzukommen.")
        print("Als ihr ankommt zeigst du ihm die Stelle und er bückt sich, um sie von Nahem zu betrachten.")
        print("Jetzt ergreifst du die Chance und schlägst ihm mit einem Backstein, den du am Boden gefunden hast, auf den Kopf.")
        print("Der Wächter liegt jetzt in Ohnmacht auf dem Boden. Du siehst den Schlüssel an seiner Hüft im Sonnenlicht schimmern.")
        print()
        print("A: Du nimmst den Schüssel.")
        print()
        print("B: Du ziehst seine Kleider an.")
        print()
        done = False
        while not done:
            
            antwort2 = input("Was machst du? ")
            antwort2 = antwort2.strip().lower()
            if antwort2 == "a":
                print("Mutig")
                print("Bevor du wieder in Richtung Haupteingang losläufst, nimmst du zur Sicherheit das Speer des Wächters mit.")
                print("Wie gehst du weiter vor?")
                print()
                print("A: Du gehst furchtlos auf den zweiten Wächter zu und wirfst ihm das Speer an.")
                print()
                print("B: Du sagst dem zweiten Wächter, er solle helfen kommen, da jemand sie angegriffen hat.")
                print()
                done = False
                while not done:
                    
                    antwort3 = input("Was tust du? ")
                    antwort3 = antwort3.strip().lower()
                    if antwort3 == "a":
                        print("Zu mutig.")
                        print("Du verfehlst, er trifft.")
                        print("GAME OVER.")
                        exit()
                    if antwort3 == "b":
                        print("Er glaubt dir und rennt, nachdem du ihm gesagt hast, dass du Verstärkung holst, schonmal los.")
                        print("Jetzt steht der Weg frei und du verschwindest schnell hinter dem Tor.")
                        print()
                        print()
                        print("Du stehst in einem kleinen Raum und vor dir ist eine Tür, die dich wahrscheinlich direkt zum Gold führen würde.") 
                        print("Du kannst sie aber mit deinem Schlüssel nicht öffnen. Dazu sind die Wachen nicht ausgestattet.")
                        print("Zwei Wege, links und rechts von der Tür, sind zu sehen.")
                        print("Beide Wege sehen gleich aus.")
                        print()
                        done = True
                        while done:
                            antwort4 = input("Links oder Rechts? ")
                            antwort4 = antwort4.strip().lower()
                            if antwort4 == "links":
                                print("Gute Wahl.")
                                print("Du biegst links ab und stehst in einem dunklen Gang. Du hast Glück, denn du kannst noch gerade Löcher in den beiden Wänden erkennen.")
                                print("Wahrscheinlich lauert dort eine Falle.")
                                print("Willst du vorsichtig sein oder eher mutig?")
                                print()
                                print("A: Du wirfst ein Speer bis zum anderen Ende des Ganges, um die Falle auszulösen.")
                                print()
                                print("B: Du sprintest rüber, um der Falle auszuweichen.")
                                print()
                                done = False
                                while not done:
                                    antwort5 = input("A oder B? ")
                                    antwort5 = antwort5.lower().strip()
                                    if antwort5 == "a":
                                        print("In der Luft wird das Speer von vielen kleinen Klingen zerfetzt.")
                                        print("Vorsichtig läufst du durch den Gang.")
                                        print("Etwa in der Mitte des Ganges hörst ein: Click!.")
                                        print("Bevor du irgendwie reagieren könntest wirst du von der zweiten Salve Klingen zerfleischt.")
                                        print("GAME OVER")
                                        exit()
                                        done = True
                                    if antwort5 == "b":
                                        print("Während du rennst hörst du Klingen an dir vorbeiflitzen.")
                                        print("Du erreichst das andere Ende, lebend. Vor dir siehst du eine Tür, die du ohne Probleme öffnen kannst.")
                                        done = True
                                        print("Jetzt stehst du hinter dieser Tür und schaust hinunter.")
                                        print("Dort siehst du einen Abgrund mit hunderten von zischenden Cobras. Der Lärm ist fast nicht auszuhalten.")
                                        print("Es ist ein sehr grosser, hohler Raum. Um das andere Ende zu erreichen, ist die Begegnung mit den Cobras zu vermeiden.")
                                        print("Es ist ein Jump'n'Run. Du musst also von Säule zu Säule springen. Es gibt keinen anderen Weg.")
                                        print("Dir stehen zwei Möglichkeiten zur Verfügung:")
                                        print()
                                        print("Entweder jede Säule nach der anderen mit Pausen dazwischen oder alles in einem Lauf.")
                                        print()
                                        
                                        
                                        done = False
                                        while not done:
                                            antwort6 = input("schnell oder langsam? ")
                                            antwort6 = antwort6.lower().strip()
                                            if antwort6 == "schnell":
                                                print("Die dritte Säule verschiebt sich nach unten, als du dort landest.")
                                                print("Da du nur auf einem Bein landest, knickst du ein.")
                                                print("Du fliegst kopfsvoran in die nächste Säule, bevor du in den Abgrund fällst und das Zischen immer lauter wird.")
                                                print("Leider überlebst du den Sturz...")
                                                print("Eine letzte Heldentat oder stellst du dich tot?")
                                                print()
                                                print("A für die Heldentat.")
                                                print()
                                                print("B für das Totstellen.")
                                                print()
                                                done = False
                                                while not done:
                                                    antwort7 = input("A oder B? ")
                                                    antwort7 = antwort7.lower().strip()
                                                    if antwort7 == "a":
                                                        print("Mit deinem Speer kannst du noch ein paar Cobras mit in den Tod reissen.")
                                                        print("GAME OVER")
                                                        exit()
                                                    if antwort7 == "b":
                                                        print("So funktioniert das nicht. Du wirst lebendig verspeist.")
                                                        print("GAME OVER")
                                                        exit()
                                                    else:
                                                        print("ERROR")
                                                        print("Bitte nur A oder B.")
                                            if antwort6 == "langsam":
                                                print("Kontrolliert springst du von Säule zu Säule und gelangst rüber.")
                                                print("Du öffnest die Türe zum nächsten Raum und trittst über die Schwelle.")
                                                print("Dort begegnest du einer Sphinx, die gemütlich in der Mitte des Raumes liegt.")
                                                print("Sie spricht ohne dich anzuschauen und sagt: ")
                                                print("'Guten Tag Sklave, ich bitte dich meine Fragen zu beantworten.'")
                                                print("'Bei richtigen Antworten kommst du weiter, sonst endet es schlecht für dich.'")
                                                print("'Mal sehen wieviel du über die Ägyptische Kunst weisst.'")
                                                print("'Die erste Frage lautet:'")
                                                print()
                                                print("'Welches Merkmal hat die ägyptische Statue des Pharaos namens Chephren?'")
                                                print()
                                                print("A: In seiner rechten Hand hält er ein Zepter.")
                                                print()
                                                print("B: Auf seinem Hinterkopf befindet sich ein kleiner Falke.")
                                                print()
                                                print("C: Er ist nackt.")
                                                print()
                                               
                                                done = False
                                                while not done:
                                                    antwort8 = input("'Na, was denkst du? A, B oder C?' ")
                                                    antwort8 = antwort8.lower().strip()
                                                    if antwort8 == "a":
                                                        
                                                        print("'Deine Antwort ist falsch.'")
                                                        print("'Als ägyptischer Sklave solltest du den verstorbenen Chephren doch kennen oder nicht?'")
                                                        print("'Leider muss ich Unwissende eliminieren...'")
                                                        print()
                                                        print("GAME OVER.")
                                                        exit()
                                                    if antwort8 == "c":
                                                        print("'Deine Antwort ist falsch.'")
                                                        print("'Als ägyptischer Sklave solltest du den verstorbenen Chephren doch kennen oder nicht?'")
                                                        print("'Leider muss ich Unwissende eliminieren...'")
                                                        print()
                                                        print("GAME OVER.")
                                                        exit()
                                                    if antwort8 == "b":
                                                        print("'Richtige Antwort!'")
                                                        print("'Du musst noch eine Frage richtig beantworten um weiterzukommen.'")
                                                        print("'Die zweite Frage lautet:'")
                                                        print()
                                                        print("'Wie ist der Körper des Menschen in ägyptischen Malereien abgebildet?'")
                                                        print()
                                                        print("A: Das Auge frontal, der Rest des Körpers seitlich.")
                                                        print()
                                                        print("B: Der ganze Körper wurde seitlich abgebildet.")
                                                        print()
                                                        print("C: Das Auge und der Oberkörper frontal, der Unterkörper seitlich.")
                                                        print()
                                                        
                                                        done = False
                                                        while not done:
                                                            antwort9 = input("'Die letzte Frage. Welche der drei Optionen?' ")
                                                            antwort9 = antwort9.lower().strip()
                                                            if antwort9 == "c":
                                                                print("'Alles andere zu wählen wäre beschämend für einer, der imselben Land lebt.'")
                                                                print("Die Sphinx steht auf und fliegt zur Seite, um dir den Weg freizumachen.")
                                                                print("Die Türe zum geheimen Tresor öffnet sich und schon fallen Goldmünzen raus...")
                                                                print()
                                                                print("GAME COMPLETED.")
                                                                exit()
                                                            if antwort9 == "b":
                                                                print("'Fast.'")
                                                                print()
                                                                print("GAME OVER.")
                                                                exit()
                                                            if antwort9 == "a":
                                                                print("'Naja, nicht ganz.'")
                                                                print()
                                                                print("GAME OVER.")
                                                                exit()
                                                            else:
                                                                print("ERROR.")
                                                                print("Bitte nur einer der möglichen Antworten eingeben bitte.")
                                                                continue
                                                                
                                                            
                                                                
                                                            
                                                    else:
                                                        print("ERROR.")
                                                        print("Bitter nur A, B oder C eingeben.")
                                                        continue
                                            else:
                                                print("Nur schnell oder langsam eintippen.")
                                                continue
                                                

                                                
                                                
                                    else:
                                        print("ERROR.")
                                        print("Bitte nur A oder B eintippen.")
                                        continue
                                        done = True
                          
                            
                        
                            if antwort4 == "rechts":
                                print("Schlechte Wahl.")
                                done = False
                                print("Den nächsten Schritt, den du machst, fühlt sich irgendwie komisch an, als ob der Boden anders wäre.")
                                print("Du schaust nach unten auf deinen Fuss und löst deinen Fuss vom Boden. Click!")
                                print("Das war einen Druckplatte.")
                                print("Im nächsten Moment regnen Klingen von der Decke und dein Gehirn wird durchlöchert. Das solltest du nicht überleben können...")
                                print("GAME OVER")
                                exit()
                            else:
                                print("ERROR.")
                                print("Nur Richtungsangaben bitte.")
                    else:
                        print("Nur A oder B, merci.")
                        continue
            if antwort2 == "b":
                print("Wie geplant.")
                print("Weil du für das Aus- und Anziehen der Wächter-Bekleidung zu lange brauchst, kommt der zweite Wächter nachschauen.")
                print("Du erkennst es zu spät und wirst ebenfalls K.O. geschlagen.")
                print("GAME OVER.")
                exit()
            else:
                print("Nur A oder B bitte.")
                continue
    if antwort == "b":
        print("Die Schlüssel kriegst du von der Frau des Pharaos.")
        print("Du begibst dich also vor ihr Haus und musst einen Plan schmieden.")
        print()
        print("A: Du suchst eine Mordwaffe und bringst sie um.")
        print()
        print("B: Du suchst ihren Ersatzschlüssel in ihrem Schlafzimmer.")
        print()
        done = False
        while not done:
            antwort5 = input("A oder B? ")
            antwort5 = antwort5.strip().lower()
            if antwort5 == "a":
                print("Wo denkst du findet man etwas tödliches?")
                print()
                print("A: In der Küche.")
                print()
                print("B: Im Wohnzimmer.")
                print()
                done = False
                while not done:
                    antwort6 = input("Welche der beiden Optionen? ")
                    antwort6 = antwort6.strip().lower()
                    if antwort6 == "a":
                        print("Du siehst die Frau des Pharaos neben dem Wohnzimmer auf dem Balkon mit einer ihrer Freundinnen ein Bier trinken. Du hast glück, denn sie kehrt dir den Rücken zu.")
                        print("Du schleichst also am Wohnzimmer vorbei in die Küche. Dort schnappst du dir ein Küchenmesser.")
                        print("Du musst beide ermorden, um an den Schlüssel zu gelangen. Danach solltest du sehr schnell abhauen.")
                        print("Du wartest ab, bis die Freundin auf die Toilette geht. Als sie fertig ist, stichst du ihr in den Rücken. Die Leiche versteckst du im Badezimmer.")
                        print("Nach einer Weile kommt die Frau des Pharaos nach, um nachzuschauen, wo sich ihre Freundin aufhält.")
                        print("Sie tritt ins Badezimmer. Du hast dich währenddessen in ihrem Schlafzimmer versteckt.")
                        print("Als du das Schliessen der Tür hörst und den Schreckensschrei der Frau, kommst du aus deinem Versteck hervor und tötest sie ebenfalls.")
                        print("Mit dem Schlüssel begibst du dich zum Geheimgang.")
                        print()
                        print("Du begibst dich ins Innere der Pyramide. Du stehst in einem gewöhnlichen Gang.")
                        print()
                        print("An dessen Ende erblickst du eine Treppe, die einem nach unten bringt.")
                        print()
                        print("Langsam gehst du die Treppe hinunter. Du kannst ganz unten Licht sehen.")
                        print("Du bist neugierig, was unten auf dich wartet, also läufst du die Treppe hinunter.")
                        print("Als du unten angekommen bist, öffnet sich an deiner rechten Seite ein kleiner Raum.")
                        print("Dieser ist von Fakeln belichtet, welche an den vier Wänden befestigt sind.")
                        print("psssssttttt. du musst leise sein. da schläft ein Löwe...")
                        print("Er ist angekettet und hinter ihm ist eine riesige Tür, die dich weiterführen wird.")
                        print("Neben ihm kannst du eine angefressene Gazelle finden.")
                        print()
                        print("Wie willst du vorgehen?")
                        print()
                        print("A: Du nimmst dir eine Fackel zur Hilfe.")
                        print()
                        print("B: Du brichst die Hörner der Gazelle ab und tötest den Löwen.") 
                        print()
                        done = False
                        while not done:
                            antwort9 = input("A oder B? ")
                            antwort9 = antwort9.lower().strip()
                            if antwort9 == "a":
                                print("Du trittst also näher an die nächstgeliegene Fakel heran.")
                                print("Du greifst nach ihr und bemerkst, dass der geschmolzene Wachs schon die ganze Halterung verklebt hat.")
                                print("Mit grosser Wucht ziehst du mit beiden Händen daran, da löst sich die Fackel samt der Halterung von der Wand.")
                                print("Du fliegts rückwärts auf den Boden, verbrennst dir das Gesicht, als du auch noch ein Gebrüll neben dir hörst.")
                                print("Blind tastest du nach dem Ausgang, als du ins Bein gebissen wirst. Der Löwe verspeist gerade sein Dessert.")
                                print()
                                print("GAME OVER")
                                exit()
                        
                            if antwort9 == "b":
                                print("Gestorbene Tiere missbrauchen, so einer bist du also.")
                                print("Du läufst langsam in die Richtung der Gazelle. Der Gestank des toten Tieres dringt in deine Nase ein.")
                                print("Du brichst die Hörner also ab. Du stehst jetzt da vor dem Löwen mit je einem abgebrochenem Horn in beiden Händen.")
                                print("Du musst dich wiederum entscheiden:")
                                print()
                                print("A: Je ein Horn in ein Auge.")
                                print()
                                print("B: Ein Horn könntest du später noch gebrauchen. Das andere sollte reiche, einen schlafenden Löwen erledigen.")
                                print()
                                done = False
                                while not done:
                                    antwort10 = input("A oder B? ")
                                    antwort10 = antwort10.strip().lower()
                                    if antwort10 == "a":
                                        print("Du willst es blutig sehen.")
                                        print("Blind, versucht der Löwe dich mit seinen Pfoten zu treffen, was ihm aber nicht gelingt.")
                                        print("Du kannst an ihm vorbeirennen und die Tür hinter dir schliessen.")
                                        print("Als du hinunter schaust, kannst du einen Abgrund erkennnen.")
                                        print("Dort siehst du einen Abgrund mit hunderten von zischenden Cobras. Der Lärm ist fast nicht auszuhalten.")
                                        print("Es ist ein sehr grosser, hohler Raum. Um das andere Ende zu erreichen, ist die Begegnung mit den Cobras zu vermeiden.")
                                        print("Es ist ein Jump'n'Run. Du musst also von Säule zu Säule springen. Es gibt keinen anderen Weg.")
                                        print("Dir stehen zwei Möglichkeiten zur Verfügung:")
                                        print()
                                        print("Entweder jede Säule nach der anderen mit Pausen dazwischen.")
                                        print()
                                        print("Oder alles in einem Lauf.")
                                        print()
                                        
                                        done = False
                                        while not done:
                                            antwort6 = input("schnell oder langsam? ")
                                            antwort6 = antwort6.lower().strip()
                                            if antwort6 == "schnell":
                                                print("Die dritte Säule verschiebt sich nach unten, als du dort landest.")
                                                print("Da du nur auf einem Bein landest, knickst du ein.")
                                                print("Du fliegst kopfsvoran in die nächste Säule, bevor du in den Abgrund fällst und das Zischen immer lauter wird.")
                                                print("Leider überlebst du den Sturz...")
                                                print("Eine letzte Heldentat oder stellst du dich tot?")
                                                print()
                                                print("A für die Heldentat.")
                                                print()
                                                print("B für das Totstellen.")
                                                print()
                                                done = False
                                                while not done:
                                                    antwort7 = input("A oder B? ")
                                                    antwort7 = antwort7.lower().strip()
                                                    if antwort7 == "a":
                                                        print("Mit deinem Speer kannst du noch ein paar Cobras mit in den Tod reissen.")
                                                        print("GAME OVER")
                                                        exit()
                                                    if antwort7 == "b":
                                                        print("So funktioniert das nicht. Du wirst lebendig verspeist.")
                                                        print("GAME OVER")
                                                        exit()
                                                    else:
                                                        print("ERROR")
                                                        print("Bitte nur A oder B.")
                                            if antwort6 == "langsam":
                                                print("Kontrolliert springst du von Säule zu Säule und gelangst rüber.")
                                                print("Du öffnest die Türe zum nächsten Raum und trittst über die Schwelle.")
                                                print("Dort begegnest du einer Sphinx, die gemütlich in der Mitte des Raumes liegt.")
                                                print("Sie spricht ohne dich anzuschauen und sagt: ")
                                                print("'Guten Tag Sklave, ich bitte dich meine Fragen zu beantworten.'")
                                                print("'Bei richtigen Antworten kommst du weiter, sonst endet es schlecht für dich.'")
                                                print("'Mal sehen wieviel du über die Ägyptische Kunst weisst.'")
                                                print("'Die erste Frage lautet:'")
                                                print()
                                                print("'Welches Merkmal hat die ägyptische Statue des Pharaos namens Chephren?'")
                                                print()
                                                print("A: In seiner rechten Hand hält er ein Zepter.")
                                                print()
                                                print("B: Auf seinem Hinterkopf befindet sich ein kleiner Falke.")
                                                print()
                                                print("C: Er ist nackt.")
                                                print()
                                                
                                               
                                                done = False
                                                while not done:
                                                    antwort8 = input("'Na, was denkst du? A, B oder C?' ")
                                                    antwort8 = antwort8.lower().strip()
                                                    if antwort8 == "a":
                                                        
                                                        print("'Deine Antwort ist falsch.'")
                                                        print("'Als ägyptischer Sklave solltest du den verstorbenen Chephren doch kennen oder nicht?'")
                                                        print("'Leider muss ich Unwissende eliminieren...'")
                                                        print()
                                                        print("GAME OVER.")
                                                        exit()
                                                    if antwort8 == "c":
                                                        print("'Deine Antwort ist falsch.'")
                                                        print("'Als ägyptischer Sklave solltest du den verstorbenen Chephren doch kennen oder nicht?'")
                                                        print("'Leider muss ich Unwissende eliminieren...'")
                                                        print()
                                                        print("GAME OVER.")
                                                        exit()
                                                    if antwort8 == "b":
                                                        print("'Richtige Antwort!'")
                                                        print("'Du musst noch eine Frage richtig beantworten um weiterzukommen.'")
                                                        print("'Die zweite Frage lautet:'")
                                                        print()
                                                        print("'Wie ist der Körper des Menschen in ägyptischen Malereien abgebildet?'")
                                                        print()
                                                        print("A: Das Auge frontal, der Rest des Körpers seitlich.")
                                                        print()
                                                        print("B: Der ganze Körper wurde seitlich abgebildet.")
                                                        print()
                                                        print("C: Das Auge und der Oberkörper frontal, der Unterkörper seitlich.")
                                                        print()
                                                        
                                                        done = False
                                                        while not done:
                                                            antwort9 = input("'Die letzte Frage. Welche der drei Optionen?' ")
                                                            antwort9 = antwort9.lower().strip()
                                                            if antwort9 == "c":
                                                                print("'Alles andere zu wählen wäre beschämend für einer, der imselben Land lebt.'")
                                                                print("Die Sphinx steht auf und fliegt zur Seite, um dir den Weg freizumachen.")
                                                                print("Die Türe zum geheimen Tresor öffnet sich und schon fallen Goldmünzen raus...")
                                                                print()
                                                                print("GAME COMPLETED.")
                                                                exit()
                                                            if antwort9 == "b":
                                                                print("'Fast.'")
                                                                print()
                                                                print("GAME OVER.")
                                                                exit()
                                                            if antwort9 == "a":
                                                                print("'Naja, nicht ganz.'")
                                                                print()
                                                                print("GAME OVER.")
                                                                exit()
                                                            else:
                                                                print("ERROR.")
                                                                print("Bitte nur einer der möglichen Antworten eingeben bitte.")
                                                                continue
                                        
                                                                
                                                            
                                                                
                                                            
                                                    else:
                                                        print("ERROR.")
                                                        print("Bitter nur A, B oder C eingeben.")
                                                        continue
                            
                                            else:
                                                print("Bitte nur schnell oder langsam eingeben.")
                                                continue
                                        
                                        done = True
                                    if antwort10 == "b":
                                        print("Kannst du den Löwen noch erledigen?")
                                        print("Mit einem Auge sieht der Löwe trotzdem noch was.")
                                        print("Du denkst nach und kommst zum Schluss, dass du doch das Horn wieder rausstecken kannst und diese für das andere Auge benutzen.")
                                        print("Du steckst das Horn ins erste Auge, als der Löwe abrupt aus dem Schlaf geweckt wird und dir direkt eine Pfote ins Gesicht haut.")
                                        print()
                                        print("GAME OVER.")
                                        exit()
                                              
                                    else:
                                        print("ERROR:")
                                        print("Tippe nur: A oder B ein.")
                                        continue
                                   
                                    
                            
                    if antwort6 == "b":
                        print("Im Wohnzimmer sieht nur etwas gefährlich aus: einen Blumetopf.")
                        print("Du erkennst zwei Frauen auf dem Balkon neben dem Wohnzimmer, wahrscheinlich die Frau des Pharaos mit einer ihrer Freundinnen")
                        print("Leider reicht ein Topf nur für eine Person...")
                        print("Also wartest du ab bis die Pharao in die Küche geht, um neues Bier zu holen.")
                        print("Als sie an dir vorbeiläuft, schmeisst du den Topf auf ihren Kopf. Sie ist ohnmächtig.")
                        print("Aufgrund des Riesenlärms, den du verursacht hast, wird die Freundin der Pharao aufmerksam.")
                        print("Sie nimmt ein Speer in ihre Hand, das sie auf dem Balkon gefunden hat und wirft ihn dir direkt in die Stirn.")
                        print("GAME OVER")
                        exit()
                    else:
                        print("Bitte nur A oder B wählen.")
                        continue

                
            elif antwort5 == "b":
                print("Dann ab ins Schlafzimmer.")
                print("Da hast du aber Pech gehabt, denn als du probierst die Schlafzimmertür aufzumachen, merkst du dass diese verschlossen ist.")
                print("Wähle besser die andere Variante.")
                print()
                continue
    else:
       print("ERROR.")
       continue
    





