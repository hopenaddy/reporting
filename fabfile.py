from fabric.api import put, run
from fabvenv import Venv

ROOT = "/opt/lv128/reporting"
def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("manage.py", ROOT)
    put("lv128_reporting.service", ROOT)
    run("sudo mv %s/lv128_reporting.service /etc/systemd/system/" % ROOT)
    run("sudo systemctl enable lv128_reporting")
    run("sudo systemctl restart lv128_reporting")
