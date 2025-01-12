## "Killing" Containers - Solution

1. Run Pod with a web service (e.g. httpd) - `kubectl run web --image registry.redhat.io/rhscl/httpd-24-rhel7`
2. Verify the web service is running with the `ps` command - `kubectl exec web -- ps`
3. Check how many restarts the pod has performed - `kubectl get po web`
4. Kill the web service process -`kubectl exec web -- kill 1`
5. Check how many restarts the pod has performed - `kubectl get po web`
6. Verify again the web service is running - `kubectl exec web -- ps`

## After you complete the exercise


* Why did the "RESTARTS" count raised? - `Kubernetes restarted the Pod because we killed the process and the container was not running properly.`