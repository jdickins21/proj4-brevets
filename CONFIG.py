"""
Configuration of vocabulary game server.
Generated Mon Oct 17 17:59:31 PDT 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="cc1b4cfc9d23b3b0851a19e8606c5679"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

