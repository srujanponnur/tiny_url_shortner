# tiny_url_shortner
Tiny Url shortner to generate shortened version of a promotional URL - useful for easy redirection, tracking the number of hits and other use cases

## Design Details
1. Saved the user details and the URL data in AWS Dynamo DB
2. Generated the short url using hashing when the user input is not provided.
3. Deployed the service in Amazon ECS Service to scale the container's based on load.
