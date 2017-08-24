#!/usr/bin/env bash


## Variables
scriptPath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
templateDir=~/Templates

# create Template directory if it doesn#t exist
if [ ! -d "$templateDir" ]; then
    echo "Creating Template directory."
    mkdir -p $templateDir
fi

# remove all existing templates and symlinks in ~/Templates
if [ "$(ls -A $templateDir)" ]; then
    echo "Deleting existing templates."
    for file in $templateDir/*; do
        rm -r "$file"
    done
fi

# copy all tempates
echo "Copying all templates to $templateDir."
for file in * .[^.]*; do

    if [ "$file" != "README.md" ] && [ "$file" != "setup.sh" ] && [ "$file" != ".git" ]; then

        if [ -d "$file" ]; then
            cp -a "$scriptPath/$file/." "$templateDir/$file/"
        else
            cp "$scriptPath/$file" "$templateDir/$file"
        fi
        
    fi
    
done

echo "Done!"

