import json
import os

JSON_FILE = "questions.json"
#Load Questions Funktion
def load_questions(filename):
    #try/Catch für Fehlersuche
    try:
        # Pfad der aktuellen Datei suchen und filename anfügen
        #__file__ ist der path zur python datei, automatisch von Python
        #nimmt nur den ordner, wo die Datei liegt
        base_path = os.path.dirname(os.path.abspath(__file__))
        #fügt den Json-Dateinamen an
        file_path = os.path.join(base_path, filename)
        #File öffnen und in data laden
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    #Exception if JsonDecode Error
    except json.JSONDecodeError as e:
        print(f"Error while reading JSON: {e}")
        #Leere Liste zurückgeben
        return []
    #Liste definieren
    questionsFile = []
    #für jeden EIntrag in der Json datei die Data heisst
    for entry in data:
        #mit append(entry) wird der im moment gewählte Eintrag in die Liste questionsFile hinzugefügt
        questionsFile.append(entry)
    #die Liste aus der FUntkion ausgeben
    return questionsFile

#Funktion zur Berechnung der Note, numberCorrect = Anzahl richtig beantwortete Fragen, numberAll = anzahl Fragen
def calculateGrade(numberCorrect, numberAll):
    #Prozentualer Anteil der richtig beantworteten Fragen
    percent = numberCorrect / numberAll
    #grade calculation
    grade = 1.0 + percent * 5.0
    #round to .5
    return round(grade, 1)

def main():
    #Print
    print("=== Quiz-App ===")
    #Input für den namen, wird in der variable name gespeichert, Strip() entfernt Leerzeichen am Anfang und Ende
    name = input("Please enter your name: ").strip()
    #Falls kein Name eingegeben wurde, wird "Unknown" als Name gesetzt
    if not name:
        name = "Unknown"
    #Lade Fragen aus der JSON Datei über die Funktion load_questions. wird in variable questions gespeichert
    questions = load_questions(JSON_FILE)
    #Falls die Liste questions leer ist, wird eine Fehlermeldung ausgegeben und die Funktion beendet
    if not questions:
        print("File contains no questions")
        return
    #Begrüßung des Nutzers mit der Anzahl der Fragen, len wird für anzahlelemente in der Liste genutzt
    print(f"Hello {name}! there are {len(questions)} questions.\n")
    #Warte auf Enter Taste
    input("press enter to start! ...")
    #numberCorrect wird auf 0 gesetzt
    numberCorrect = 0
    #Counter for questions
    counterQuestions = 0
    #Loop für jede Frage in der Liste questions
    for question in questions:
        #Fragezähler erhöhen
        counterQuestions += 1
        #Trennlinie drucken
        print("----------------------------------------------------------------")
        #Fragenummer und Frage drucken
        print(f"Question {counterQuestions}: {question['question']}")
        #Counter for questions
        counterOptions = 0
        #Loop für jede Option in der aktuellen Frage
        for option in question["options"]:
            #Optionenzähler erhöhen
            counterOptions += 1
            #Option drucken
            print(f"  {counterOptions}) {option}")
        #loop bis eine gültige Antwort eingegeben wurde, und break dann raus
        while True:
            #User input für die Antwort, strip um leerzeichen zu entfernen
            response = input("Your response (enter number): ").strip()
            #prüfen ob die Eingabe eine Zahl ist
            if not response.isdigit():
                #Falls nicht, Fehlermeldung und zur nächsten Iteration mit continue
                print("Please enter a number")
                continue
            #Python fängt mit 0 an zu zählen, deshalb -1
            chosen = int(response) - 1
            #die Antwort muss zwischen 0 und der Anzahl der Optionen liegen
            if not 0 <= chosen < len(question["options"]):
                #Falls nicht, Fehlermeldung
                print("Please enter a valid option number")
            else:
                break
        #Prüfen ob die gewählte Antwort korrekt ist, sucht nach dem Wert des Element "correct_index" in der aktuellen Frage in der JSON Datei
        if chosen == question["correct_index"]:
            #Ausgabe für korrekte Antwort
            print("✅ Correct!")
            #Counter für richtig beantwortete Fragen erhöhen
            numberCorrect += 1
        else:
            #Richtige Antwort herausfinden, gibt den Text im Element options aus, die den Index des Elements correct_index hat
            correctResponse = question["options"][question["correct_index"]]
            #Ausgabe für falsche Antwort
            print(f"❌ Incorrect! Correct answer: {correctResponse}")
    #Note berechnen über die Funktion calculateGrade
    grade = calculateGrade(numberCorrect, len(questions))
    #Ausgaben der Ergebnisse
    print("========================================================")
    print(f"Here are your results {name}")
    print(f"questions correct: {numberCorrect} of {len(questions)}")
    print(f"grade (1–6): {grade}")
    print("========================================================")

#Programmstart
main()