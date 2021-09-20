# REFERENCES

## CREATE PYTHON CORE PROJECT

* How to deploy on GKE: https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploying-a-language-specific-app#python_1

```
gcloud auth login
gcloud config set project gbucket-on-gke
```


Check if artifact repository API is enabled

```
https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com?authuser=1&project=gbucket-on-gke
```

Create Dockerfile and Submit it to the artifact registry

```
gcloud artifacts repositories create hello-repo --project=gbucket-on-gke --repository-format=docker --location=europe-west1 --description="Hello Repo on Gbucket"
gcloud builds submit --tag europe-west1-docker.pkg.dev/gbucket-on-gke/hello-repo/helloworld-gke .
gcloud artifacts repositories list
```

## 


