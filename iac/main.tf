# Configure Google Cloud Provider
provider "google" {
  credentials = file("credentials.json")
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Create a GCE instance
resource "google_compute_instance" "example_instance" {
  name         = "test-instance"
  machine_type = "f1-micro"
  zone         = var.zone

  # Boot Disk
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  # Network Interface
  network_interface {
    network = "default"
  }

  # Tags
  tags = ["http-server", "https-server"]

  # Startup script to install required dependencies
  metadata_startup_script = file("scripts/startup-script.sh")
}