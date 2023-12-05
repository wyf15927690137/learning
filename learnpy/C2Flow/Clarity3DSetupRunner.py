from Clarity3DSetupUtils import LicenseHolder
from Clarity3DSetupHttpC2 import C2CloudJobManager

class C2SimulationRunner:
    def __init__(self):
        self.m_licRemotes = LicenseHolder()

    def getC2CloudInstance(self):
        self.m_licRemotes.m_host_id = "1"

    def run(self):
        pass

    def listUserJobListOnC2(self):
        pass

    def getC2CloudManagerInstance(self):
        C2CloudJobManager().getC2CloudInstance()

if __name__ == "__main__":
    runner = C2SimulationRunner()
    runner.run()