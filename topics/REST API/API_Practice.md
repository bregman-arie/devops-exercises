# My Journey Through Core API Concepts

Today was a fantastic day for learning! I dove into the practical side of APIs and RESTful services. This document is my personal log of the key operations I practiced, from simple data fetching to more complex authenticated updates. I've included the exact scripts for both Linux (bash) and Windows (PowerShell) that I used, along with my thoughts on what I learned from each task.

## Table of Contents
- [My Journey Through Core API Concepts](#my-journey-through-core-api-concepts)
  - [Table of Contents](#table-of-contents)
    - [1. Basic GET Request (Fetch data)](#1-basic-get-request-fetch-data)
    - [2. GET with Query Parameters (Filtered request)](#2-get-with-query-parameters-filtered-request)
    - [3. POST Request (Create a resource)](#3-post-request-create-a-resource)
    - [4. PUT Request (Replace a resource)](#4-put-request-replace-a-resource)
    - [5. PATCH Request (Update part of a resource)](#5-patch-request-update-part-of-a-resource)
    - [6. DELETE Request (Remove a resource)](#6-delete-request-remove-a-resource)
    - [7. Headers \& Authentication (API Key / Token)](#7-headers--authentication-api-key--token)
    - [8. Update GitHub Profile (PATCH with Bearer Token)](#8-update-github-profile-patch-with-bearer-token)
    - [9. Loop / Automation (Multiple requests)](#9-loop--automation-multiple-requests)
    - [10. Conditional Logic (Check response \& act)](#10-conditional-logic-check-response--act)

---

### 1. Basic GET Request (Fetch data)
My first step was to simply fetch data. I learned how to make a basic `GET` request to retrieve a list of all posts. This is the foundation of consuming any API.

**Linux (bash)**
```bash
#!/bin/bash
# Fetch all posts from JSONPlaceholder
curl -s -X GET https://jsonplaceholder.typicode.com/posts
```

- `-s`: Stands for **silent mode**; it hides progress, errors, and download info, so only the response body is shown.
- `-X GET` → Tells curl which HTTP method to use (GET, POST, PUT, etc.).

**Windows PowerShell**
```powershell
# Fetch all posts
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts" -Method GET
```

---

### 2. GET with Query Parameters (Filtered request)
Next, I explored how to filter results. By adding a query parameter (`?userId=1`), I could ask the API to return only the posts belonging to a specific user. This is incredibly useful for getting targeted data.

**Linux (bash)**
```bash
#!/bin/bash
# Fetch posts by userId=1
curl -s "https://jsonplaceholder.typicode.com/posts?userId=1"
```

- The `?` in a URL is used to start query parameters.
- Anything after `?` is `key=value` pairs that modify the request.
- Multiple parameters are separated by `&`.

**Windows PowerShell**
```powershell
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts?userId=1" -Method GET
```

---

### 3. POST Request (Create a resource)
After fetching data, I learned how to create it. This `POST` request taught me how to send a JSON payload in the request body to create a new resource on the server.

**Linux (bash)**
```bash
#!/bin/bash
curl -s -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"foo","body":"bar","userId":1}'
```
- `-H`: Headers provide metadata or instructions to the server, like content type, authentication, or what format you want in the response.
  - **in short**: *add this metadata or instruction to my request*
- `-d`: It is used to **send data** in the request body, usually with POST, PUT, or PATCH requests.

**Windows PowerShell**
```powershell
$body = @{ title="foo"; body="bar"; userId=1 } | ConvertTo-Json
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts" -Method POST `
-Headers @{ "Content-Type"="application/json" } -Body $body
```

---

### 4. PUT Request (Replace a resource)
Here, I learned about idempotency with `PUT`. This request replaces an *entire* existing resource. I had to provide all the fields for the post, even the ones that weren't changing.

**Linux (bash)**
```bash
#!/bin/bash
curl -s -X PUT https://jsonplaceholder.typicode.com/posts/1 \
-H "Content-Type: application/json" \
-d '{"id":1,"title":"new title","body":"new body","userId":1}'
```

**Windows PowerShell**
```powershell
$body = @{ id=1; title="new title"; body="new body"; userId=1 } | ConvertTo-Json
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts/1" -Method PUT `
-Headers @{ "Content-Type"="application/json" } -Body $body
```

---

### 5. PATCH Request (Update part of a resource)
`PATCH` was a great discovery for efficiency. Unlike `PUT`, it allows me to update just a *part* of a resource. In this case, I only sent the `title` field to be updated, which is perfect for small changes.

**Linux (bash)**
```bash
#!/bin/bash
curl -s -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
-H "Content-Type: application/json" \
-d '{"title":"patched title"}'
```

**Windows PowerShell**
```powershell
$body = @{ title="patched title" } | ConvertTo-Json
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts/1" -Method PATCH `
-Headers @{ "Content-Type"="application/json" } -Body $body
```

---

### 6. DELETE Request (Remove a resource)
To complete the CRUD (Create, Read, Update, Delete) cycle, I practiced deleting a resource. This was a straightforward request to a specific resource's URL that removed it from the server.

**Linux (bash)**
```bash
#!/bin/bash
curl -s -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Windows PowerShell**
```powershell
Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts/1" -Method DELETE
```

---

### 7. Headers & Authentication (API Key / Token)
This task was about understanding that requests have metadata called headers. I practiced sending an `Accept` header to tell the server what kind of response format I expected.

**Linux (bash)**
```bash
#!/bin/bash
# Example with Reqres API (no auth required, practice header)
curl -s -X GET https://reqres.in/api/users/2 \
-H "Accept: application/json"
```

**Windows PowerShell**
```powershell
Invoke-RestMethod -Uri "https://reqres.in/api/users/2" -Method GET `
-Headers @{ "Accept"="application/json" }
```

---

### 8. Update GitHub Profile (PATCH with Bearer Token)
This was a big step! I learned how to make an authenticated request using a Personal Access Token (PAT). By sending an `Authorization` header with my token, I was able to securely update my own GitHub profile bio. This is a core concept for DevOps automation.

**Linux (bash)**
```bash
#!/bin/bash
TOKEN="YOUR_GITHUB_PAT"
curl -s -X PATCH https://api.github.com/user \
-H "Authorization: token $TOKEN" \
-H "Accept: application/vnd.github.v3+json" \
-H "Content-Type: application/json" \
-d '{"bio":"Updated via API"}'
```

**Windows PowerShell**
```powershell
$token = "YOUR_GITHUB_PAT"
$body = @{ bio = "Updated via API" } | ConvertTo-Json
Invoke-RestMethod -Uri "https://api.github.com/user" -Method PATCH `
-Headers @{
    Authorization = "token $token"
    Accept = "application/vnd.github.v3+json"
    "Content-Type" = "application/json"
} -Body $body
```

---

### 9. Loop / Automation (Multiple requests)
I then moved on to automation. Using a simple `for` loop, I wrote a script to download the first five posts and save each one to a separate JSON file. This showed me how powerful scripting can be for handling multiple API calls.

**Linux (bash)**
```bash
#!/bin/bash
for i in {1..5}; do
    curl -s "https://jsonplaceholder.typicode.com/posts/$i" -o "post_$i.json"
done
```

**Windows PowerShell**
```powershell
for ($i=1; $i -le 5; $i++) {
    Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts/$i" -Method GET |
    ConvertTo-Json | Out-File "post_$i.json"
}
```

---

### 10. Conditional Logic (Check response & act)
Finally, I learned how to make my scripts 'smarter'. By checking the HTTP status code of the response, my script could determine if a request was successful (`200 OK`) and then perform different actions based on the outcome. This is essential for building reliable automation.

**Linux (bash)**
```bash
#!/bin/bash
response=$(curl -s -o /dev/null -w "%{http_code}" https://jsonplaceholder.typicode.com/posts/1)
if [ "$response" -eq 200 ]; then
  echo "Post exists"
else
  echo "Post not found"
fi
```

**Windows PowerShell**
```powershell
$response = Invoke-WebRequest -Uri "https://jsonplaceholder.typicode.com/posts/1" -UseBasicParsing
if ($response.StatusCode -eq 200) {
    Write-Output "Post exists"
} else {
    Write-Output "Post not found"
}
```