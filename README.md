# clone-mdb-docs

This script: 

- clones all of a writer's forks of MongoDB documentation repos, and
- sets the upstream appropriately for each cloned fork.

It is designed to:

- speed up the onboarding process for new writers with MongoDB, and
- simplify migrating a writer's workload to a new physical or virtual machine.

## Clone your Forks

To clone your forks to a new machine:

1. On the machine to which you want to clone your forks, [generate an SSH key](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).
2. [Add the key you generated to your GitHub account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
3. Clone this repository.
4. Navigate to the `clone-mdb-docs` directory.
5. Run the `clone-mdb-docs-repos.py` script. Pass your GitHub username as an argument:

   ```
   python3 clone-mdb-docs-repos.py jwilliams-mongo
   ```
   
 When the script completes, it returns a list of repositories that it did not clone because:
 
 - You have not forked them, or
 - You have already cloned them.
 
## Troubleshooting 
 
If all repos appear in the `repos not cloned because you need to fork` list, ensure that you've [added the correct SSH key to your Github account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
