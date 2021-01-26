# ClearML agent for slurm

* Create environment

```
mkvirtualenv clearml-agent
pip install -r requirements.txt
```
* Copy the service file to the appropriate systemd directory

```
cp utils/slurm-clearml-worker.service /etc/systemd/system/
```

* Services
    * List services use `sudo systemctl --type=service`
    * Reload services (after changing a service file) `sudo systemctl daemon-reload`
    * Start service `sudo systemctl start slurm-clearml-worker`
    * Enable automatically after rebooting `sudo systemctl enable slurm-clearml-worker`
