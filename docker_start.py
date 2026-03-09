import docker

client = docker.from_env()

print("Verbindung:", client.ping())

print("\nDocker-Info:")
info = client.version()
print(info.get("Version"), "-", info.get("Os"))

print("\nUbuntu-Test:")
out = client.containers.run(
    "ubuntu:latest",
    "echo Hallo aus Python und Docker!",
    remove=True
)
print(out.decode())

print("\nFertig.")
