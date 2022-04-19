# Predict that Dish

![](home_page.png)

## Objective

A Web Application that uses a trained Neural Network hosted by a server to predict the label of an input image sent by the client

## Architecture

Front End - ReactJS

Back End - Flask

Model - Developed using TensorFlow

# Neural Network Development

Training Dataset: https://www.kaggle.com/datasets/kmader/food41

Training Code with Results and Analysis:

[link](https://github.com/KingJulius/Predict-that-Dish/blob/main/training/efficientnetb0-train.ipynb)

Trained Models:

[link](https://github.com/KingJulius/Predict-that-Dish/tree/main/server/artifacts/efficientnetb0)


# To run the web application

1. Clone this Repository
2. Follow Client Side and Server Side setup specified below



# Client Side

## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Install dependencies

```bash
cd client
npm install --from-lock-json
npm audit fix
```

4. Change API url in `.env`.

## Running the client

1. Get inside `client` folder

```bash
cd client
```

2. Update `REACT_APP_API_URL` to API URL if needed in `.env`.
3. Run the frontend

```bash
npm run start
```


# Server Side

## Flask Web App Setup & Installtion

1. Make sure you have the latest version of Python installed.

2. Install All the Dependencies.
```bash
pip install requirements.txt
```

## Running The App

```bash
python server.py
```
