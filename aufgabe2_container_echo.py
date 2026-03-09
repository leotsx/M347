import docker

def main():
    client = docker.from_env()

    print("📥 Lade Image ubuntu:latest ...")
    client.images.pull("ubuntu:latest")
    print("✅ Image bereit.\n")

    command = "bash -lc 'echo Hallo aus dem Container!; whoami; uname -s'"
    output = client.containers.run(
        "ubuntu:latest",
        command,
        remove=True
    )

    print("--- Ausgabe aus dem Container ---")
    print(output.decode().strip())

if __name__ == "__main__":
    main()
