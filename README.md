# Jupyter-installation on Ubuntu
This repo shows that how to set up jupyter lab from your own PC and VM

Give folder directory that you installed. Not using this config directory install in home/.jupyter folder <br/>
```
export "JUPYTER_CONFIG_DIR=/home/mmc/jupyterlab"
```

If you don't have python in your computer, please install with this command <br/>
```
sudo apt install python
```

pip install <br/>
```
sudo apt install -y python3-pip
```

When you finished python installation, can check the python version in computer <br/>
```
python3 --version
```

Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories. <br/>
```
pip install virtualenv
```

Make sure virtualenv installation. <br/>
```
virtualenv --version
```

Create python virtual enviroment <br/>
```
virtualenv py30
```

Activate virtual env <br/>
```
source py30/bin/activate
```

Install jupyter notebook <br/>
```
pip install jupyter
```

Make sure Jupyter version for installation <br/>
```
jupyter --version
```

install Jupyter lab <br/>
```
pip install jupyterlab
```

Generate config file for jupyter notebook <br/>
```
jupyter-notebook --generate-config
```

Change note book config file. <br/>
```
vim jupyter_notebook_config.py

    → c.NotebookApp.allow_origin = '*'
    → c.NotebookApp.ip = 'your ip'
    → c.NotebookApp.port = 8888
```

Add password for jupyter notebook password <br/>
```
jupyter notebook password
```

Create Workspace <br/>
```
mkdir /home/mmc/Desktop/jupyterlab
```

Create jupyter lab service <br/>
```
sudo vim /etc/systemd/system/jupyter-lab.service
```

```
[Unit]
Description=Jupyter Lab <br/>
[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/mmc/py30/bin/jupyter-lab --config=/home/mmc/jupyterlabjupyter_notebook_config.py
WorkingDirectory=/home/mmc/Desktop/jupyterlab
User=mmc
Group=mmc
Restart=always
RestartSec=10
#KillMode=mixed
[Install]
WantedBy=multi-user.target
```

Reload for jupyter lab service <br/>
```
sudo systemctl daemon-reload
```

```
sudo systemctl enable jupyter-lab.service
```

```
sudo systemctl enable jupyter-lab.service
```

```
sudo systemctl status jupyter-lab.service
```
