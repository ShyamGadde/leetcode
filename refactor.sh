#!/bin/bash

# Loop over each directory
for dir in */; do
    # Remove leading './' and trailing '/'
    dir="${dir%*/}"
    dir="${dir#*/}"

    # Replace spaces with hyphens, remove quotes, convert to lowercase, and keep the dot after the number
    new_name=$(echo "$dir" | tr -d "'" | sed 's/ /-/g' | tr '[:upper:]' '[:lower:]' | sed 's/\.-/./g')

    # Rename 'solution.py' to the new name
    mv "$dir/solution.py" "$new_name.py"

    # Remove the directory
    rmdir "$dir"
done

