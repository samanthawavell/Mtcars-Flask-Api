# Mtcars-Flask-Api

This project builds and deploys a simple Flask API that serves a linear regression model trained on the mtcars.csv dataset. The model predicts miles per gallon (mpg) based on other car attributes. It is containerized with Docker and deployable to Google Cloud Run.

This repo contains the following files:

- Dockerfile: Builds a lightweight image to train the model and run the Flask API server.
- mtcars.csv: Dataset containing vehicle specs and fuel efficiency (mpg). Note that the first column of the database (Model) has been deleted (non-numeric data).
- train_model.py: Trains the linear regression model using statsmodels, adds a constant term, and saves the model and column structure using joblib.
- app.py: Flask API with two endpoints: a health check (/) and prediction endpoint (/predict). Loads the trained model and matches input features.
- requirements.txt: Python dependencies: Flask, Pandas, Statsmodels, Joblib.
- linear_model_mtcars.py: A standalone script used to fit the model and print the summary, for local experimentation.

HOW TO USE THE API:

1. Ensure you have the following files saved in one folder:

Dockerfile
mtcars.csv
train_model.py
app.py
requirements.txt

2. If using Apple Silicon (M1/M2), use buildx to ensure compatibility with Google Cloud Run:

docker buildx create --use
docker buildx build --platform linux/amd64 -t YOUR_DOCKERHUB_USERNAME/mtcars-api:latest --push .
Replace YOUR_DOCKERHUB_USERNAME with your Docker Hub username.

3. Make sure gcloud is installed, authenticated, billing enabled, and you're using a valid PROJECT_ID:

gcloud config set project YOUR_PROJECT_ID

gcloud run deploy mtcars-api \
  --image=docker.io/YOUR_DOCKERHUB_USERNAME/mtcars-api:latest \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated \
  --port=8080

4. Once deployed, your endpoint will be something like:

https://mtcars-api-abc123-uc.a.run.app

You can test it using curl:

curl -X POST https://mtcars-api-abc123-uc.a.run.app/predict \
  -H "Content-Type: application/json" \
  -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'

It should return the following output:

{"mpg_prediction":22.59950576126212}
