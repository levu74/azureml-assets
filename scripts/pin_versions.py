import argparse
from pathlib import Path

from pin_image_versions import pin_images
from pin_package_versions import pin_packages


def transform_file(input_file: Path, output_file: Path = None):
    # Read Dockerfile
    with open(input_file) as f:
        contents = f.read()

    # Pin images and packages
    contents = pin_images(contents)
    contents = pin_packages(contents)

    # Write to stdout or output_file
    if output_file == "-":
        print(contents)
    else:
        if output_file is None:
            output_file = input_file
        with open(output_file, "w") as f:
            f.write(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, help="File containing images/packages to pin to latest versions", required=True)
    parser.add_argument("-o", "--output", type=Path, help="File to which output will be written. Defaults to the input file if not specified.")
    args = parser.parse_args()

    output = args.output or args.input
    transform_file(args.input, output)
