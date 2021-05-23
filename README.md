# Build images for TEST API App
## Prerequisites:
- You need a Linux /OSX environment to run the build script. Make sure Python 3.6+ and Docker got installed in the machine.
```
https://docs.docker.com/get-docker/
https://realpython.com/installing-python/
```

# Build and run locally:

## Build base image locally
```
infra/build.py --build-base-image
```

## Build app image locally
```
infra/build.py --build-app-image
```

## Run app image locally
```
docker run --rm -it -p8008:8008 api-test:V0.0.1 .venv/bin/python -m apitest.app
```

### Once Images got built , Try to access below URL from browser.
```
http://localhost:8008/health
```
