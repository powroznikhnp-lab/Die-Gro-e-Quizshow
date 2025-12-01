#Schleifen beginn
while True:

#Teilnehmen Frage
    print ('Willkommen zu der großen Quiz Show.Willst du teilnehmen?')
    teilnehmen = input ('ja/nein\n').strip().lower()

#Wenn jemand nein auf teilnehmen Frage sagt
    if teilnehmen == 'nein':
         print ('Tja nicht mein Problem. DU MACHST MIT!')

#Wenn jemand nein auf teilnehmen Frage sagt
    elif teilnehmen == 'ja':
         print ('Good Boy. Lass uns anfangen.')

#Wenn jemand etwas anderes auf teilnehmen Frage sagt
    else: print ('RECHTSCREIBUNG! Aber egal ich werte das als ein ja, und du kannst nichts dagegen machen. HAHAHAHHAH')

#Variable wie oft jemand richtig lag
    richtig_count = 0

###################################################################################################################################

#1.Frage
    print ('Also erste Frage:\n1.Was Kann fr.Donney am besten?')
    frage_1 = input ('A: Englisch B: Deutsch C: Driften D: Mewen\n').strip().lower()
#wenn jemand die frage richtig hatte 
    if frage_1 == 'c':
         print ('RICHTIG Frau Donney kann am besten driften.')
         richtig_count += 1
#wenn jemnad die frage falsch hatte
    else: print ('FALSCH! Frau Donney kann am besten driften.')


#2.Frage
    print ('Welche Diagnose hat der Reck')
    frage_2 = input ('A: Passiv Agressiv B: Autismus C: Keine\n').strip().lower()
#wenn jemand die frage richtig hatte 
    if frage_2 == 'a':
         print ('RICHTIG Der Reck ist passiv agressiv')
         richtig_count += 1
#wenn jemnad die frage falsch hatte
    else: print ('Falsch Der Reck ist passiv agressiv')


#3.Frage
    print ('Als was kann man das JCS noch bezeichnen?')
    frage_3 = input ('A: HTG B: JVA C: JVA fü reiche\n').strip().lower()
#wenn jemand die frage richtig hatte 
    if frage_3 == 'a' or frage_3 == 'c':
         print ('RICHTIG unsere Schule ist sowohl eiene HTG als auch eine JVA für reiche.')
         richtig_count += 1
#wenn jemnad die frage falsch hatte
    else: print ('Falsch unsere Schule ist sowohl eiene HTG als auch eine JVA für reiche.')


#4.Frage
    print ('Wer hat genau das selbe Level an intiliegenz wie Donals Trump?')
    frage_4 = input ('A: P Diddy B: Einstein C: Epstein D: Alice Weidel\n').strip().lower()
#wenn jemand die frage richtig hatte 
    if frage_4 == 'a' or frage_4 == 'c' or frage_4 == 'd':
         print ('RICHTIG Diese Persönlichkeiten zählen zu den dümmsten auf der Welt.')
         richtig_count += 1
#wenn jemnad die frage falsch hatte
    else: print ('Falsch Dafür wird dir ein Punkt abgezogen!!!'); richtig_count -= 1
        


#5.Frage
    print ('Was kann fr.Goedike am besten?')
    frage_5 = input ('A: Chemie B: Ihre Frisur machen C: Mit einem Buttermesser Natrium zerschneiden\n').strip().lower()
#wenn jemand die frage richtig hatte 
    if frage_5 == 'c':
         print ('RICHTIG Frau Goedike kann am besten mit einem Buttermesser Natrium zerschneiden.')
         richtig_count += 1
#wenn jemnad die frage falsch hatte
    else: print ('Falsch Frau Goedike kann am besten mit einem Buttermesser Natrium zerschneiden.')    

###################################################################################################################################

    print (' Du hattest',richtig_count,'/5 Fragen richtig')
   
#0 Mal richtig
    if richtig_count == 0:
        print('Du Bist ja mal so dumm. Du musst wiederholen.\n')

#1 Mal richtig
    elif richtig_count == 1:
        print('Gerade mal eine Frage richtig! Du wiederholst\n')

#2 Mal richtig
    elif richtig_count == 2:
        print('Nur 2 richtige Antworten? Deine Eltern müssen echt entaüscht von dir sein. Mach das nochmal!\n')      

#3 Mal richtig
    elif richtig_count == 3:
        print('Du hast gerade einmal 3 richtige Antworten geschafft.')
        break

#4 Mal richtig
    elif richtig_count == 4:
        print('4 ist ganz OK.')
        break

#5 Mal richtig
    else:
        print('Du bist "nicht schlecht".')
        break

