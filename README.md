# Predict that Dish

![](/extras/home_page.png)

## Description

![](/extras/Architecture.png)

This web service can be queried to obtain the prediction of a dish from a trained neural network using the Amazon EC2 Instance. The aim of this project is to create a usable piece of software that harnesses the inference capabilities of a deep learning model for stakeholders to consume.

## Workflow

1. Training a neural network on a local system or cloud servers like Google Colab.

2. Wrapping the model along with its inference logic into a flask application.

3. Developing a frontend using React and connecting it to the backend flask application.

4. Creating an EC2 instance and configuring the NGINX reverse proxy server to handle connections from users over the Internet.

5. Hosting the application on an AWS EC2 instance.

## Neural Network Training Details

[Training Dataset](https://www.kaggle.com/datasets/kmader/food41)

Training Code with Results and Detailed Analysis: [link](https://github.com/KingJulius/Predict-that-Dish/blob/main/training/efficientnetb0-train.ipynb)

Trained Models: [link](https://github.com/KingJulius/Predict-that-Dish/tree/main/server/artifacts/efficientnetb0)

## Procedure To Deploy this Application using the EC2 Instance:

1. Clone this Repository.

2. Follow Client Side Setup.

3. Follow Server Side Setup.

4. Can be deployed on local machine or a service via the cloud.

## Client Side Setup and Build

### Setup

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))

2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))

3. Install dependencies

```bash
cd client
npm install --from-lock-json
npm audit fix
```

4. Copy `.env.example` as `.env`.

5. Change API url in `.env`.

### Running the Client:

1. Get inside `client` folder

```bash
cd client
```

2. Update `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.

3. Run the client

```bash
npm run start
```

4. Builds the app for production to the `build` folder.

```bash
npm run build
```

It correctly bundles React in production mode and optimizes the build for the best performance.
The build is minified and the filenames include the hashes.
Your app is ready to be deployed!

## Server Side Setup

### Flask Web App Setup & Installtion:

1. Make sure you have the latest version of Python installed and pip.

2. Install All the Dependencies.

```bash
pip install requirements.txt
```

### Running The Server:

```bash
python server.py
```

## Deploying Application to the Cloud (AWS EC2)

1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic and connect to it.

2. Clone client build and server to the instance.

3. NGINX setup

   1. Install nginx on EC2 instance using these commands,

   ```
   sudo apt-get update
   sudo apt-get install nginx
   ```

   2. Above will install nginx as well as run it. Check status of nginx using

   ```
   sudo service nginx status
   ```

   3. Here are the commands to start/stop/restart nginx

   ```
   sudo service nginx start
   sudo service nginx stop
   sudo service nginx restart
   ```

   4. Now when you load cloud url in browser you will see a message saying "welcome to nginx" This means your nginx is setup and running.

4. Now you need to copy all your code to EC2 instance. You can upload the application using git clone on the server.

5. After copying code on EC2 server now we can point nginx to load our property website by default. For below steps,

   1. Create this file /etc/nginx/sites-available/ptd.conf. The file content looks like this,

   ```
   server {
       listen 80;
           server_name bhp;
           root /home/ubuntu/Predict-that-Dish/client/build;
           index index.html;
           location /api/ {
                rewrite ^/api(.*) $1 break;
                proxy_pass http://127.0.0.1:5000;
           }
   }
   ```

   2. Create symlink for this file in /etc/nginx/sites-enabled by running this command,

   ```
   sudo ln -v -s /etc/nginx/sites-available/ptd.conf
   ```

   3. Remove symlink for default file in /etc/nginx/sites-enabled directory,

   ```
   sudo unlink default
   ```

   4. Restart nginx,

   ```
   sudo service nginx restart
   ```

6. Now install python packages and start flask server

```
sudo apt-get install python3-pip
sudo pip3 install -r /home/ubuntu/Predict-that-Dish/server/requirements.txt
python3 /home/ubuntu/Predict-that-Dish/server/server.py
```

After successfully performing all the above steps, the Web Service can be accessed over the Internet using the EC2 Instance! 

Link:  
## Future Scope:

The model could be improved by increasing the number of layers and training the model over many more epochs. To improve performance even further we could potentially isolate the background noise by using an object detection network to create bounding boxes to focus on the relevant part of the image. A drawback to consider is the limited type of labels and would need to increase range for wide scale adoption in current stage. Will improve upon current results in the near future.

## References:

1. https://github.com/codebasics
2. https://www.twilio.com/blog/deploy-flask-python-app-aws
3. https://enrico-portolan.medium.com/how-to-host-react-app-with-nginx-634ad0c8425a
4. https://blog.devgenius.io/using-nginx-to-serve-react-application-static-vs-proxy-69b85f368e6c
