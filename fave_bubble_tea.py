# Bubble Tea Popularity Algorithm 
# Author: Miles Ty
# Date: Oct 27th, 2023

NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite bbt place is
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(",.?! ").lower()

    # Tallying/Counting Algo
    # Options: CoCo, Chatime, SunTea, Xing Fu Tang, Bubble Queen
    # If they say CoCo, increase the counter for CoCo by one, etc.
    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "xingfutang":
        xingfutang_likes += 1
    elif fave_bbt == "bbqueen":
        bbqueen_likes += 1

# Print a summary of the results
print(f"CoCo Likes: {coco_likes}")
print(f"Chatime Likes: {chatime_likes}")
print(f"Suntea Likes: {suntea_likes}")
print(f"XingFuTang Likes: {xingfutang_likes}")
print(f"BbQueen Likes: {bbqueen_likes}")
