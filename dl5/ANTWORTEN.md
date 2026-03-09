# Übungsblatt – DL5: Registries & Image-Workflow

---

## Teil A – Grundverständnis

### Was ist eine Registry?

Eine Docker-Registry ist ein Server, der Docker-Images speichert und verteilt. Sie funktioniert wie ein zentrales Lager, aus dem Entwickler Images herunterladen (pull) oder eigene Images hochladen (push) können. Die bekannteste öffentliche Registry ist Docker Hub, aber man kann auch private Registries betreiben (z.B. für Firmen-interne Images).

### Erkläre die Begriffe

- **Image:** Eine unveränderbare Vorlage mit allen Dateien, Bibliotheken und Einstellungen, die nötig sind, um eine Anwendung in einem Container auszuführen.
- **Container:** Eine laufende Instanz eines Images – eine isolierte Umgebung, in der Programme ausgeführt werden.
- **Repository:** Ein Bereich innerhalb einer Registry, der verschiedene Versionen (Tags) eines bestimmten Images zusammenfasst (z.B. `python` auf Docker Hub).
- **Tag:** Eine Versionsbezeichnung für ein Image innerhalb eines Repositories (z.B. `3.12-slim`, `latest`, `1.0`).
- **Pull:** Das Herunterladen eines Images von einer Registry auf den lokalen Rechner.
- **Push:** Das Hochladen eines lokalen Images in eine Registry, damit andere es verwenden können.

### Warum ist latest problematisch?

- `latest` ist nur ein Standard-Tag-Name. Er zeigt nicht auf eine feste Version, sondern auf das zuletzt hochgeladene Image.
- Das ist problematisch, weil sich der Inhalt von `latest` jederzeit ändern kann. Heute könnte `python:latest` auf Python 3.12 zeigen und morgen auf 3.13. Damit ist das Verhalten nicht reproduzierbar.
- Besser ist es, eine feste Versionsnummer zu verwenden, z.B. `python:3.12-slim`. So weiss man genau, welche Version läuft, und das Verhalten bleibt konsistent.

---

## Teil B – Arbeiten mit dem Skript

### Image suchen

- Ich habe nach **python** gesucht.
- Das Image **python** war als „Official" markiert.
- Man erkennt Official Images daran, dass sie in der Suche mit einem ⭐ Official-Label angezeigt werden. Auf Docker Hub haben Official Images ein blaues „Docker Official Image"-Badge und keinen Benutzernamen im Image-Namen (z.B. `python` statt `username/python`).

### Pull

- Ich habe das Image **python:3.12-slim** gepullt.
- „Pull" bedeutet, dass ein Image von einer entfernten Registry (z.B. Docker Hub) auf den lokalen Rechner heruntergeladen wird. Docker prüft dabei, welche Layer bereits lokal vorhanden sind, und lädt nur die fehlenden Layer herunter.

### Tagging

- Man taggt ein Image neu, um ihm einen eigenen Versionsnamen zu geben, z.B. für die eigene Registry oder um eine spezifische Konfiguration zu kennzeichnen.
- Beispiel für einen sinnvollen Tag: `meinuser/python-demo:1.0` – der Benutzername identifiziert den Besitzer, der Image-Name beschreibt den Inhalt, und `1.0` ist eine klare Versionsnummer.

---

## Teil C – Sicherheit & Bewertung

Beispiel-Image: **python:3.12-slim**

### Quelle

- Ja, `python` ist ein Official Image auf Docker Hub. Es wird direkt von Docker und der Python-Community gepflegt.
- Gepflegt wird es vom Docker Official Images Team in Zusammenarbeit mit der Python Software Foundation.

### Maintainer

- Ja, das Dockerfile ist öffentlich einsehbar auf GitHub im Repository `docker-library/python`.
- Das ist wichtig, weil man so nachvollziehen kann, was genau im Image enthalten ist, welche Pakete installiert werden und ob es Sicherheitslücken geben könnte. Transparenz schafft Vertrauen.

### Version

- `python:3.12-slim` ist besser als `python:latest`, weil:
  - Die Version 3.12 ist fest definiert – man weiss genau, welche Python-Version läuft.
  - `slim` bedeutet, dass das Image nur die minimal nötigen Pakete enthält (kleiner und sicherer).
  - `latest` könnte sich jederzeit ändern und auf eine andere Python-Version zeigen, was Builds unvorhersehbar macht.

### Risiken prüfen

- Das Image `python:3.12-slim` ist ca. **45-55 MB** gross (komprimiert), entpackt ca. **130-150 MB**.
- Ja, standardmässig läuft der Container als **root**.
- Root ist ein Risiko, weil ein Angreifer, der aus dem Container ausbricht, dann Root-Rechte auf dem Host-System haben könnte. Best Practice ist es, im Dockerfile einen unprivilegierten Benutzer zu erstellen und den Container als diesen Benutzer auszuführen.

---

## Teil D – Reflexion

### Warum speichert Docker Login-Daten in ~/.docker/config.json?

- In `~/.docker/config.json` werden die Zugangsdaten für Registries gespeichert (Benutzername, Auth-Token oder Verweis auf einen Credential Store).
- Man sollte vorsichtig sein, weil die Datei auf macOS/Linux standardmässig lesbar ist. Wenn kein Credential Store (z.B. macOS Keychain) konfiguriert ist, könnten Passwörter im Klartext oder als Base64 gespeichert sein. Die Datei sollte nie in ein Git-Repository committed oder mit anderen geteilt werden.

### Push vs. Pull

- **Pull** = Ein Image von einer entfernten Registry auf den lokalen Rechner herunterladen.
- **Push** = Ein lokales Image in eine entfernte Registry hochladen, damit es dort gespeichert und von anderen genutzt werden kann.

---

## Bonus

**Warum spart Docker Zeit, wenn beim Push steht: „Layer already exists"?**

Docker-Images bestehen aus mehreren Layern (Schichten). Beim Push prüft Docker für jeden Layer, ob er bereits in der Registry vorhanden ist. Wenn ein Layer schon existiert (z.B. weil er aus einem Basis-Image stammt, das schon hochgeladen wurde), wird er nicht erneut übertragen. Das spart Bandbreite und Zeit, da oft nur die obersten, geänderten Layer neu hochgeladen werden müssen.

---

## Lernziel-Kontrolle

- ✅ erklären, was eine Registry ist
- ✅ erklären, warum latest problematisch ist
- ✅ ein Image pullen
- ✅ ein Image taggen
- ✅ ein Image kritisch beurteilen
