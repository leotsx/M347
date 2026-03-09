import docker

# Verbindung zu Docker herstellen
client = docker.from_env()

# Verbindung prüfen
print("=== Verbindung zu Docker prüfen ===")
print("Verbindung:", client.ping())

# Docker-Version anzeigen
print("\n=== Infos über Docker anzeigen ===")
info = client.version()
print("Docker-Version:", info.get("Version"))
print("API-Version:", info.get("ApiVersion"))
print("Betriebssystem:", info.get("Os"))
print("Architektur:", info.get("Arch"))

# Ubuntu-Image herunterladen
print("\n=== Erstes Image herunterladen ===")
client.images.pull("ubuntu:latest")
print("Ubuntu-Image ist bereit.")

# Ersten Container starten
print("\n=== Ersten Container starten ===")
output = client.containers.run(
    "ubuntu:latest",
    "echo Hallo aus dem Container!",
    remove=True
)
print(output.decode())

# Alpine-Image testen
print("\n=== Anderes Image testen (Alpine) ===")
client.images.pull("alpine:latest")
output = client.containers.run(
    "alpine:latest",
    "echo Hallo von Alpine",
    remove=True
)
print(output.decode())

# Container im Hintergrund starten
print("\n=== Container im Hintergrund starten ===")
container = client.containers.run(
    "alpine:latest",
    "sleep infinity",
    detach=True
)
print("Container gestartet:", container.name)

# Laufende Container anzeigen
print("\n=== Laufende Container anzeigen ===")
for c in client.containers.list():
    print(c.name, "-", c.status)

# IP-Adresse anzeigen
print("\n=== IP-Adresse des Containers anzeigen ===")
container.reload()
networks = container.attrs["NetworkSettings"]["Networks"]
for name, data in networks.items():
    print("Netzwerk:", name)
    print("IP-Adresse:", data["IPAddress"])

# Container stoppen und löschen
print("\n=== Container stoppen und löschen ===")
container.stop()
container.remove()
print("Container beendet und gelöscht.")

print("\n=== Fertig ===")
