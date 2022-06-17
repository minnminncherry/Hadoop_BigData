# Jupyter-installation on Ubuntu
This repo shows that how to set up jupyter lab from your own PC and VM

<code>export "JUPYTER_CONFIG_DIR=/home/mmc/jupyterlab"</code>

<code>sudo apt install python</code>

<code>sudo apt install -y python3-pip</code>

<code>python3 --version</code>

<code>pip install virtualenv</code>

<code>virtualenv --version</code>

<code>virtualenv py30</code>

<code>source /home/mmc/py30/bin/activate</code>

<code>pip install jupyter</code>

<code>jupyter --version</code>

<code>pip install jupyterlab</code>

<code>jupyter-notebook --generate-config</code>

<code>vim jupyter_notebook_config.py</code>

<code>
    → c.NotebookApp.allow_origin = '*'
    → c.NotebookApp.ip = 'your ip'
    → c.NotebookApp.port = 8888
</code>

<code>jupyter notebook password</code>

<code>mkdir /home/mmc/Desktop/jupyterlab</code>

<code>sudo vim /etc/systemd/system/jupyter-lab.service</code>

<code>[Unit]
Description=Jupyter Lab
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
WantedBy=multi-user.target</code>

<code>sudo systemctl daemon-reload</code>

<code>sudo systemctl enable jupyter-lab.service</code>

<code>sudo systemctl enable jupyter-lab.service</code>

<code>sudo systemctl status jupyter-lab.service</code>
