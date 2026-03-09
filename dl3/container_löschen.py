import docker

client = docker.from_env()

for container in client.containers.list(all=True):
    print("Stoppe:", container.name)
    container.stop()

    print("Lösche:", container.name)
    container.remove()
