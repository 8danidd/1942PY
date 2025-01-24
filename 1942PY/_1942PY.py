# Activity 1

# Introduction
# It is 1942 and World War II is at its final stage, so it is critical to have
# a reliable communication channel to transfer messages.

# There is a rudimentary machine for that communication, but it is quite slow
# (remember, it is 1942...) and all the sent and received messages have to be manually processed.

# To replace that slow machine, you are in charge of the important task
# of implementing an automatic mechanism to send and receive messages.

# It is important to take also into account the military ranks when sending
# and receiving a message. The military ranks are, from higher to lower:
# Admiral > Captain > Commander > Lieutenant > Officer

# If the sender of a message has a higher rank than the receiver,
# the first field of the transmitted message will be the word "URGENT",
# and the interpretation of the received message must start with
# "<<< URGENT >>>" always (a received message could be
# missing that word due to an error when sending it).
#
# Input
# The first line of the input is a word which must contain either "S"
# or "R" to indicate that we have to "send" or "receive" a message, respectively.

# If the first line is "S", it will be followed by 6 lines, each one
# of them being: the name of the sender, the rank of the sender, the name of the receiver,
# the rank of the receiver, the message text and the time in the
# format hhmm (being hh the hour and mm the minute).

# If the first line is "R", it will be followed by a single line
# containing all the data of the message that has been received.
#
# Output
# If the input is a message that has to be sent (S), the output must be the transmitted message in a single line, with all the input fields separated by commas.
# Remember to put an extra field "URGENT" at the beginning of the message if the rank of the sender is higher than the rank of the receiver.
# If the input is a received message (R), the output must be the interpretation of that message, as shown in the Example 2 below.
# If it is an "URGENT" message, remark that putting the word in between "<<< >>>", as shown in Example 2.
# If the first line is neither "S" nor "R", you must indicate that there is an error in the input by showing the message "Invalid input.".
# Show that message also if any of the given military ranks is invalid. Be careful, because both sent and received messages may contain an invalid rank.
#
# Example 1
# Input
# S
# Bobby Shaftoe
# Lieutenant
# Lawrence Waterhouse
# Officer
# Bring coffee!
# 2357
# Output
# URGENT,Bobby Shaftoe,Lieutenant,Lawrence Waterhouse,Officer,Bring coffee!,2357
#
# Example 2
# Input
# R
# Bobby Shaftoe,Lieutenant,Lawrence Waterhouse,Officer,Bring coffee!,2357
# Output
# <<< URGENT >>>
# From: Bobby Shaftoe
# From rank: Lieutenant
# To: Lawrence Waterhouse
# To rank: Officer
# Content: Bring coffee!
# Timestamp: 2357
#
# Example 3
# Input
# M
# URGENT,Bobby Shaftoe,Lieutenant,Lawrence Waterhouse,Officer,Bring coffee!,2357
# Output
# Invalid input.

y = 0
ranks = {"Admiral": 5, "Captain": 4, "Commander": 3, "Lieutenant": 2, "Officer": 1}
message = [""] * 6
inputkey = str(input("Send or receive message (s/r): ")).lower()

if inputkey == "s":
    message[0] = input("Name: ")
    message[1] = input("Your Rank: ")
    message[2] = input("Receiver Name: ")
    message[3] = input("Receiver Rank: ")
    message[4] = input("Message: ")
    message[5] = input("Time (hhmm): ")

    if message[1 and 3] in ranks:

        if ranks[message[1]] > ranks[message[3]]:
            print("URGENT", end=", ")
        for word in message:
            print(message[y], end=", ")
            y = y + 1
    else:
        print("Invalid Input")
        exit()

elif inputkey == "r":

    urgent = False
    offset = 0
    fullMessage = input("Message: ")
    messageSplit = fullMessage.split(",")


    if messageSplit[2 and 4 + offset] in ranks:
        if messageSplit[0] == "URGENT":
            urgent = True
        elif ranks[messageSplit[1]] > ranks[messageSplit[3]]:
            urgent = True
            offset = -1
        else:
            offset = -1
        if urgent == True:
            print("<<< URGENT >>>")
        print(f"From: {messageSplit[1 + offset]}")
        print(f"From Rank: {messageSplit[2 + offset]}")
        print(f"To: {messageSplit[3 + offset]}")
        print(f"To Rank: {messageSplit[4 + offset]}")
        print(f"Content: {messageSplit[5 + offset]}")
        print(f"Timestamp: {messageSplit[6 + offset]}")
    else:
        print("Invalid Input")
        exit()

else:
    print("Invalid Input")