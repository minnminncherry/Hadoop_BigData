# Jupyter-installation on Ubuntu
This repo shows that how to set up jupyter lab from your own PC and VM

Give folder directory that you installed. Not using this config directory install in home/.jupyter folder <br/>
<code>export "JUPYTER_CONFIG_DIR=/home/mmc/jupyterlab"</code>

If you don't have python in your computer, please install with this command <br/>
<code>sudo apt install python</code>

pip install <br/>
<code>sudo apt install -y python3-pip</code>

When you finished python installation, can check the python version in computer <br/>
<code>python3 --version</code>

Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories. <br/>
<code>pip install virtualenv</code>

Make sure virtualenv installation. <br/>
<code>virtualenv --version</code>

Create python virtual enviroment <br/>
<code>virtualenv py30</code>

Activate virtual env <br/>
<code>source py30/bin/activate</code>

Install jupyter notebook <br/>
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
