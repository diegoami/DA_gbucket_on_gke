import os

from flask import Flask

app = Flask(__name__)
json_data = ""
@app.route('/')
def hello_world():
    print(json_data)
    return '{}!\n'.format(json_data)

if __name__ == "__main__":
    from google.cloud import storage
    google_application_credentials = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if (google_application_credentials):
        print(google_application_credentials)
        client = storage.Client.from_service_account_json(google_application_credentials)
    else:
        print("No GOOGLE_APPLICATION_CREDENTIAL env found")
        client = storage.Client()
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('gsbucket-gke')

    # get bucket data as blob
    blob = bucket.get_blob('horsers')
    # convert to string
    json_data = blob.download_as_string()
    print(json_data)

    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))


