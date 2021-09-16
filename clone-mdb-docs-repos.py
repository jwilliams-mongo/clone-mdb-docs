import subprocess
import sys
import os

tengen = "10gen"
mongodb = "mongodb"


def try_to_get_sys_arg(argv_position, error_msg):
    try:
        return sys.argv[argv_position]
    except:
        print(error_msg)
        exit()

github_username = try_to_get_sys_arg(1, f"""
################################################################################
you did not include your github username.
please run the script again and provide your github username as an argument.

Example:
python3 {sys.argv[0]} jwilliams-mongo /Users/jwilliams/projects/
################################################################################
""")


path_to_repos = try_to_get_sys_arg(2, f"""
################################################################################
you did not include the desired path to repos.
please run the script again and provide the desired path to your repos.

Example:
python3 {sys.argv[0]} jwilliams-mongo /Users/jwilliams/projects/
################################################################################
""")
os.chdir(path_to_repos) # throws error if path doesn't exist


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

def fetch_and_clone_repo(gh_org, repo):
        os.chdir(path_to_repos)
        os.getcwd()
        print("######## cloning " + repo + " ...")
        run("gh", "repo", "fork", "https://github.com/" +  gh_org + "/" + repo + ".git", "--clone=true")
        os.chdir(path_to_repos + repo)
        run("git", "fetch", "--all")
        if repo == "docs-realm-sdks":
            run("git", "branch", "-u", "upstream/latest")
        else:
            run("git", "branch", "-u", "upstream/master")
        os.chdir(path_to_repos)


def fetch_and_clone_repos_by_org(gh_org, org_repo_list):
    for repo in org_repo_list: 
        try:
            # tries to change to repo directory. if it doesn't exist, script clones the repo.
            os.chdir(path_to_repos + repo)
            not_cloned.append(repo)
            print("######## repo", repo, "exists. skipping.")
        except: 
            try:
                fetch_and_clone_repo(gh_org, repo)
            except:
                not_forked.append(repo)
                # assumes reason for failure is that no fork exists.
                print("######## cloning " + repo + " failed. Make sure that you've forked this repository.") 


def print_error_repos(error_list, error_msg):
    print(error_msg)
    if len(error_list) > 0:
        for repo in error_list:
            print(repo)
        print("")
    else:
        print("")

def clone_tengen():
    fetch_and_clone_repos_by_org(tengen, tengen_repo_list)

def clone_mongodb():
    fetch_and_clone_repos_by_org(mongodb, mongodb_repo_list)

def print_not_forked():
    print_error_repos(not_forked, "######## repos not cloned because you need to fork:")

def print_not_cloned():
    print_error_repos(not_cloned, "######## repos not cloned because they already exist:")


clone_tengen()

clone_mongodb()

print_not_forked()

print_not_cloned()
