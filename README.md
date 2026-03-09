# Erste Schritte mit Docker – gesteuert mit Python

## Setup

### 1. Docker starten
Docker Desktop muss laufen:
```bash
open -a Docker
```

### 2. Virtual Environment aktivieren
```bash
source venv/bin/activate
```

### 3. Python-Skripte ausführen

#### Vollständiges Tutorial:
```bash
python tutorial.py
```

#### Einfacher Test:
```bash
python docker_start.py
```

#### Container löschen:
```bash
python container_loeschen.py
```

#### Images löschen:
```bash
python images_loeschen.py
```

## Python-REPL verwenden

```bash
source venv/bin/activate
python
```

Dann im REPL:
```python
import docker
client = docker.from_env()
client.ping()  # Sollte True zurückgeben
```

## Nützliche Befehle

### Docker CLI vs Python

| Aufgabe | Python | Docker CLI |
|---------|--------|------------|
| Verbindung prüfen | `client.ping()` | `docker info` |
| Image herunterladen | `client.images.pull("ubuntu:latest")` | `docker pull ubuntu:latest` |
| Container starten | `client.containers.run(...)` | `docker run ...` |
| Container anzeigen | `client.containers.list()` | `docker ps` |
| Container stoppen | `container.stop()` | `docker stop <name>` |
| Container löschen | `container.remove()` | `docker rm <name>` |
