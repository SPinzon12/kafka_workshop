# Happiness Score Prediction with Regression Model and Kafka Streaming
This project aims to build a regression machine learning model to predict happiness scores in different countries based on data from five CSV files. The entire process includes Exploratory Data Analysis (EDA), Extract, Transform, Load (ETL) operations, model training, streaming transformed data using Kafka, and evaluating model performance.

## About the data
The data used in this project is from [Kaggle](https://www.kaggle.com/unsdsn/world-happiness). The dataset includes happiness information of various countries over different years. The datasets include multiple variables that contribute to the evaluation of a country's happiness.

## About the model
This project employs a Random Forest Regressor, a powerful machine learning algorithm,to predict happiness scores. The model is implemented using the `RandomForestRegressor` function from the `sklearn` library.

The Random Forest Regressor model achieved an R-squared of 0.79, indicating a strong performance in capturing the variance in the happiness scores.

## About the Kafka Streaming
The project utilizes Kafka to stream the transformed data. The Kafka Producer is implemented in `kafka_producer.py`, and the Kafka Consumer is implemented in `kafka_consumer.py`.

## Getting Started
To start using the project, follow these steps:

1. **Clone the Repository:**
   - Clone the project repository in your development environment.

2. **Install the Required Libraries:**
   - Install the necessary libraries listed in the `requirements.txt` file. You can do this using a package manager like pip in Python. Run the following command:

     ```
     pip install -r requirements.txt
     ```

3. **Configure the PostgreSQL Database Connection:**
   - Create a `db_config.json` file in the project root directory.

        ```json
        {
            "user": "your_postgres_username",
            "password": "your_postgres_password",
            "database": "your_postgres_database"
        }
        ```

4. **Setting up Kafka:**
   - Run Docker Compose:
        ```bash
        docker-compose up
        ```
   - Access Kafka Container:
        ```bash
        docker exec -it kafka bash 
        ```
   - Create Kafka Topic:
        
        Inside the Kafka container, run the following command to create a Kafka topic named `kafka-happiness`:
        ```bash
        kafka-topics --bootstrap-server kafka --create --topic kafka-happiness 
        ```  
        This command sets up a Kafka topic that will be used for streaming happiness data.

5. **Running the Strem:**
    - Open two new terminals and run the following command in each terminal:
        ```bash
        python kafka_consumer.py
        ```
        ```bash
        python kafka_producer.py
        ```

        **Note:** Make sure to run the consumer first.


## Contact
If you have any questions, please feel free to contact me via [sampinval@gmail.com].




