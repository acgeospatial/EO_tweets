#!/usr/bin/python3
import twint

c = twint.Config()

c.Search = "RemoteSensing"
c.Store_csv = True
# CSV Fieldnames

c.Output = "RS"

twint.run.Search(c)