def partridge(words):
    alan_words = ["Partridge", "Pear Tree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]

    if words == []:
      return "Lynn I've pierced my foot on a spike!!"

    count_alan_words = 0

    for word in words:
        if word in alan_words:
            count_alan_words += 1

    pint = "Mine's a Pint!"

    if count_alan_words == 0:
       return "Lynn I've pierced my foot on a spike!!"

    for i in range(count_alan_words - 1):
      pint += "!"

    return pint


    

  