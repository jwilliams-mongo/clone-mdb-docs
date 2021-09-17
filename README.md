# clone-mdb-docs

This script: 

- forks and clones all MongoDB documentation repos, and
- sets the upstream appropriately for each cloned fork.

It is designed to:

- speed up the onboarding process for new writers with MongoDB, and
- simplify migrating a writer's workload to a new physical or virtual machine.

## Before You Begin
Before you get started running the script, you **must** set up the [Github CLI](https://cli.github.com/). 

You can do this by following these installation instructions: https://github.com/cli/cli#installation

## Clone your Forks

To clone your forks to a new machine:

1. On the machine to which you want to clone your forks, [generate an SSH key](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).
2. [Add the key you generated to your GitHub account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
3. Clone this repository.
4. Navigate to the directory into which you wish to clone your forks.
5. Run the `clone-mdb-docs-repos.py` script. Pass your GitHub username and desired location of the repos as arguments:

   ```shell
   python3 path/to/clone-mdb-docs-repo/clone-mdb-docs-repos.py jwilliams-mongo /Users/jwilliams/projects/
   ```
   
 When the script completes, it returns a list of repositories that it did not clone because:
 
 - You have not forked them, or
 - You have already cloned them.
 
## Troubleshooting 
 
If all repos appear in the `repos not cloned because you need to fork` list, ensure that you've [added the correct SSH key to your Github account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
