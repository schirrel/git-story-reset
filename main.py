import os

mergedCommit = input("Enter the commit you want to revert: ")
mergedCommit = str(mergedCommit)

try:
    print("Getting commits after merge")
    commits = os.system(f"git rev-list {mergedCommit}...HEAD --reverse")
    print(f"Commit hashs: {commits}\n")

    print("\nGetting commit before merge")
    previeousCommit = os.system(f"git rev-parse --short {mergedCommit}^1")
    print(f"Commit hashs: {previeousCommit}\n")

    print("\nExecuting reset --hard")
    os.system(f"git reset --hard {previeousCommit}")
    print("\nExecuting cherry pick")

    for commit in commits:
        print(f"Executing cherry pick of {commit}")
        os.system(f"cherry-pick {commit} --strategy-option=theirs")

    os.system("git push --force")
except Exception:
    print(Exception)
    exit()
