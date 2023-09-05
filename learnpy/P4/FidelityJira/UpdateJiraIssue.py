from UtilsForP4AndJira import P4Conn, JiraTool, Config
import sys

if __name__ == "__main__":
    p4port = sys.argv[1]
    changelist = sys.argv[2]

    con = P4Conn(Config.p4user, Config.p4pwd, p4port)
    con.con()
    jissue = con.getJiraIssue(changelist)
    print("Jira Issue is: " + str(jissue))

    jira = JiraTool(Config.jusr, Config.jtoken)
    jira.updateJiraIssueComment(jissue, changelist)
