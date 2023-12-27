# Star Wars Social Network Daten

Die Daten stammen aus einer [Kaggle Challenge](https://www.kaggle.com/datasets/ruchi798/star-wars) und sind stehen online zur Verfügung.

[Zweitdatensatz](https://www.kaggle.com/datasets/jsphyg/star-wars/data?select=characters.csv) den wir verwendet haben. haben wir ebenfalls auf Kaggle gefunden. 

# Beschreibung der Daten

Anzahl Knoten: 110   
Anzahl Kanten: 443

Diese Angaben gelten über alle Filme. Wir haben auch die Daten für jede einzelne Episode, welche wir zuerst verwenden werden. Diese werden kleiner sein, in der ersten Episode hat es 37 Knoten und 134 Kanten.

## Knotenattribute:

- Name des Charakters

- Anzahl der Szenen, in denen der Charakter auftritt

- Farbe in der Visualisierung (wir können dieses Attribut nicht nachvollziehen und wer-den es vorerst ignorieren)

## Kantenattribute:

- Index des Start- und Zielcharakters

- Anzahl der Szenen, in denen beide Charaktere gemeinsam auftreten

- Datenqualität und -probleme: Wir erwarten noch keine Unregelmässigkeiten oder Probleme bei den Daten. Denn es handelt sich um einen viel genutzten Datensatz von Kaggle, für den auch schon Notebooks/Anwendungen veröffentlicht wurden. Wir erwarten, in der explorati-ven Datenanalyse mögliche Fehler abfangen zu können
