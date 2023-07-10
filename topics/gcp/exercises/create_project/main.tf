resource "google_project" "gcp_project" {
  name       = "Some Project"
  project_id = "some-unique-project-id"
  folder_id  = google_folder.some_folder.name
}

resource "google_folder" "some_folder" {
  display_name = "Department 1"
  parent       = "organizations/some-organization"
}