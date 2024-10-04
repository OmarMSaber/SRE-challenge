# Kubernetes Configurations

This folder contains two Kubernetes resources: a **Deployment** for an API and a **CronJob** for a periodic task.

## Files

### 1. `deployment.yaml`
- **Purpose**: Deploys 3 replicas of the `strm/helloworld-http:latest` container.
- **Port**: Exposes port 80.
- **Liveness Probe**: TCP check on port 80, with an initial delay of 10 seconds.
- **Readiness Probe**: HTTP GET to `/` on port 80, 1-second interval, marked "unready" after 2 failures.

#### Usage:
```bash
kubectl apply -f deployment.yaml
```


### 2. `cronjob.yaml`
Defines a **CronJob** that runs a simple task every 30 minutes.

- **Schedule**: Runs every 30 minutes (`*/30 * * * *`).
- **Command**: Executes `echo "Hello SRE"` in a `busybox` container.
- **Restart Policy**: Set to `OnFailure`, meaning the job will restart only if it fails.

### Key Sections:
- **Schedule**: The job is triggered at regular intervals (every 30 minutes).
- **Command**: Executes the command to output `"Hello SRE"`.

## Usage

To apply the CronJob to your Kubernetes cluster, run the following command:

```bash
kubectl apply -f cronjob.yaml
```