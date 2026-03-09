import docker

client = docker.from_env()

for image in client.images.list():
    try:
        print("Lösche Image:", image.short_id)
        client.images.remove(image.id)
    except docker.errors.APIError as e:
        print("Übersprungen:", image.short_id)
