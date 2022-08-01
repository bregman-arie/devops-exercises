## CI for Open Source Project

1. Choose an open source project from Github and fork it
2. Create a CI pipeline/workflow for the project you forked
3. The CI pipeline/workflow will include anything that is relevant to the project you forked. For example:
  * If it's a Python project, you will run PEP8
  * If the project has unit tests directory, you will run these unit tests as part of the CI
4. In a separate file, describe what is running as part of the CI and why you chose to include it. You can also describe any thoughts, dilemmas, challenge you had

### Bonus

Containerize the app of the project you forked using any container engine you would like (e.g. Docker, Podman).<br>
Once you successfully ran the application in a container, submit the Dockerfile to the original project (but be prepared that the maintainer might not need/want that).

### Suggestions for Projects

The following is a list of projects without CI (at least at the moment):

Note: I wrote a script to find these (except the first project on the list, of course) based on some parameters in case you wonder why these projects specifically are listed.

* [This one](https://github.com/bregman-arie/devops-exercises) - We don't have CI! help! :)
* [image retrieval platform](https://github.com/skx6/image_retrieval_platform)
* [FollowSpot](https://github.com/jenbrissman/FollowSpot)
* [Pyrin](https://github.com/mononobi/pyrin)
* [food-detection-yolov5](https://github.com/lannguyen0910/food-detection-yolov5)
* [Lifely](https://github.com/sagnik1511/Lifely)
