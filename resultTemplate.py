def resultTemplate(playerStrength, enemyStrength, result):

    if result == True:
        msg = "wins"
    else:
        msg = "loses"
    return """
Player strength: {}
Enemy strength: {}
Player {}!
""".format(playerStrength, enemyStrength, msg)

print resultTemplate(1,2,False)
