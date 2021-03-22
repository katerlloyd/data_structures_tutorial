aliens = ["hopkinsville goblin", "grey", "silurian", "mothman", "grey", "venusian"]

# Create an empty set called alien_catalog.
alien_catalog = set()

# Add each alien to the alien_catalog one at a time.
alien_catalog.add("hopkinsville goblin")
alien_catalog.add("grey")
alien_catalog.add("silurian")
alien_catalog.add("mothman")
alien_catalog.add("grey") # This one will not actually be added since it is a duplicate.
alien_catalog.add("venusian")

# Check to see if there are any agarthans in your set.
if "agarthan" in alien_catalog:
    print("How did that get in there?")
else:
    print("We don't have any agarthans, sorry!")

# Remove the hopkinsville goblin since it escaped while you were talking to the trader.
alien_catalog.remove("hopkinsville goblin")