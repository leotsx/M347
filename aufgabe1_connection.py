import docker

def main():
    try:
        client = docker.from_env()
        if client.ping():
            print("✅ Verbindung zu Docker klappt.")
    except Exception as error:
        print("❌ Keine Verbindung zu Docker.")
        print("Tipp: Ist Docker gestartet?")
        print("Fehler:", error)
        return

    info = client.version()
    print("\n--- Docker-Infos ---")
    print("Docker-Version:", info.get("Version"))
    print("Betriebssystem:", info.get("Os"))
    print("Architektur:", info.get("Arch"))

if __name__ == "__main__":
    main()
