"""
Configuration of vocabulary game server.
Generated Sun Oct 23 15:39:36 PDT 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="6513ab6b3e651ea7d828612433a8a169"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

