
class Config:
    BridgeServerHost = "https://sjf-cpgmsa10:5000"
    # BridgeServerHost = "https://shsirdlnx2:5000"  #for local debug
    # BridgeServerHost = "https://127.0.0.1:8000"  #for local debug
    BridgeServerWindowsPath = BridgeServerHost + "/windows"
    BridgeServerLinuxPath = BridgeServerHost + "/linux"
    BridgeServerCheckAllowSubmit = BridgeServerHost + "/checkallowsubmit"
    BridgeServerCheckCCRNote = BridgeServerHost + "/test-ccr-note"
    BridgeServerVersion = "20230711"

    SigritySHP4 = "ssl:p4shanghai:2644"
    SigrityUSP4 = "ssl:sigbroker:1644"
    FidelityP4 = "ssl:p4broker1:1660"
    SigrityP4Usr = "cc"
    SigrityP4UsrPwd = "QzJkZW5jZUAyMDIx"
    FidelityP4Usr = "cc"
    FidelityP4UsrPwd = "QzJkZW5jZUAyMDIx"

    vc_user_list = ["jarodliu", "jcchen", "hjbu", "lili17", "scai", "jianc", "yunfeiz", "nathanai", "nali", "huah",
                    "ljiang", "jwzhang", "tianzuoz", "sunyx", "junepy", "jwang", "clarkwu", "xiongx", "patrickh",
                    "chllv", "landjin", "gkang", "huiqi", "mazenb", "jianhua", "xiaoming", "tedwang",
                    "zmj", "hguo", "yliu", "miaomiao", "keely", "hufugang", "taowei", "yunfeiz", "yuanliu", "stimit","qinliu","wurongy","yinglong"]

    #Branch Tag String
    BranchMain = "main"
    BranchIsr = "isr"
    ProductSigrity = "sigrity"
    ProductFidelity = "fidelity"

    JobAll = "All_Project"
    JobCGC = "CGC_Project"
    JobFidelity = "Fidelity_Project"

    TagMainSigrity = "//depot/sigrity/main/", BranchMain
    TagIsrSigrity = "//depot/sigrity/23.10/ISR1/", BranchIsr
    TagMainFidelity = "//depot/fidelity/trunk/", BranchMain
    TagIsrFidelity = "//depot/fidelity/releases/fidelity2023.x/", BranchIsr

    @staticmethod
    def getBridgeServerProjectUrl(platform):
        if str(platform).lower() == "windows" or str(platform).lower() == "windows-linux":
            return Config.BridgeServerWindowsPath
        return Config.BridgeServerLinuxPath

    def __init__(self):
        pass
