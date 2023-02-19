#!/bin/sh

# remove database file
rm app/tests/database/test.sqlite

# run unit tests
pytest app/tests

