#!/usr/bin/env python3
import psutil

import time

import logging

import os

logging.basicConfig(level=logging.INFO,
                    filename="process.log",
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

old_set = set(list(psutil.process_iter()))
while True:
    new_set = set(list(psutil.process_iter()))
    added = new_set - old_set
    for p in added:
        logging.info(f"New process: {p.name()} (PID: {p.pid})")
        print("New", p)
    old_set = new_set
    time.sleep(5.0)

