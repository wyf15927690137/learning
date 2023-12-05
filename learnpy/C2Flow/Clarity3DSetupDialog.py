import request


class OptionsData:
    def __init__(self):
        self.m_autoResume = False
        self.m_resume = False
        self.m_finalOnly = False
        self.m_sendMail = False
        self.m_isReconnect = False
        self.m_mail = ""
        self.m_parallelCount = 2
        self.m_downloadFilter = ""
        self.m_isC2PowerMode = False


class SSHData:
    def __init__(self):
        self.m_computerName = ""
        self.m_slotsPerComputer = 1
        self.m_sourceType = ""
        self.m_gpuCount = 1


class QueueData:
    def __init__(self):
        self.m_queueName = ""
        self.m_CPUPerSlot = 1
        self.m_minimumMemoryPerSlot = 1


class SSHDataList:
    def __init__(self):
        self.m_dataList = SSHData()
        self.m_queueData = QueueData()


class LSFData:
    def __init__(self):
        self.m_slotsPerComputer = 1
        self.m_computersNum = 1
        self.m_useServerFarmQueue = True
        self.m_ServerFarmQueueName = ""
        self.m_submitCommand = "bsub"
        self.m_path = ""
        self.m_separator = ""
        self.m_userDefinedParamter = ""
        self.m_CPUPerSlot = 4
        self.m_minimumMemoryPerSlot = 32000
        self.m_enableCPUTime = True
        self.m_enableTimeHint = True
        self.m_CPUTime = 48
        self.m_TimeHint = 48
        self.m_lsf_mem_unit = "M"
        self.m_enableMaterComputer = False
        self.m_masterUserDefinedParamter = ""
        self.m_masterComputerCPUs = 4
        self.m_masterComputerMemory = 32000
        self.m_GPUCount = 1

    def totalCPUs(self):
        nSlots = self.m_computersNum * self.m_slotsPerComputer
        nCpus = nSlots * self.m_CPUPerSlot

        if self.m_enableMaterComputer:
            nCpus = nCpus + self.m_masterComputerCPUs

        return nSlots, nCpus


class FilesData:
    def __init__(self):
        self.m_files = []


class RemoteSimuConfigData:
    def __init__(self):
        self.m_remoteIP = ""
        self.m_remotePort = ""
        self.m_clarityVersion = ""
        self.m_caseFolderPath = ""
        self.m_isRemoteSimu = False
        self.m_simuType = 0


class AtlasEnvCheck:
    def __init__(self):
        self.m_env_checker = "atlas_env_checker.sh"
        self.m_env_checker_retry_limit = 2
        self.m_env_checker_retry_delay_sec = 10
        self.m_env_checker_fatal = False
        self.m_default = True

class ClaritySetupData:
    def __init__(self):
        self.m_type = 0
        self.m_work_flow = ""
        self.m_feature_name = ""
        self.m_feature_pipe = ""
        self.m_simu_flow = ""
        self.m_optionsData = OptionsData()
        self.m_SSHList = SSHDataList()
        self.m_defaultSSHData = SSHData()
        self.m_LSFData = LSFData()
        self.m_fileData = FilesData()
        self.m_remoteConfData = RemoteSimuConfigData()
        self.m_atlasEnvCheck = AtlasEnvCheck()

    def computeTotalCpuForSingleCase(self):
        nSlots, nCpus = self.computeSlotAndCpu()
        return nCpus

    def computeSlotAndCpu(self):
        usingLSFData = self.m_LSFData
        nSlots, nCpus = usingLSFData.totalCPUs()
        return nSlots, nCpus

class ClaritySetupDialog:
    def __init__(self):
        self.m_claritySetupData = ClaritySetupData()

    def saveToClarity3DSetupData(self):
        if self.m_claritySetupData is None:
            return False

    def saveOptionsToData(self):
        dataConf = OptionsData()
        return dataConf
