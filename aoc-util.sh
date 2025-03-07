#!/usr/bin/env bash

# ------------------------------------------------------------------------------

# default
YEAR=2025

# ------------------------------------------------------------------------------

# set flag to exit when error
set -eo pipefail

# ------------------------------------------------------------------------------

# help function
show_help() {
  cat <<EOF

Usage: $(basename "$0") [-y YEAR] -d DAY OPTIONS

ARGUMENTS:
  -y  YEAR  (default: 2025)
  -d  DAY

OPTIONS:
  c  create files for given DAY in YEAR
  i  get input for given DAY in YEAR
  r  run program for given DAY in YEAR

Note:
  - YEAR must be in 4-digit format
  - DAY must be in range of 1 to 25
  - for 'r' option, YEAR and DAY can be 0.

Examples:
  $(basename "$0") -y2023 -d2 c
  --> create files for day 2

  $(basename "$0") -d2 r
  --> run program for day 2 for default YEAR

  $(basename "$0") -d0 r
  --> run program for ALL days in default YEAR

  $(basename "$0") -y0 r
  --> run program for ALL days in ALL years

EOF
  exit "$1"
}

# ------------------------------------------------------------------------------

aoc_create() {
  local src="${YEAR}/src/day${DDAY}.py"

  mkdir -p "${YEAR}/src/"
  mkdir -p "${YEAR}/input/"

  # copy from template if file not yet created
  if [[ ! -f $src ]]; then
    cp "${YEAR}/src/template.py" "$src"
    # todo: fix this
    sed -i "12s/Day00/Day$DDAY/" "$src"
    sed -i "16s/=\ 0/=\ $DAY/" "$src"
    sed -i "32s/Day00/Day$DDAY/" "$src"
  fi

  touch "${YEAR}/input/day${DDAY}.txt"
  touch "${YEAR}/input/day${DDAY}_test.txt"

  echo "INFO: AOC $YEAR Day $DDAY created"
}

get_input() {
  # if [[ $(date +%s) -lt $(date -d "${YEAR}-12-${DAY} 06:00" +%s) ]]; then
  #   echo "ERROR: AOC $YEAR Day $DDAY input not available"
  #   exit 1
  # fi

  local url="https://i18n-puzzles.com/puzzle/${DAY}/input"
  local input="${YEAR}/input/day${DDAY}.txt"
  echo $url

  mkdir -p "${YEAR}/input/"

  if curl --silent --fail "$url" \
    --cookie "session=$I18N_SESSION" \
    -A 'abidkyo @ github.com/abidkyo' \
    -o "$input"; then

    echo "INFO: AOC $YEAR Day $DDAY input downloaded"
  else
    echo "ERROR: AOC $YEAR Day $DDAY input not available"
    exit 1
  fi
}

aoc_run() {
  cd "$YEAR"

  local src="src/day${DDAY}.py"

  if [[ -f $src ]]; then
    ./"$src"
  else
    echo "ERROR: AOC $YEAR Day $DDAY program not found"
    exit 1
  fi

  cd ..
}

aoc_run_all() {
  local years
  years=$(ls -d 20*)

  for year in $years; do
    aoc_run_all_days "$year"
  done
}

aoc_run_all_days() {
  cd "$1"

  local srcs
  srcs=$(ls src/day*.py)

  for src in $srcs; do
    ./"$src"
  done

  cd ..
}

# ------------------------------------------------------------------------------

parse_args() {
  while getopts "cirhy:d:" opt; do
    case $opt in
    y)
      YEAR=$OPTARG
      ;;
    d)
      DAY=$OPTARG
      DDAY=$(printf "%02d" "$OPTARG")
      ;;
    c)
      AOC_CREATE=1
      ;;
    i)
      GET_INPUT=1
      ;;
    r)
      AOC_RUN=1
      ;;
    h)
      show_help 0
      ;;
    *)
      echo "ERROR: unknown argument"
      show_help 1
      ;;
    esac
  done
  shift $((OPTIND - 1))

  if [[ -z $DAY && $YEAR -ne 0 ]]; then
    echo "ERROR: missing -d argument"
    show_help 1
  fi

  if [[ -z $AOC_CREATE && -z $GET_INPUT && -z $AOC_RUN ]]; then
    echo "ERROR: no argument given"
    show_help 1
  fi

  if ! [[ $DAY -ge 1 && $DAY -le 25 ]] && ! [[ -n $AOC_RUN && $DAY -eq 0 ]]; then
    echo "ERROR: DAY must be in range of 1 to 25 or 0 for 'r' options"
    exit 1
  fi
}

# ------------------------------------------------------------------------------

main() {
  parse_args "$@"

  cd "$(realpath "$(dirname "$0")")"

  if [[ -n $AOC_CREATE ]]; then
    aoc_create
  fi

  if [[ -n $GET_INPUT ]]; then
    get_input
  fi

  if [[ -n $AOC_RUN ]]; then
    if [[ $YEAR -eq 0 ]]; then
      aoc_run_all
    elif [[ $DAY -eq 0 ]]; then
      aoc_run_all_days "$YEAR"
    else
      aoc_run
    fi
  fi
}

# ------------------------------------------------------------------------------

main "$@"
exit $?

# ------------------------------------------------------------------------------
