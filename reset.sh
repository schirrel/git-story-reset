#!/bin/sh
mergeCommit=

echo "Getting commits after merge"
commits=$( git rev-list  $mergeCommit...HEAD --reverse)
echo "Commit hashs: $commits"

echo "---"
echo "Getting commit before merge"
prev=$( git rev-parse --short $mergeCommit^1)
echo "Commit hashs: $prev"


echo "---"
echo "Executing reset --hard"
git reset --hard $prev


 echo "---"
 echo "Executing cherry pick"

 for commit in $commits
 do
    echo "Executing cherry pick of $commit"
  git cherry-pick $commit --strategy-option=theirs
 done 

git push --force 
