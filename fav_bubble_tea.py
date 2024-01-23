# Bubble Tea Popularity Algorithm
# Author: Ricco Chong
#Date 27 october 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data

NUM_RESPONDENTS =  5

coco_likes = 0
suntea_likes = 0
xingfutang_likes = 0
chatime_likes = 0
bbqeen_likes = 0

for _ in range(NUM_RESPONDENTS):

    # Ask the user what their favourite bubble tea place is
    print("What's your favourite bubble tea play? ")
    fave_bbt = input().strip(".<!?").lower()

    # Talling/ counting algo
    # Options: CoCo, Chatime, SunTea, xing fu tang, Bubble queen
    # if they say CoCo, increase the counter for CoCo by one, etc
    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "bbqeen":
        bbqeen_likes += 1
    elif fave_bbt == "xingfutang":
        xingfutang_likes += 1
    else:
        print("error")

#print out the results
print(f"CoCo Likes: {coco_likes} | {coco_likes/NUM_RESPONDENTS * 100}%")
print(f"Chatime likes: {chatime_likes} | {chatime_likes/NUM_RESPONDENTS * 100}%")
print(f"Suntealikes: {suntea_likes} | {suntea_likes/NUM_RESPONDENTS * 100}%")
print(f"Bbqeen likes: {bbqeen_likes} | {bbqeen_likes/NUM_RESPONDENTS * 100}%")
print(f"XingFuTang like: {xingfutang_likes} | {xingfutang_likes/NUM_RESPONDENTS * 100}%")