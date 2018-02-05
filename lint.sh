#!/bin/sh

CYAN='\033[1;36m'
PURPLE='\033[1;35m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
RED='\033[1;31m'
NC='\033[0m'

DIRS=`find . -maxdepth 1 -type d`
PYLINTARGS="--rcfile=.pylintrc --disable=I0011"
PYLINT="pylint $PYLINTARGS"
PYLINTERR="pylint -E $PYLINTARGS"
CHANGED=`{ git diff --name-only ; git diff --name-only --staged ; } | sort | uniq | grep ".py"`
RETCODE=0


if [ "$1" = "--git" ]
then
    for file in $CHANGED; do
        echo "${YELLOW}Linting${NC} ${PURPLE}$file${NC}"
        $PYLINT -f colorized $file
    done
else
	for dir in $DIRS; do
		if [ -e "$dir/__init__.py" ]
		then
            echo "${YELLOW}Linting${NC} ${CYAN}$dir${NC}"
			$PYLINT -f colorized $dir
			if [ $? -ne 0 ]
			then
				RETCODE=1
				# Error
			fi
		fi
	done
fi

if [ $RETCODE = 0 ]
then
    echo "${GREEN}Lint success!${NC}"
else
    echo "${RED}Lint failure!${NC}"
fi


exit $RETCODE
