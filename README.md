[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22186912&assignment_repo_type=AssignmentRepo)
# Rem. Ex. Kerst - django praktijk
Er mag geen gebruik gemaakt worden van voorgaande oefeningen of AI.</br>
Internet met wel gebruikt worden alsook de documenten uit de oneNote. cheatSheets

## datamodel

1. speler [naam, voornaam, email]
2. match_punten [nummerSpeler, punten, matchCode]

Je hebt verschillende spelers die matchen spelen (pingpong bv): </br>
Winnen ze de match krijgen ze 4p, gelijkspel 2p, verlies = 0 maar wordt ook geregistreerd.

## zorg ervoor dat onderstaande endpoint het gewenste resultaat geven 

| endpoint      | resultaat      |
| ------------- | ------------- |
| speler/add | een speler toevoegen |
| speler/<<int:id>> | de gegevens van een speler op basis van zijn id |
| speler/ | een array van alle spelers |
| matchPunten/resultaat/<<int:idSpeler>>/<<int:matchCode>> | het resultaat opvragen van een speler op een match  |
| punten/<<int:idSpeler>> | 1 resultaat= totaal van die speler |
