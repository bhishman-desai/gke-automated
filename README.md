# gke-automated

# Google Cloud Platform (GCP) with Terraform and Kubernetes

This project is a journey through Google Cloud Platform (GCP) using Terraform to create a Kubernetes cluster from scratch. The process navigates the GCP Cloud Shell, and once the GKE cluster is up and running, it showcases a CI/CD pipeline. Code changes trigger the pipeline, leading to a new image being deployed to the GKE cluster. All of this is done within the Cloud Shell, with code cloned directly from the Cloud Source Repository. This project serves as a comprehensive guide to GKE, Terraform, and CI/CD pipelines.

## Key Takeaways

- **Provisioning resources on Google Cloud Platform (GCP) using Terraform**: The project sets up and manages resources on GCP using the powerful IaC tool, Terraform.

- **Using the Cloud Source Repository for effective version control and code storage**: The project uses the Cloud Source Repository. Triggers on the repository kickstart an automatic build and deploy process every time there’s a code push.

- **Exploring the Artifact Registry**: The project explores the Artifact Registry, a haven for storing images.

- **Delving into the world of Kubernetes**: The project delves into the world of Kubernetes, creating pods, persistent volumes, and services using Kubernetes objects in the deployment file.

## Getting Started

To get started with this project, GCP, Terraform, and Kubernetes need to be installed. Follow the instructions in the [video](https://www.youtube.com/watch?v=T4SojEoboSw). to set up the environment.

## Contributing

Contributions to enhance the app's functionality or address any issues are welcome. Feel free to use the provided source code as a reference for creating similar applications for your institution.

## License

This project is licensed under the [MIT License](LICENSE).