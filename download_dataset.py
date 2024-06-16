import os
import argparse
import requests
from tqdm import tqdm
from zipfile import ZipFile

def download_file(session, url, data_dir):
    response = session.get(url, stream=True)
    response.raise_for_status()  # Check for any errors during file download

    # Get the filename from the content-disposition header
    filename = url.split('=')[-1] + '.zip'  # Assuming the files are .zip format
    if 'content-disposition' in response.headers:
        content_disposition = response.headers['content-disposition']
        if 'filename=' in content_disposition:
            filename = content_disposition.split('filename=')[1].strip('"')

    # Create the full path for the file
    file_path = os.path.join(data_dir, filename)

    # Save the file with a progress bar
    total_size = int(response.headers.get('content-length', 0))
    with open(file_path, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

    return file_path

def unzip_file(file_path, data_dir):
    with ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
        print(f"Unzipped: {file_path}")

def main(username, password, data_dir, package_ids, unzip):
    # Define the login URL
    login_url = 'https://www.cityscapes-dataset.com/login/'

    # Define the login payload
    payload = {
        'username': username,
        'password': password,
        'submit': 'Login'
    }

    # Create the directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    # Start a session
    session = requests.Session()

    # Perform the login
    response = session.post(login_url, data=payload)
    response.raise_for_status()  # Check for any errors during login

    # Generate the file URLs based on the package IDs
    file_urls = [f'https://www.cityscapes-dataset.com/file-handling/?packageID={package_id}' for package_id in package_ids]

    # Download and unzip the files
    for url in file_urls:
        file_path = download_file(session, url, data_dir)
        if unzip:
            unzip_file(file_path, data_dir)

    print("Files downloaded and unzipped successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and unzip files from Cityscapes dataset with login.")
    parser.add_argument("--username", required=True, help="Your username for the Cityscapes dataset login.")
    parser.add_argument("--password", required=True, help="Your password for the Cityscapes dataset login.")
    parser.add_argument("--data-dir", required=True, help="Directory to save and unzip the downloaded files.")
    parser.add_argument("--package-ids", required=True, help="Comma-separated list of package IDs to download.", type=lambda s: [int(item) for item in s.split(',')])
    parser.add_argument("--unzip", action="store_true", help="Flag to unzip the downloaded files.")

    args = parser.parse_args()
    main(args.username, args.password, args.data_dir, args.package_ids, args.unzip)
