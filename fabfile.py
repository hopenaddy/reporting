from fabric.api import put, run
from fabvenv import Venv

ROOT = "/opt/lv128/reporting"
def deploy():
	venv = Venv(ROOT, "requirements.txt")
	if not venv.exists():
		venv.create()
		venv.install()
put("manage.py", ROOT)
put("lv128.service", ROOT)
run("sudo mv %s/lv128.service /etc/systemd/system/" % ROOT)
run("sudo systemctl enable lv128")
run("sudo systemctl restart lv128")
