# Project Title: Goodreads Book Recommendation System

## Overview

This project presents an advanced book recommendation system utilizing a hybrid approach that amalgamates both item-based and user-based filtering techniques. Leveraging data scraped from Goodreads, the system applies sophisticated data processing and machine learning methodologies to deliver personalized book recommendations to users.

## Development Process

| Process                                     | Description                                                                                                                             | Potential Improvements                                                               |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Web Scraping from Goodreads**             | Implemented asynchronous web scraping techniques to efficiently gather comprehensive book data from Goodreads.                         |                                                                                      |
| **Data Cleaning and Preprocessing**         | Employed robust Natural Language Processing (NLP) techniques and rigorous data cleaning methodologies to ensure data quality.           |                                                                                      |
| **Content-Based Filtering and Synthetic Data Generation** | Integrated content-based filtering techniques, augmented with synthetic data generation to handle missing values.               |                                                                                      |
| **Feature Engineering**                     | Utilized advanced feature engineering strategies to extract meaningful insights from the dataset.                                       |                                                                                      |
| **User and Item Profile Creation**          | Engineered user and item profiles based on book genres, employing dimensionality reduction techniques for enhanced performance.        |                                                                                      |
| **Flask Application Development**           | Developed a robust Flask application featuring a secure login system and dynamic book recommendations.                                 |                                                                                      |
| **Data Storage and Retrieval**              | Utilized PostgreSQL database for efficient data storage and retrieval, employing a combination of API calls and SQL queries.          |                                                                                      |
| **Model Serialization and Deployment**      | Serialized trained models for streamlined deployment using Gunicorn.                                                                   |                                                                                      |
| **Dockerization**                           | Containerized the application for optimized deployment and scalability.                                                               |                                                                                      |
| **CI/CD**                                   | Established a robust CI/CD pipeline using Docker, GCP, and GitHub Actions for seamless integration and deployment.                   |                                                                                      |

## Things That Can Be Improved

1. **Middleware and Caching**: Implement middleware for input validation and utilize Redis for caching database calls to improve performance and efficiency.Adding Logging and testing too would be great for the implementation.

2. **Advanced Techniques**: Explore advanced recommendation techniques such as Neural Collaborative Filtering, Alternating Least Squares (ALS), and Decision Trees (content-based classifier) to enhance recommendation accuracy and diversity.

3. **Implementing Micro-service Design**: Adding Microservices is a better and scalable approach which will use the full capabilities of Cloud, Adding ways to implement database transactions,event Sourcing db,Chuncking big db(AWS_RDS/Google_cloudsql or AWS_S3 ).


## Getting Started

To begin using this project:

1. Clone the repository.
2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Run the application using Gunicorn:

   ```bash
   poetry run gunicorn -w 4 -b 0.0.0.0:8000 main:app
   ```

4. Login using Userid and Password

   The user id and password are given in [JSON FILE](user_info.json)



## License

This project is licensed under the [MIT License](LICENSE).

## Resources

- [GCP documentaion](https://cloud.google.com)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Postgresql](https://www.postgresql.org/docs/)
- [BART documentaion](https://huggingface.co/docs/transformers/main/en/model_doc/bart#transformers.BartForConditionalGeneration)
- [Docker documentation](https://docs.docker.com/)
- [Doc2vec](https://radimrehurek.com/gensim/models/doc2vec.html)
- [User Profiling](https://arxiv.org/html/2402.09660v2)
- [CI-CD pipelines using gcp](https://github.com/google-github-actions/deploy-cloudrun)
- [Other approaches to build recommendations](https://github.com/recommenders-team/recommenders)


