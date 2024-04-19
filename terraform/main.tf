provider "google" {
  project     = "kubernetes-assignment-413919"
  region      = "us-central1"
}

resource "google_container_cluster" "primary" {
  name     = "my-gke-cluster"
  location = "us-central1"

  remove_default_node_pool = true
  initial_node_count       = 1

  master_auth {
    client_certificate_config {
      issue_client_certificate = false
    }
  }

  deletion_protection = false
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "e2-micro"

    metadata = {
      disable-legacy-endpoints = "true"
    }

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/servicecontrol",
      "https://www.googleapis.com/auth/service.management.readonly",
      "https://www.googleapis.com/auth/trace.append"
    ]

    disk_size_gb = 10
    disk_type = "pd-standard"
    image_type = "COS_CONTAINERD"
  }
}

resource "google_compute_disk" "default" {
  name  = "my-data-disk"
  type  = "pd-standard"
  size  = "20"
  zone  = "us-central1-a"
  image = "debian-8-jessie-v20170523"
}

