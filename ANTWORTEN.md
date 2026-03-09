# Übungsblatt DL 3 – Docker mit Python steuern
## Antworten und Ergebnisse

---

## Aufgabe 1: Verbindung & Docker-Infos anzeigen ✅

### Notierte Ausgabe

* **Docker-Version:** 29.1.2
* **Betriebssystem:** linux
* **Architektur:** arm64

### Check-Fragen

**1. Was bedeutet `True` bei `client.ping()`?**

➡️ `True` bedeutet, dass Python erfolgreich mit dem Docker-Daemon kommunizieren kann. Die Verbindung funktioniert und Docker ist bereit, Befehle zu empfangen.

**2. Warum ist es sinnvoll, bei Fehlern eine Tipp-Meldung auszugeben?**

➡️ Eine Tipp-Meldung hilft dem Benutzer, das Problem schnell zu verstehen und zu lösen (z.B. "Docker starten"). Ohne Tipp würde nur eine technische Fehlermeldung erscheinen, die schwer zu interpretieren ist.

---

## Aufgabe 2: Einen Container starten und die Ausgabe verstehen

### Notierte Ausgabe

Schreibe hier die 3 Zeilen ab, die du bekommst:

1. Hallo aus dem Container!
2. root
3. Linux

### Check-Fragen

**1. Erkläre in einem Satz: Was ist ein Image?**

➡️ Ein Image ist eine unveränderbare Vorlage/Bauplan, die alle Dateien und Einstellungen enthält, um einen Container zu starten.

**2. Erkläre in einem Satz: Was ist ein Container?**

➡️ Ein Container ist eine laufende Instanz eines Images – eine isolierte Umgebung, in der Programme ausgeführt werden können.

**3. Was macht `remove=True`?**

➡️ `remove=True` sorgt dafür, dass der Container automatisch gelöscht wird, sobald er seine Aufgabe beendet hat. So bleibt das System sauber und es sammeln sich keine gestoppten Container an.

---

## Aufgabe 3: Hintergrund-Container starten, finden, IP anzeigen, aufräumen

### Notierte Ergebnisse

* **Container-Name:** brave_driscoll
* **Netzwerk-Name:** bridge
* **IP-Adresse:** 172.17.0.2

### Check-Fragen

**1. Warum ist `detach=True` praktisch?**

➡️ Mit `detach=True` läuft der Container im Hintergrund weiter, ohne dass Python/das Terminal blockiert wird. Man kann sofort mit dem nächsten Code weitermachen, während der Container parallel arbeitet.

**2. Was kann passieren, wenn du Container nie stoppst/löschst?**

➡️ Es sammeln sich immer mehr gestoppte Container an, die Speicherplatz und Ressourcen belegen. Das System wird langsamer und unübersichtlich. Außerdem können Ports blockiert bleiben.

---

## Bonus (freiwillig) ⭐

**Ändere bei Aufgabe 2 das Image von `ubuntu:latest` auf eine feste Version, z.B. `ubuntu:24.04`**

**Frage: Siehst du Unterschiede in der Ausgabe oder beim Download?**

➡️ Bei einer festen Version (z.B. `ubuntu:24.04`) wird genau diese Version heruntergeladen. Bei `latest` wird immer die neueste verfügbare Version verwendet. Der Vorteil fester Versionen: Das Verhalten bleibt reproduzierbar und ändert sich nicht, wenn Ubuntu eine neue Version veröffentlicht.

---

## Zusammenfassung

### Was habe ich gelernt?

- ✅ Python kann Docker über die `docker`-Bibliothek steuern
- ✅ Container sind isolierte, laufende Instanzen von Images
- ✅ Container können einmalig (`remove=True`) oder im Hintergrund (`detach=True`) laufen
- ✅ Jeder Container bekommt seine eigene IP-Adresse im Docker-Netzwerk
- ✅ Container müssen aufgeräumt werden, um Ressourcen freizugeben

### Wichtige Python-Befehle

```python
# Verbindung herstellen
client = docker.from_env()
client.ping()  # Prüfen ob Docker läuft

# Image laden
client.images.pull("ubuntu:latest")

# Container einmalig starten
client.containers.run("ubuntu:latest", "echo Hello", remove=True)

# Container im Hintergrund starten
container = client.containers.run("alpine:latest", "sleep 30", detach=True)

# Container verwalten
container.stop()    # Stoppen
container.remove()  # Löschen
container.reload()  # Aktualisieren
```
