#!/usr/bin/python3
import twint

c = twint.Config()

c.Search = "RemoteSensing"
c.Store_csv = True
# CSV Fieldnames
c.Custom = ["username", "date", "time","tweet"]
c.Output = "RemoteSensing.csv"

twint.run.Search(c)