import docker
import json
import os


def connect():
    try:
        client = docker.from_env()
        if client.ping():
            print("✅ Verbindung zu Docker hergestellt.")
        return client
    except Exception as error:
        print("❌ Keine Verbindung zu Docker.")
        print("Tipp: Ist Docker Desktop gestartet?")
        print("Fehler:", error)
        return None


def search_image(client):
    term = input("\n🔍 Nach welchem Image möchtest du suchen? ")
    results = client.images.search(term, limit=5)
    if not results:
        print("Keine Ergebnisse gefunden.")
        return None
    print(f"\n--- Suchergebnisse für '{term}' ---")
    for i, img in enumerate(results, 1):
        official = "⭐ Official" if img.get("is_official") else "  Community"
        name = img.get("name", "unbekannt")
        desc = img.get("description", "")[:60]
        stars = img.get("star_count", 0)
        print(f"  {i}. [{official}] {name} ⭐{stars}")
        print(f"     {desc}")
    return results


def pull_image(client):
    image_name = input("\n📥 Welches Image möchtest du pullen (z.B. python:3.12-slim)? ")
    print(f"Lade '{image_name}' herunter...")
    try:
        image = client.images.pull(image_name)
        print(f"✅ Image gepullt: {image.tags}")
        print(f"   ID: {image.short_id}")
        print(f"   Grösse: {image.attrs['Size'] / 1024 / 1024:.1f} MB")
        return image
    except Exception as error:
        print(f"❌ Fehler beim Pull: {error}")
        return None


def tag_image(image):
    if image is None:
        print("⚠️  Kein Image zum Taggen vorhanden.")
        return
    print("\n--- Image taggen ---")
    print("Aktuell:", image.tags)
    new_repo = input("Neuer Repository-Name (z.B. meinuser/python-demo): ")
    new_tag = input("Neuer Tag (z.B. 1.0): ")
    if new_repo and new_tag:
        success = image.tag(new_repo, tag=new_tag)
        if success:
            print(f"✅ Image getaggt als: {new_repo}:{new_tag}")
        else:
            print("❌ Tagging fehlgeschlagen.")
    else:
        print("⚠️  Übersprungen (leere Eingabe).")


def push_image(client):
    print("\n--- Push (optional) ---")
    do_push = input("Möchtest du ein Image pushen? (j/n): ").strip().lower()
    if do_push != "j":
        print("Push übersprungen.")
        return
    username = input("Docker Hub Benutzername: ")
    password = input("Docker Hub Passwort: ")
    try:
        client.login(username=username, password=password)
        print("✅ Login erfolgreich.")
    except Exception as error:
        print(f"❌ Login fehlgeschlagen: {error}")
        return
    repo = input("Welches Image pushen (z.B. meinuser/python-demo:1.0)? ")
    print(f"Pushe '{repo}'...")
    for line in client.images.push(repo, stream=True, decode=True):
        status = line.get("status", "")
        if status:
            progress = line.get("progress", "")
            print(f"  {status} {progress}")
    print("✅ Push abgeschlossen.")


def check_docker_config():
    print("\n--- Docker Login-Konfiguration ---")
    config_path = os.path.expanduser("~/.docker/config.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        print(f"📄 Datei gefunden: {config_path}")
        auths = config.get("auths", {})
        if auths:
            print("   Gespeicherte Registries:")
            for registry in auths:
                print(f"     - {registry}")
        else:
            print("   Keine gespeicherten Logins gefunden.")
        cred_store = config.get("credsStore", None)
        if cred_store:
            print(f"   Credential Store: {cred_store}")
            print("   ℹ️  Passwörter werden sicher im System-Keystore gespeichert.")
    else:
        print("   Keine config.json gefunden. Noch kein Login durchgeführt.")


def security_checklist(client, image):
    print("\n" + "=" * 50)
    print("🔒 IMAGE-SICHERHEITS-CHECKLISTE")
    print("=" * 50)
    if image is None:
        print("⚠️  Kein Image vorhanden. Übersprungen.")
        return

    tags = image.tags if image.tags else ["<kein Tag>"]
    print(f"\nImage: {tags[0]}")
    print(f"ID:    {image.short_id}")
    size_mb = image.attrs["Size"] / 1024 / 1024
    print(f"Grösse: {size_mb:.1f} MB")

    labels = image.labels
    if labels:
        print("\nLabels/Metadaten:")
        for key, value in labels.items():
            print(f"  {key}: {value}")
    else:
        print("\nKeine Labels/Metadaten vorhanden.")

    history = image.history()
    print(f"\nAnzahl Layer: {len(history)}")
    print("Letzte Layer-Befehle:")
    for layer in history[:5]:
        cmd = layer.get("CreatedBy", "")[:80]
        if cmd:
            print(f"  - {cmd}")

    print("\n--- Bitte beantworten ---")
    print("1. Ist es ein Official Image?")
    print("2. Wer ist der Maintainer?")
    print("3. Wird eine feste Version genutzt (nicht :latest)?")
    print(f"4. Wie gross ist das Image? → {size_mb:.1f} MB")
    print("5. Läuft es als root?")
    print("6. Ist das Dockerfile öffentlich einsehbar?")


def main():
    print("=" * 50)
    print("  DL5 – Registries & Image-Workflow")
    print("=" * 50)

    client = connect()
    if client is None:
        return

    # 1. Image suchen
    search_image(client)

    # 2. Image pullen
    image = pull_image(client)

    # 3. Image taggen
    tag_image(image)

    # 4. Push (optional)
    push_image(client)

    # 5. Docker-Konfiguration prüfen
    check_docker_config()

    # 6. Sicherheits-Checkliste
    security_checklist(client, image)

    print("\n✅ Übung abgeschlossen!")


if __name__ == "__main__":
    main()
