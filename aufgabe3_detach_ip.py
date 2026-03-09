import docker

def main():
    client = docker.from_env()

    print("📥 Lade Image alpine:latest ...")
    client.images.pull("alpine:latest")

    print("\n🚀 Starte Container im Hintergrund ...")
    container = client.containers.run(
        "alpine:latest",
        "sleep 30",
        detach=True
    )
    print("✅ Container-Name:", container.name)

    print("\n📋 Laufende Container:")
    for running_container in client.containers.list():
        print("-", running_container.name, "| Status:", running_container.status)

    container.reload()
    networks = container.attrs["NetworkSettings"]["Networks"]
    print("\n🌐 Netzwerk-Infos:")
    for network_name, network_data in networks.items():
        print("Netzwerk:", network_name)
        print("IP:", network_data.get("IPAddress"))

    print("\n🧹 Aufräumen ...")
    container.stop()
    container.remove()
    print("✅ Container gestoppt und gelöscht.")

if __name__ == "__main__":
    main()
