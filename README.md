# Build images for TEST API App
## Prerequisites:
- You need a Linux /OSX environment to run the build script. Make sure Docker got installed in the machine.
```
https://docs.docker.com/get-docker/
```

# Build and run locally:

## Build base image locally
```
infra/build.py --build-base-image
```

## Build app image locally
```
infra/build.py --build-base-image
```

## Run app image locally
```
docker run --rm -it -p8008:8008 api-test:V0.0.1 .venv/bin/python -m apitest.app
```

### Once Images got built , Try to access below URL from browser.
```
http://localhost:8008/
```
