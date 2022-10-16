# Node Selectors

## Objectives

1. Apply the label "hw=max" on one of the nodes in your cluster
2. Create and run a Pod called `some-pod` with the image `redis` and configure it to use the selector `hw=max`
3. Explain why node selectors might be limited


## Solution

Click [here](solution.md) to view the solution

1. `kubectl label nodes some-node hw=max`
2. 

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```

3. Assume you would like to run your Pod on all the nodes with with either `hw` set to max or to min, instead of just max. This is not possible with nodeSelectors which are quite simplified and this is where you might want to consider `node affinity`.