import os
import subprocess
import argparse

app_name = "testapi"

base_version = '0.0.1'
os.environ["BASE_NAME"] = f"base-V{base_version}"
os.environ["APP_VERSION"] = f"V{base_version}"


def build_base_image():
    try:
        result = subprocess.check_call(["docker-compose", "-f", "./docker-compose.yml", "build", "base"])
        print(result)
    except subprocess.CalledProcessError as err:
        print(err)
        raise


def build_app_image():

    app_image_name = os.environ["APP_IMAGE_NAME"]
    print("APP_IMAGE_NAME: {}".format(app_image_name))
    try:
        subprocess.check_call(["docker-compose", "-f", "./docker-compose.yml", "build", "app"])
    except subprocess.CalledProcessError as err:
        print(err)
        raise
    return app_image_name


def arguments_parser():
    parser = argparse.ArgumentParser(description="Build Apps steps", add_help=True)
    parser.add_argument("--build-base-image", action="store_true", default=False)
    parser.add_argument("--build-app-image", action="store_true", default=False)
    return parser


def serialise_job_arg(action):
    return "{0}, required={1}, help={2}".format(action.option_strings, action.required, action.help)


if __name__ == "__main__":
    args = arguments_parser().parse_args()

    if args.build_base_image:
        build_base_image()
    elif args.build_app_image:
        build_app_image()
    else:
        arguments_parser().print_usage()
