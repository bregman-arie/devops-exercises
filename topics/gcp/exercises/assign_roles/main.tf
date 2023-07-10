locals {
  roles = [
    "roles/compute.storageAdmin",
    "roles/compute.networkAdmin",
    "roles/compute.securityAdmin"
  ]
}

resource "google_service_account" "some_member" {
  account_id   = "${substr(var.env_id, 0, min(length(var.env_id), 10))}-some-member"
  display_name = "${var.env_id} some-member"
}

resource "google_project_iam_member" "storageAdminMaster" {
  for_each = toset(concat(local.roles))
  project  = "${var.project_id}"
  role     = each.key
  member   = "serviceAccount:${google_service_account.some_member.email}"
}