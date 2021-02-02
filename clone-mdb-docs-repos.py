import subprocess
import sys
import os

tengen = "10gen"
mongodb = "mongodb"

try:
    github_username = sys.argv[1]
except:
    print("################################################################################")
    print("you did not include your github username.")
    print("please run the script again and provide your github username as an argument.")
    print("")
    print("Example:")
    print("")
    print("python3", sys.argv[0], "jwilliams-mongo")
    print("################################################################################")
    exit()

not_forked = []
not_cloned = []

# lists of mdb docs repositories as of Nov 24 2020

tengen_repo_list = [
    "mms-docs",
    "cloud-docs",
    "docs-charts",
    "docs-k8s-operator",
    "cloud-docs-osb",
    "docs-mongocli",
    "docs-datalake",
    "docs-kafka-connector",
    "docs-realm-sdks",
    "docs-tutorials"
]
mongodb_repo_list = [
    "docs-assets",
    "docs-tools",
    "docs",
    "docs-ecosystem",
    "docs-primer",
    "docs-compass",
    "docs-bi-connector",
    "docs-spark-connector",
    "docs-mongodb-shell",
    "mongodb-kubernetes-operator",
    "docs-realm",
    "docs-commandline-tools",
    "docs-worker-pool",
    "docs-tools",
    "docs-landing"
]
def run(*args):
    return subprocess.check_call(list(args))

def clone_repo(user, repo):
        print("######## cloning " + repo + " ...")
        run("git", "clone", "git@github.com:" +  github_username + "/" + repo + ".git")
        os.chdir(repo)
        run("git", "remote", "add", "upstream", "git@github.com:" + user + "/" + repo + ".git")
        run("git", "fetch", "--all")
        if repo == "docs-realm-sdks":
            run("git", "branch", "-u", "upstream/latest")
        else:
            run("git", "branch", "-u", "upstream/master")
        os.chdir("..")

def clone_tengen():
    for repo in tengen_repo_list:
        try:
            # tries to change to repo directory. if it doesn't exist, script clones the repo.
            os.chdir(repo)
            os.chdir("..")
            not_cloned.append(repo)
            print("######## repo", repo, "exists. skipping.")
        except: 
            try:
                clone_repo(tengen, repo)
            except:
                not_forked.append(repo)
                # assumes reason for failure is that no fork exists.
                print("######## cloning " + repo + " failed. Make sure that you've forked this repository.")

def clone_mongodb():
    for repo in mongodb_repo_list:
        try:
            # tries to change to repo directory. if it doesn't exist, script clones the repo.
            os.chdir(repo)
            os.chdir("..")
            not_cloned.append(repo)
            print("######## repo", repo, "exists. skipping.")
        except:            
            try:
                clone_repo(mongodb, repo)
            except:
                not_forked.append(repo)
                # assumes reason for failure is that no fork exists.
                print("######## cloning " + repo + " failed. Make sure that you've forked this repository.")

def print_not_forked():
    print("######## repos not cloned because you need to fork:")
    if len(not_forked) > 0:
        for repo in not_forked:
            print(repo)
        print("")
    else:
        print("")

def print_not_cloned():
    print("######## repos not cloned because they already exist:")
    if len(not_cloned) > 0:
        for repo in not_cloned:
            print(repo)
    else:
        print("")

clone_tengen()

clone_mongodb()

print_not_forked()

print_not_cloned()